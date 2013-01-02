#!/usr/bin/python2
import os.path
import re

class discoverPackages:

	results	= {}
	locateOptions	= ""
	searchRegex	= ""
	regex	= None
	translation	= {}
	packageInfo	= {}

	def __init__(self):
		results = map(self._readFile, self._findFiles())
		self.results = filter(lambda x: 'version' in x, results)

	def _findFiles(self):
		"""returns an array of files based on locateOptions and searchRegex

		Note, there are a million ways to do this. Current code based on a shell hack

		TODO:  Add error handling
		"""

		commandLine = "locate "+self.locateOptions+" --regexp='"+self.searchRegex+"'"
		lines = os.popen(commandLine).read().split('\n')
		return filter(lambda x: os.path.exists(x), lines)

	def _readFile(self,path):
		"""Returns parsed version data for the discovered files

		It's a tactical decision right now to use regex vs. intelligent parser.

		TODO:  Add error handling
		"""
		result = self._defaults()
		result['path'] = path
		data = open(path,'r').read()
		tempResult = self.regex.findall(data)

		for key, value in tempResult:
			result[self.translation[key]] = value

		return result

