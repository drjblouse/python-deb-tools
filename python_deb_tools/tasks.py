""" This file is used for build automation of the rest api service. """
from invoke import run, task


PYTHON_MANAGE = 'python manage.py '


def install_requirements():
    """ Installs all of the requirements using PIP. """
    run('sudo pip install -r requirements.pip')


@task
def clean(docs=False, bytecode=False, extra=''):
    """ Clean up old build files. """
    patterns = ['build']
    if docs:
        patterns.append('docs/_build')
    if bytecode:
        patterns.append('**/*.pyc')
    if extra:
        patterns.append(extra)
    for pattern in patterns:
        run("rm -rf %s" % pattern)


@task
def coverage():
    """ Run code coverage. """
    run("coverage run --source='./api' nosetests")
    run('coverage report')


@task
def test():
    """ Run all tests. """
    run("nosetests")


@task
def lint():
    """ Run lint check. """
    run('flake8 --ignore=E265 .')


@task
def setup():
    """ Full setup of fresh environment. """
    #install_requirements()
    clean()
    test()
    lint()
