from fabric.api import *

# Hosts to deploy onto

# Where your project code lives on the server
env.project_root = '/home/sidc/this4bliss/web0'

def deploy_static():
    with cd(env.project_root):
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