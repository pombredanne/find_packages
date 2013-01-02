# find_packages.py

This is a simple tool to discover the version of the following package types and applications, regardless where they are installed on the system:

* Python egg (pip)
* Ruby Gem
* Node.JS NPM
* Wordpress
* Wordpress plugins
* Timthumb
* Mediawiki

## Background

We can maintain system security patch levels all we want, but the above packages are often installed independently of system level packages.  Often times they are installed in arbitrary locations and often go forgotten and unpatched against security vulnerabilties.

This tool was written to find such packages and applications, and return their version.  Once the version information is gathered, it can be checked against what's currently available.

## Limitations / ToDo

Right now this is a functional proof-of-concept and will be expanded in the future.

* I wrote this application while learning python, so it's very basic and probably done very incorrectly.  :-)
* Currently this only runs on POSIX compliant systems and even then only if the "locate" command is present.  This will change in the future, so it can be more flexible for operating system and will not depend on 'locate'
* Determining wordpress slugs for plugin names is currently inconsistent - As is wordpress (grrr)
* Do not currently look up npm packages for current versions
* Need to clean check_versions.sh  a little more.

## The scripts

### find_packages.sh

This returns tab-delimtied output featuring all the packages it could find and their current version

### check_versions.sh

This script is an interim script to do version lookups until I integrate into a larger application (such as Minion).

This is where I'll be testing version lookup code before moving to a larger application.

Added caching to speed lookups.  It made a huge improvement in speed.

## Contact

Questions, comments, concerns?  Constructive feedback?  Vulcan mind-meld with python programming knowledge?

* You can assign an issue to me here
* You can contact me on irc.mozilla.org as tinfoil
* You can contact me on Freenode as neoCrimeLabs
* You can contact me on Twitter as @neoCrimeLabs
