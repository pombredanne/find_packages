#!/usr/bin/python2
import os.path
import re
from discoverPackages import discoverPackages

class discoverEggInfo(discoverPackages):

	locateOptions	= "--basename"
	searchRegex	= "\.egg-info$"
	regex = re.compile('(Name|Version|Home-page): ([^\n]+)\n')
	translation = {
		'Name': 'package',
		'Version': 'version',
		'Home-page': 'url'
		}

	def _defaults(self):
		return { 
			'type': 'egg-info',
			'environment': 'python'
			} 

	def _readFile(self,path):
		"""
		TODO:  Add error handling
		"""
		result = {
				'type':	'egg-info',
				'environment':	 'python',
				'path':	path
				}

		if os.path.isdir(path):
			fileName = path + "/PKG-INFO"
		else:
			fileName = path

		data = open(fileName,'r').read()
		tempResult = self.regex.findall(data)

		for key, value in tempResult:
			result[self.translation[key]] = value

		return result
