#!/usr/bin/python3

"""
a Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers

Author: Londeka Dlamini
Date: 06-10-2023
"""
from fabric.api import env, run, put, local
from datetime import datetime
from os import path


env.hosts = ['54.144.222.14', '3.85.41.204']


def do_pack():
    """Creates archive of static files into a .tgz archive"""
    tnow = datetime.utcnow()
    archive = f"web_static_{tnow.year}{tnow.month}{tnow.day}{tnow.hour}\
{tnow.minute}{tnow.second}.tgz"

    if local('mkdir -p versions').failed:
        return None
    if local(f'tar -czvf versions/{archive} web_static/*').failed:
        return None

    return f"versions/{archive}"


def do_deploy(archive_path):
    """deploys archived static content to server"""
    if not path.exists(archive_path):
        return False

    file = archive_path.split('/')[-1]
    name = file.split('.')[0]
    release_dir = f'/data/web_static/releases/{name}'
    current_dir = '/data/web_static/current'

    if put(archive_path, '/tmp/').failed:
        return False
    if run(f'mkdir -p {release_dir}').failed:
        return False
    if run(f'tar -xzf /tmp/{file} -C {release_dir}').failed:
        return False
    if run(f'rm /tmp/{file}').failed:
        return False
    if run(f'mv {release_dir}/web_static/* {release_dir}/').failed:
        return False
    if run(f'rm -rf {release_dir}/web_static').failed:
        return False
    if run(f'rm -rf {current_dir}').failed:
        return False
    if run(f'ln -s {release_dir} {current_dir}').failed:
        return False
    return True


def deploy():
    """combines do_pack and do_deploy to deploy static files to servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
