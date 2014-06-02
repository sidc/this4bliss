from fabric.api import *

# Hosts to deploy onto

# Where your project code lives on the server
env.project_root = '/home/sidc/this4bliss/web0'

def deploy_static():
    with cd(env.project_root):
        run('source ../env/bin/activate')
        run('python manage.py collectstatic -v0 --noinput')


def commit():
    local("git add -p && git commit")

def push():
    local("git push")