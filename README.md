diy-web-app
===========

Files for the "From 0 to DIY web app in 120 minutes" talk at CompCon 2013.

Stuff you **must** do before the talk is below. **I will not have time to help troubleshoot your vagrant/ssh/etc issues during the talk. If you have issues, *please* contact me on [daniel@axtens.net](mailto:daniel@axtens.net) *before* the talk.**

These instructions have been tested on a Mac. Windows users, I apologise if things are a bit fuzzy.

* Figure out how to use SSH on your platform. For anything other than windows, you should already have ```ssh``` installed. If you're on Windows, you probably want to look at [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/) or you can try installing it on Cygwin.

* Install [Vagrant][1]. You'll also need [VirtualBox][2] if you don't already have it. They're both free. Vagrant is a painless way to isolate all your development in a virtual machine, and allows everyone who works on your project to use a consistent environment.

* Clone this repository.

* ```cd``` into the repository and run ```vagrant up```.  This will work on a Linux, Mac or Windows shell.

* Patiently wait while vagrant downloads:
    * A disk image.
    * All the bits and bobs you need to develop and deploy.
    * Occasionally something will fail to download. If so, do ```vagrant halt; vagrant up``` and see if that fixes it.

* Verify that you can ```ssh``` in.
    * If you are not on Windows: ```vagrant ssh``` should work. This might also work with Cygwin.
    * If you are on windows and using PuTTY, see the [instructions provided by Vagrant][3].

* You should now be presented with a linux shell prompt identifying that you're in a Vagrant VM. 

* Exit that (Ctrl-D or logout should work) and ```vagrant halt```. You now have a disk image ready to go.

[1]: http://vagrantup.com "Vagrant"
[2]: https://www.virtualbox.org/ "VirtualBox"
[3]: http://docs-v1.vagrantup.com/v1/docs/getting-started/ssh.html "SSH"
