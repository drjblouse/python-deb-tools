""" Setup file for package installation. """
#!/usr/bin/env python
import python_deb_tools
from setuptools import setup, find_packages

requires = ['invoke', 'flake8']

with open('README.md') as f:
    readme = f.read()

packages = find_packages()

setup(
    name=python_deb_tools.__name__,
    version=python_deb_tools.__version__,
    description='Python library for manipulating debian packages.',
    long_description=readme,
    author=python_deb_tools.__author__,
    author_email='jblouse@linux.com',
    url='https://github.com/drjblouse/python-deb-tools.git',
    packages=packages,
    install_requires=requires,
)