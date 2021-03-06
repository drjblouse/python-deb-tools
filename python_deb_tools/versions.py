""" Module for managing package versions from server. """
#!/usr/bin/env python
import fileinput
import json
import sys
from subprocess import Popen, PIPE, STDOUT


def get_version_list():
    """ Read all packages with their current versions. """
    version_list = dict()
    process = Popen('dpkg -l', shell=True, stdout=PIPE, stderr=STDOUT)
    for line in iter(process.stdout.readline, ''):
        split_line = line.split()
        if len(split_line) > 3:
            if split_line[2] != 'Version':  # ignore header row
                version_list[split_line[1]] = split_line[2]
    return version_list


def get_version_list_json():
    """ Return version list as json. """
    return json.dumps(get_version_list())


def update_control_version(file_path, version):
    """ Updates the version number in a provided debian control file. """
    for line in fileinput.input(file_path, inplace=1):
        if 'Version: ' in line:
            old_ver = line.split(' ')[1]
            line = line.replace(old_ver, version) + '\n'
        sys.stdout.write(line)
