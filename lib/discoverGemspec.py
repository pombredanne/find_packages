#!/usr/bin/python2
import os.path
import re
from discoverPackages import discoverPackages

class discoverGemspec(discoverPackages):

	locateOptions	= "--basename"
	searchRegex	= "\.gemspec$"
	regex = re.compile('\s+s\.(homepage|name|version)\s*=\s*"([^\n]+)"\n')
	translation = {
		'name': 'package',
		'version': 'version',
		'homepage': 'url'
		}

	def _defaults(self):
		return {
			'type': 'gemspec',
			'environment': 'ruby'
			}
