#!/usr/bin/python2
import os.path
import re
from discoverPackages import discoverPackages

class discoverMediawiki(discoverPackages):

	locateOptions	= "--basename"
	searchRegex	= "DefaultSettings\.php$"
	regex = re.compile('\$wg(Version)\s*=\s*\'(.+)\';')
	translation = {
		'Version': 'version',
		}

	def _defaults(self):
		return {
			'type': 'mediawiki',
			'environment': 'php',
			'package':	'mediawiki',
			'url':	'http://mediawiki.org/'
			}
