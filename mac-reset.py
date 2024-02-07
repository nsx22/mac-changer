#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether $(ethtool -P eth0 | awk '{print $3}')", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
subprocess.call("ifconfig eth0", shell=True)
