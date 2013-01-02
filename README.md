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

This tool was written to find such packages and applications, and return their version.  Once the version is gathered, it can be checked with another tool or manually.

## Limitations

Right now this is a functional proof-of-concept and will be expanded in the future.

* Currently this only runs on POSIX compliant systems and even then only if the "locate" command is present.
* Version-checking is independent of this application.  They may be merged in the future.
* I wrote this application while learning python, so it's very basic and probably done very incorrectly.  :-)

## Contact

Questions, comments, concerns?  Constructive feedback?  Vulcan mind-meld with python programming knowledge?

* You can assign an issue to me here
* You can contact me on irc.mozilla.org as tinfoil
* You can contact me on Freenode as neoCrimeLabs
* You can contact me on Twitter as @neoCrimeLabs
