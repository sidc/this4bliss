#!/usr/bin/env python
from fabric.api import *
import os
from contextlib import contextmanager
# Hosts to deploy onto
VENV_DIR = '/home/sidc/this4bliss/env/'
env.roledefs = {
    'pro': ['sidc@this4bliss.com']
} 
env.project_root = '/home/sidc/this4bliss/web0'

# Where your project code lives on the server

@contextmanager
def source_virtualenv():
    with prefix('source ' + os.path.join(VENV_DIR, 'bin/activate')):
        yield

def deploy_static():
    with cd(env.project_root):
        with source_virtualenv():
            run("git pull")
            run('python manage.py collectstatic -v0 --noinput')
            run("touch web0.wsgi")

def prepare_deploy():
    commit()
    push()

def commit():
    local("git add -p && git commit")

def push():
    local("git push")