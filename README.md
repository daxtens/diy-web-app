For those reading this after CompCon 2013: 

This is a fairly comprehensive tutorial for setting up a Bottle microframework web app with a MongoDB back end and a Bootstrap front end, with nginx and supervisor.

The presentation is in the presentation directory, and all the source code is in the steps directory. If you were *not* at CompCon, you probably want the ```-web``` version. (You'll also need to follow the instructions below re: Vagrant first!)

You won't have access to a CompCon AWS instance unless you were at the workshop, but you're welcome to deploy on your own AWS instance, or your own VPS, or not at all. :) 

Enjoy and feel free to get in touch with any questions.

--- Daniel Axtens, 29/9/13


diy-web-app
===========

In a couple of hours, you'll build a full stack and (partially) buzzword compliant web app. It's the ideal platform for something too 'different' for a CMS like WordPress and too simple/small to justify using a massive framework like Django. 

By the end of the workshop, you'll have built a web application using Python, the Bottle micro framework, a MongoDB backend, the nginx web server, Amazon Web Services (AWS), and a Bootstrap front-end with some jQuery based AJAX-y fun. We'll also cover authentication (and how not to screw it up), and Google Analytics, so you can watch your app go viral. We'll learn about Fabric for simple deployment, and Vagrant for painless team development. I'll tell you about common security vulnerabilities and how to avoid them. Even better, you will be given a week's usage of an AWS micro instance to host your new app. 

I'm interested but I don't know what X is
===========================
Don't worry if any of the above terms are new to you: zero web development knowledge is assumed.

However, it is assumed that you:
* **Are familiar with procedural programming**. If you know what a function/procedure/method is, and what for loops and if statements are, and can code them in at least one language, you're probably going to be fine on this count. If you don't, googling something like "python for non-programmers" is probably a good start, or you can try something like [this](http://hetland.org/writing/instant-hacking.html).
* **Have a basic knowledge of Python**. If you are a programmer familiar with other languages, try [this](http://hetland.org/writing/instant-python.html), otherwise see the reference above.
* **Have a basic knowledge of HTTP** The difference between GET/POST and the meaning of 404/500 errors would be helpful. Anything else is a bonus. I leave this to your ability to google.
* **Knowing about git would also be helpful.** If you are familiar with version control systems, I recommend [Everyday GIT with 20 commands or so](https://www.kernel.org/pub/software/scm/git/docs/everyday.html). If you've never used a version control system before (or are going "What's a version control system?"), then you might want to start with this [introduction to version control](http://git-scm.com/book/en/Getting-Started-About-Version-Control), and read that and the next few pages. (You can skip the one on git history!) Getting your head clear on the [3 states](http://git-scm.com/book/en/Getting-Started-Git-Basics#The-Three-States) will make your life easier.

Before the talk
==========
You **must** do the following before the talk. **I will not have time to help troubleshoot your vagrant/ssh/etc issues during the talk. If you have issues, *please* contact me on [daniel@axtens.net](mailto:daniel@axtens.net) *before* the talk.**

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
