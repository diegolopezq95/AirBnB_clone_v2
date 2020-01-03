#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
from the contents of the web_static folder
using the function do_pack()
"""


from fabric.api import local
from datetime import datetime


def do_pack():
    """
    function that generates a .tgz archive
    """

    local("mkdir -p versions")
    date = datetime.now()
    date_ = date.strftime("%Y%m%d%H%M%S")
    tar_file = "tar -cvzf versions/web_static_{}.tgz ./web_static"\
        .format(date_)
    local(tar_file)
    return ("/versions/web_static_{}.tgz")
