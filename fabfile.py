from fabric.api import *

# This is a fabfile.
# It's a good place to put in things like a deploy command,
# a command to compile/minify JS/CSS assets, etc.

# We've put in a setup command, separate from bootstrap.sh, so that
# anyone who uses virtualenv rather than vagrant can install these
# packages without trampling over their system packages.
def setup():
    local("pip install bottle bottle-cork mongoengine")
