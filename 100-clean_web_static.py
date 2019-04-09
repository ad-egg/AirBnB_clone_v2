#!/usr/bin/python3
"""
this module contains do_clean function which deletes out-of-date archives
"""

import os
import re
from datetime import datetime
from fabric.api import *
env.hosts = ['35.227.63.107', '35.243.218.35']


def do_clean(number=0):
    if number > 2:
        filenames = []
        times = []
        local("ls -1t > versionfiles")
        with open('versionfiles') as f:
            local("fileslines = f.read()")
        for fileline in fileslines:
            if "web_static_" in fileline and fileline[-4:] == ".tgz":
                local(filenames.append(fileline))
        if len(filenames) > 2:
            for i in range(2, len(filenames) - 1):
                local("rm {}".format(filenames[i]))
                run("rm -rf /data/web_static/releases/{}".format(
                            filenames[i][:-4]))
