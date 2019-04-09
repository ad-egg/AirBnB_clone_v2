#!/usr/bin/python3
"""
this module contains do_clean function which deletes out-of-date archives
"""

import os
from fabric.api import *
env.hosts = ['35.227.63.107', '35.243.218.35']


def do_clean(number=0):
    if number > 2:
        filenames = []
        times = []
        local("ls -1t versions > versionfiles")
        with open('versionfiles') as f:
            fileslines = f.read()
        for fileline in fileslines:
            if len(fileline) == 29 and fileline[:11] == "web_static_" and \
                              fileline[-4:] == ".tgz":
                filenames.append(fileline)
        if len(filenames) > 2:
            for i in range(2, len(filenames) - 1):
                local("rm versions/{}".format(filenames[i]))
                run("rm -rf /data/web_static/releases/{}".format(
                            filenames[i][:-4]))
