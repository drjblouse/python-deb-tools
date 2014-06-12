""" Module for reading package versions from server. """
#!/usr/bin/env python
import json
from subprocess import Popen, PIPE, STDOUT


def get_version_list():
    """ Read all packages with their current versions. """
    version_list = dict()
    p = Popen('./dpkg -l', shell=True, stdout=PIPE, stderr=STDOUT)
    for line in iter(p.stdout.readline, ''):
        split_line = line.split()
        if len(split_line) > 3:
            if split_line[2] != 'Version':  # ignore header row
                version_list[split_line[1]] = split_line[2]
    return version_list


def get_version_list_json():
    return json.dumps(get_version_list())
