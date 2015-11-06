from resource_management import *

class Master(Script):

	def geode_user_exists(self):
		import pwd
		import params
		try:
			pwd.getpwnam(params.geode_user)
			return True
		except KeyError:
			return False

	def install(self, env):
		import os
		import params
		import urllib
		
		env.set_params(params)

		self.configure(env)
		
		if not (os.path.exists(params.geode_tarball_path) and os.path.isfile(params.geode_tarball_path)) :
			print "Downloading tarball from: %s to: %s" % (params.geode_tarball_download_url, params.geode_tarball_path)
			geodeTarball = urllib.URLopener()
                        geodeTarball.retrieve(params.geode_tarball_download_url, params.geode_tarball_path)
    
		cmd = 'tar -zvxf ' + params.geode_tarball_path + ' -C ' + params.geode_install_dir
		Execute(cmd, user=params.geode_user, timeout=300)

		cmd = 'ln -s ' + params.geode_install_dir + '/' + os.path.basename(params.geode_tarball_path).replace(".tar.gz", "").replace(".tgz", "") + ' ' + params.geode_install_target
		Execute(cmd, user=params.geode_user, timeout=300)

	def configure(self, env):
		import crypt
		import params

		env.set_params(params)

		if not self.geode_user_exists():
			Group(params.geode_group)
			User(params.geode_user,
				gid=params.geode_group,
				password=crypt.crypt(params.geode_password, 'salt'),
				groups=[params.geode_group],
				ignore_failures=True)

		Directory(params.geode_install_dir,
			owner=params.geode_user,
			group=params.geode_group,
			recursive=True)

		Directory(params.conf_dir,
			owner=params.geode_user,
			group=params.geode_group,
			recursive=True)

		Directory(params.geode_locator_dir,
			owner=params.geode_user,
			group=params.geode_group,
			recursive=True)

		File(format("{conf_dir}/geode-env.sh"),
			owner=params.geode_user,
			group=params.geode_group,
			content=InlineTemplate(params.geode_env_sh_template))

		File(format("{conf_dir}/locator.properties"),
			owner=params.geode_user,
			group=params.geode_group,
			content=InlineTemplate(params.geode_locator_properties_file))

	def start(self, env):
		import params
		env.set_params(params)

		self.configure(env)

		cmd = """
source {conf_dir}/geode-env.sh
gfsh >>{geode_locator_dir}/gfsh.log << EOF
start locator --name=locator-$HOSTNAME --port={geode_locator_port} --dir={geode_locator_dir} --properties-file={conf_dir}/locator.properties --J=-Xms128m --J=-Xmx128m
exit;
EOF"""
		Execute(format(cmd), user=params.geode_user, timeout=300)

	def stop(self, env):
		import params
		env.set_params(params)

		cmd = """
source {conf_dir}/geode-env.sh
gfsh >>{geode_locator_dir}/gfsh.log << EOF
stop locator --dir={geode_locator_dir}
exit;
EOF"""
		Execute(format(cmd), user=params.geode_user)

	def status(self, env):
		import status_params
		env.set_params(status_params)
		check_process_status(status_params.locator_pidfile)

if __name__ == '__main__':
	Master().execute()
