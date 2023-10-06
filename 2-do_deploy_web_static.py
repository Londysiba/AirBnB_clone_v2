#!/usr/bin/python3

"""
Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy

Author: Londeka Dlamini
Date: 06-10-2023
"""
from fabric.api import env, run, put
from os import path


env.hosts = ['54.144.222.14', '3.85.41.204']


def do_deploy(archive_path):
    """deploys archived static content to server"""
    try:
        if not path.exists(archive_path):
            return False

        file = archive_path.split('/')[-1]
        name = file.split('.')[0]
        release_dir = f'/data/web_static/releases/{name}'
        current_dir = '/data/web_static/current'

        put(archive_path, '/tmp/')
        run(f'mkdir -p {release_dir}')
        run(f'tar -xzf /tmp/{file} -C {release_dir}')
        run(f'rm /tmp/{file}')
        run(f'mv {release_dir}/web_static/* {release_dir}/')
        run(f'rm -rf {release_dir}/web_static')
        run(f'rm -rf {current_dir}')
        run(f'ln -s {release_dir} {current_dir}')
    except Exception:
        return False

    return True
