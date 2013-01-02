#!/usr/bin/python2
import os.path
import re
from discoverPackages import discoverPackages

class discoverPackageJson(discoverPackages):

	results	= {}
	locateOptions	= "--basename"
	searchRegex	= "package.json$"
	regex	= re.compile('\s*"(name|version|homepage)"\s*:\s*"(.+)"')
	translation	= {
		'name':	'package',
		'version':	'version',
		'homepage':	'url'
		}

	def _defaults(self):
		return { 
			'type': 'package.json',
			'environment': 'node.js'
			}

