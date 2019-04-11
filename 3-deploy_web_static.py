#!/usr/bin/python3
"""
this module contains deploy function which creates and distributes an archive
to my web servers
"""

import os
import re
from datetime import datetime
from fabric.api import *
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['35.227.63.107', '35.243.218.35']


def deploy():
    """creates an distributes an archive to my web servers"""
    ar_path = do_pack()
    if ar_path is None:
        return False
    return do_deploy(ar_path)
