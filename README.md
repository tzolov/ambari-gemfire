[Ambari](https://ambari.apache.org/) Plugin for [Apache Geode](http://geode.incubator.apache.org/) ([GemFire](http://pivotal.io/big-data/pivotal-gemfire)) 
----
#### Build the geode-ambari-plugin
Clone the project and checkout the `geode` branch (master still points to gemfire)
```
git clone  git clone https://github.com/tzolov/ambari-gemfire.git geode-ambari-plugin
cd geode-ambari-plugin
git fetch --all
git checkout geode
```
Build the plugin with Gradle (for maven build see below)
```
./gradlew clean dist -PbuildDir=target
```
or build with Maven (just a wrapper around the gradle build)
```
mvn clean package
```
If successful the build artifacts are generated in `target\distribution\` 
```
ls -lah target/distributions/
3303 Jul 20 14:10 geode-ambari-plugin-0.1-1.tgz
7448 Jul 20 14:10 geode-ambari-plugin-hdp22-0.1-1.noarch.rpm
7453 Jul 20 14:10 geode-ambari-plugin-phd30-0.1-1.noarch.rpm
```
RPMs for `PHD3.0` and `HDP2.2` are generated as well as a compressed tarball. 
#### Install the plugin on `PHD3.0` using the geode-ambari-plugin-phd-1.0-2.noarch.rpm RPM.
Copy `geode-ambari-plugin-phd30-0.1-1.noarch.rpm` to your Ambari server and run
```
sudo yum -y ./geode-ambari-plugin-phd30-0.1-1.noarch.rpm
```
Restart the Ambari Server
```
sudo /etc/init.d/ambari-server restart
```
#### Use the plugin to deploy Geode cluster via Ambari
1. Login to Ambari server
2. Form the `Services` view press `Actions`/`+Add Services` option.
3. Then choose `Geode` service and press `Next`.
4. Select a host for the Geode Locator component and press `Next`.
5. Select hosts for the Goede Server components. Note that you can not collocate Geode Locator with Geode Servers!
6. Press `Next`.
7. Open the geode-site.xml configuration panel. By default the geode plugin will check if the `geode.installation.file.path` points to a valid geode tarball. If no tarball is present locally the plugin will use `geode.installation.file.download.url` to download one. By the default plugin will use the: https://dl.dropboxusercontent.com/u/79241625/apache-geode-1.0.0-incubating-SNAPSHOT.tar.gz tarball. You can modify the download URL or provide the geode tarball locally by set `geode.installation.file.path`. Note that the local tarball must be present on all servers and locators at the same path.
8. Press `Next` to finish the deployment. 



