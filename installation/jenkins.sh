#!/bin/bash
sudo apt update
sudo apt install openjdk-8-jdk
sudo wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ &gt;
/etc/apt/sources.list.d/jenkins.list'
sudo apt install jenkins -y
sudo systemctl status jenkins
