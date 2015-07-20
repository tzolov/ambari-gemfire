from resource_management import *

config = Script.get_config()

# common configs
java64_home = config['hostLevelParams']['java_home']

# geode user
geode_user = config['configurations']['geode-site']['geode.user']

# geode group
geode_group = config['configurations']['geode-site']['geode.group']

# geode user password
geode_password = config['configurations']['geode-site']['geode.user.password']

# geode installation directory
geode_install_dir = config['configurations']['geode-site']['geode.installation.directory']

# geode locator working directory
geode_locator_dir = config['configurations']['geode-site']['geode.locator.working.directory']

# geode locator port
geode_locator_port = config['configurations']['geode-site']['geode.locator.port']

# geode server working directory
geode_server_dir = config['configurations']['geode-site']['geode.server.working.directory']

# geode server port
geode_server_port = config['configurations']['geode-site']['geode.server.port']

# geode tarball
geode_tarball_path = config['configurations']['geode-site']['geode.installation.file.path']

# geode tarball download URL
geode_tarball_download_url = config['configurations']['geode-site']['geode.installation.file.download.url']

# Locator properties file
geode_locator_properties_file = config['configurations']['geode-site']['geode.locator.properties.file']

# Serer properties file
geode_server_properties_file = config['configurations']['geode-site']['geode.server.properties.file']

# geode install target
geode_install_target = geode_install_dir + '/geode'

# geode locator hostname
geode_locator_hostname = config['clusterHostInfo']['geode_locator_hosts'][0]

# geode env configs
geode_env_sh_template = config['configurations']['geode-env']['content']
conf_dir = "/etc/geode/conf"
