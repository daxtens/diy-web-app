from fabric.api import *

def setup():
    sudo("pip install bottle mongoengine bottle-cork")

def deploy():
    # create tarball
    local("tar -czf webapp.tgz webapp.py database.py" +
          " views static")
    # upload and extract
    put("webapp.tgz", "/tmp/webapp.tgz")
    with cd("/home/webapp"):
        sudo("tar -xzf /tmp/webapp.tgz")
    # clean up
    run("rm /tmp/webapp.tgz")
    # activate
    sudo("supervisorctl restart webapp")
