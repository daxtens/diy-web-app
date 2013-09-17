#!/bin/bash

## This file is run every time you do vagrant up. 
# It's a reasonably good place to put in set up commands.
# Every time you add another system package that your project depends on, add it to be installed here.
# Python packages are installed in fabfile.py using the "fab setup" command below.

# we're assuming that everyone is basically in Australia.
sed 's|http://us.archive.ubuntu.com/ubuntu/|http://au.archive.ubuntu.com/ubuntu/|' < /etc/apt/sources.list > /etc/apt/sources.list.new
mv /etc/apt/sources.list.new /etc/apt/sources.list

sudo apt-get update

sudo apt-get install -y fabric mongodb python-dev python-pip

cd /vagrant

fab setup

