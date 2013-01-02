#!/usr/bin/python2
import os.path
import re
from discoverPackages import discoverPackages

class discoverWordpressPlugins(discoverPackages):

	locateOptions	= ""
	searchRegex		= "wp-content/plugins/.*\.php$"
	regex = re.compile('\n(Version|Plugin Name|Plugin URI): ([0-9a-zA-Z][ -~]+)')
	translation = {
		'Version': 'version',
		'Plugin Name': 'package',
		'Plugin URI': 'url',
		}

	def _defaults(self):
		return {
			'type': 'wordpress-plugin',
			'environment': 'php',
			}
