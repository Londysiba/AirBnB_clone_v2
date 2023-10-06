#!/usr/bin/python3

"""
a Fabric script that generates a .tgz archive from the contents of the
web_static

Author: Londeka Dlamini
Date: 06-10-2023
"""
from fabric.api import local
from datetime import datetime


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
