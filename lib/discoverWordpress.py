#!/usr/bin/python2
import os.path
import re
from discoverPackages import discoverPackages

class discoverWordpress(discoverPackages):

	locateOptions	= ""
	searchRegex		= "wp-includes/version\.php$"
	regex = re.compile('\$wp_(version)\s*=\s*\'(.+)\';')
	translation = {
		'version': 'version',
		}

	def _defaults(self):
		return {
			'type': 'wordpress',
			'environment': 'php',
			'package':	'wordpress',
			'url':	'http://wordpress.org/'
			}
