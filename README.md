# ECB DOCUMENTATIONS

Requirements: Ubuntu 20.04
user: vrs
password: vrs@123

Asterisk is a free and open source framework created by Sangoma for building communications applications both for small companies and for large scale use cases. Asterisk is a software based solution which turns your Old computer into a communications server that powers IP PBX systems, VoIP gateways, conference servers and other custom solutions. The solutions build by Asterisk powers call centers, carriers and government agencies worldwide.

In this blog post we’ll walk though the installation of Asterisk 18 LTS on Ubuntu 20.04 As of this writing the latest release of Asterisk is 18. Also note this is not a long term release and should not be used for production deployments that need Digium support for long years.

# Install Asterisk 18 LTS on Ubuntu 20.04

# 1. Update Ubuntu System

command: 
1. sudo apt update
2. sudo apt -y upgrade
3. [ -f /var/run/reboot-required ] && sudo reboot -f

# Install Build Dependencies

After system is rebooted login and install all dependencies required to build Asterisk on Ubuntu Linux machine.

command:
1. sudo apt update
2. sudo add-apt-repository universe
3. sudo apt -y install git curl wget libnewt-dev libssl-dev libncurses5-dev subversion libsqlite3-dev build-essential libjansson-dev libxml2-dev  uuid-dev


