#!/usr/bin/python3

"""
clean up versions

Author: Londeka Dlamini
Date: 06-10-2023
"""
from fabric.api import local, env, run


env.hosts = ['54.144.222.14', '3.85.41.204']


def do_clean(number=0):
    """cleans up versions and keeps {number} of them"""
    num = int(number)
    versions = local('ls -1t versions', capture=True).split()
    versions = list(filter(lambda x: x.startswith('web_static_'),
                           versions))
    releases = run('ls -1t /data/web_static/releases').split()
    releases = list(filter(lambda x: x.startswith('web_static_'),
                           releases))
    if num == 0 or num == 1:
        if len(versions) > 1:
            for v in versions[1:]:
                local(f'rm -rf versions/{v}')
        if len(releases) > 1:
            for r in releases[1:]:
                run(f'rm -rf /data/web_static/releases/{r}')
    elif num > 1:
        if len(versions) > num:
            for v in versions[num:]:
                local(f'rm -rf versions/{v}')
        if len(releases) > num:
            for r in releases[num:]:
                run(f'rm -rf /data/web_static/releases/{r}')