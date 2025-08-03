# ECB DOCUMENTATIONS

# Requirements: Ubuntu 20.04
# user: vrs
# password: vrs@123

Asterisk is a free and open source framework created by Sangoma for building communications applications both for small companies and for large scale use cases. Asterisk is a software based solution which turns your Old computer into a communications server that powers IP PBX systems, VoIP gateways, conference servers and other custom solutions. The solutions build by Asterisk powers call centers, carriers and government agencies worldwide.

In this blog post we’ll walk though the installation of Asterisk 18 LTS on Ubuntu 20.04 As of this writing the latest release of Asterisk is 18. Also note this is not a long term release and should not be used for production deployments that need Digium support for long years.

# Install Asterisk 18 LTS on Ubuntu 20.04

# 1. Update Ubuntu System

command: 
1. sudo apt update
2. sudo apt -y upgrade
3. [ -f /var/run/reboot-required ] && sudo reboot -f

# 2. Install Build Dependencies

After system is rebooted login and install all dependencies required to build Asterisk on Ubuntu Linux machine.

command:
1. sudo apt update
2. sudo add-apt-repository universe
3. sudo apt -y install git curl wget libnewt-dev libssl-dev libncurses5-dev subversion libsqlite3-dev build-essential libjansson-dev libxml2-dev  uuid-dev

The installation should only take few minutes if you have a decent internet connection.

# 3. Download Asterisk 18 tarball

You won’t find the latest release of Asterisk in the official system repositories. We’ll have to manually download the tarball and build the application from source.

For example, on Ubuntu 20.04, the version available in APT repositories is 16.

command: 
1. sudo apt policy asterisk

output: asterisk:
  Installed: (none)
  Candidate: 1:16.2.1~dfsg-2ubuntu1
  Version table:
     1:16.2.1~dfsg-2ubuntu1 500
        500 http://archive.ubuntu.com/ubuntu focal/universe amd64 Packages
        500 http://mirror.hetzner.de/ubuntu/packages focal/universe amd64 Packages
    
Use wget command to download archive file.

command:

```bash
1. sudo su
2. cd ~
3. wget http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-18-current.tar.gz

Extract the file with tar.
4. tar xvf asterisk-18-current.tar.gz

Run the following command to download the mp3 decoder library into the source tree.

5. cd asterisk-18*/
6. contrib/scripts/get_mp3_source.sh

Expected command execution output:
![alt text](image.png)

Ensure all dependencies are resolved:
7. sudo contrib/scripts/install_prereq install

You should get a success message at the end:
![alt text](image-1.png)

# 4. Build and Install Asterisk 18

After installation of dependencies you should be ready to build Asterisk 18 from the source we downloaded.

Run the configure script to satisfy build dependencies.

command: 
1. ./configure

A success should have an output like below:
![alt text](<Screenshot from 2025-08-03 20-14-13.png>)

Setup menu options by running the following.

2. make menuselect

Use arrow keys to navigate, and Enter key to select.

Select Addons to enable.

<img decoding="async" src="https://computingforgeeks.com/wp-content/uploads/2018/08/install-asterisk-ubuntu-18.04-01-min.png" alt="install asterisk ubuntu 18.04 01 min" title="Install Asterisk 18 LTS on Ubuntu 22.04|20.04|18.04 1">