Ambari Plugin for [Apache Geode](http://geode.incubator.apache.org/) (GemFire) 
----
#### Quick Start  [ ![Download](https://api.bintray.com/packages/big-data/rpm/geode-ambari-plugin/images/download.svg) ](https://bintray.com/big-data/rpm/geode-ambari-plugin/_latestVersion)
Install the latest plugin RPM from public YUM repository. Add the yum repository to your CentOS/RedHat system, install the plugin and restart Ambari Server: 
```
sudo wget https://bintray.com/big-data/rpm/rpm -O /etc/yum.repos.d/bintray-big-data-rpm.repo
sudo yum -y install geode-ambari-plugin-phd30
sudo /etc/init.d/ambari-server restart
```
Above will install Geode plugin on PHD30 Hadoop distro. For HDP2.2 install `geode-ambari-plugin-hdp22` and for HDP2.3 install `geode-ambari-plugin-hdp23` instead.

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
3.3K Jul 26 18:16 geode-ambari-plugin-1.1-2.tgz
7.3K Jul 26 18:16 geode-ambari-plugin-hdp22-1.1-2.noarch.rpm
7.3K Jul 26 18:16 geode-ambari-plugin-hdp23-1.1-2.noarch.rpm
7.3K Jul 26 18:16 geode-ambari-plugin-phd30-1.1-2.noarch.rpm
```
RPMs for `PHD3.0` and `HDP2.2` are generated as well as a compressed tarball. 
#### Install the plugin on `PHD3.0` using the geode-ambari-plugin-phd RPM
Copy the builded RPM (`geode-ambari-plugin-phd30-1.1-2.noarch.rpm`) to your Ambari server and run
```
sudo yum -y ./geode-ambari-plugin-phd30-1.1-2.noarch.rpm.rpm
```
Restart the Ambari Server
```
sudo /etc/init.d/ambari-server restart
```
#### Use the plugin to deploy Geode cluster via Ambari
1. Login to Ambari server
2. Open the `Services` view and click on `Actions`/`+Add Services` button.
3. Select the `Geode` service from the list and press `Next`.
4. Select a host for the Geode Locator component and press `Next`.
5. Select hosts for the Goede Server components. You can not collocate Geode Locator with Geode Servers!
6. Press `Next`.
7. Open the geode-site.xml configuration panel. By default the plugin will check if the `geode.installation.file.path` points to a valid Geode tarball. If the tarball is not available the plugin will use `geode.installation.file.download.url` to download it. By default plugin will use this URL to download the Geode tarball: https://dl.dropboxusercontent.com/u/79241625/apache-geode-1.0.0-incubating-SNAPSHOT.tar.gz tarball. You can change the download URL or provide a Geode tarball locally by setting the `geode.installation.file.path`. Note that the local tarball must be provided to all servers and locators at the same path location.
8. Press `Next` to finish the deployment. 



