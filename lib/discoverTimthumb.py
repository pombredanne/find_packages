#!/usr/bin/python2
import os.path
import re
from discoverPackages import discoverPackages

class discoverTimthumb(discoverPackages):

	locateOptions	= "--basename"
	searchRegex	= "thumb\.php$"
	regex = re.compile('define\s+\(\'(VERSION)\',\s*\'(.+)\'\);')
	translation = {
		'VERSION': 'version',
		}

	def _defaults(self):
		return {
			'type': 'timthumb',
			'environment': 'php',
			'package':	'timthumb',
			'url':	'http://code.google.com/p/timthumb/'
			}
