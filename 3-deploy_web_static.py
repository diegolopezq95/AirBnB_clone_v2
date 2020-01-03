#!/usr/bin/python3
""" Fabric script that distributes an archive to the
web servers, using the function do_deploy()
"""


from fabric.api import local, put, run, env
from datetime import datetime
import os


env.hosts = ['104.196.35.117', '35.185.92.133']
env.user = "ubuntu"


def deploy():
    """
    creates and distributes an archive to web servers
    """
    new_path = do_pack()
    print(new_path)
    if not new_path:
        return False
    return do_deploy(new_path)


def do_pack():
    """
    function that generates a .tgz archive
    """
    try:
        local("mkdir -p versions")
        date = datetime.now()
        date_ = date.strftime("%Y%m%d%H%M%S")
        tar_file = "tar -cvzf versions/web_static_{}.tgz ./web_static"\
            .format(date_)
        local(tar_file)
        return ("./versions/web_static_{}.tgz".format(date_))
    except:
        return None


def do_deploy(archive_path):
    """
    distributes an archive to the web servers
    """
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        filename_tgz = archive_path.split("/")[2]
        filename = filename_tgz[:-4]
        print(filename_tgz)
        print(filename)
        run("mkdir -p /data/web_static/releases/{}".format(filename))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(filename_tgz, filename))
        run("rm /tmp/{}".format(filename_tgz))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(filename, filename))
        run("rm -rf /data/web_static/releases/{}/web_static/".format(filename))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(filename))
        return True
    except:
        return False
