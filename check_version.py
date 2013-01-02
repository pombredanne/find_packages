#!/usr/bin/python2
import sys
import xmlrpclib
import pprint
import requests
import json
import urllib
import re
from phpserialize import *
from distutils.version import StrictVersion

def checkEgg(record):
	result = eggClient.package_releases(record['package'])

	if len(result) > 0:
		return result[0]
	else:
		return 'unknown'

def checkJson(record):
	return 'unknown'

def to_wp_slug(strings):
	# Wordpress slugs aren't all the same - dammit!
	# Worse, I couldn't easily find the slug in the plugin files - will look deeper, but this is the current solution
	# Coming up with a good variety based on name and path info, but this doesn't account for every variation
	result = {}
	whitespace = re.compile('[ \t]')
	path = re.compile('^.+/wp-content/plugins/')
	extension = re.compile('\.php$')
	newline = re.compile('[\r\n]+') 

	for string in strings:
		string = string.lower()
		string = re.sub(newline,"",string)
		string = re.sub(path,"",string)
		string = re.sub(extension,"",string)
		string = re.sub(whitespace,"-",string)

		for key in string.split("/"):
			result[key] = 0

	return result.keys()
		
def checkWPPlugin(record):
	slugs = to_wp_slug([record['package'],record['path']])

	for slug in slugs:
		f = opener.open("http://api.wordpress.org/plugins/info/1.0/"+slug)
		string = f.read()
		parsed = loads(string, object_hook=phpobject)
		if parsed == None:
			result = 'unknown'
		else:
			result = parsed.version
			break
	return result

def checkWP(record):
	f = opener.open("http://api.wordpress.org/core/version-check/1.6/")
	parsed = loads(f.read(), object_hook=phpobject)
	print parsed["offers"][0]['current']
	return parsed["offers"][0]['current']

def checkMW(record):
	# no api, manuallys setting for now.  Write a parser
	return '1.20.1'

def checkTimthumb(record):
	# no api, manually setting for now.   Write a parser
	return '2.8.11'

def checkGem(record):
	result = requests.get("https://rubygems.org/api/v1/versions/"+record['package']+".json")

	if result.status_code == 200:
		return json.loads(result.text)[0]['number']
	else:
		return 'unknown'

def check(record):

	key = record['type']+record['package']

	if cache.has_key(key):
		record['current'] = cache[key]
	elif jump_table.has_key(record['type']):
		current = jump_table[record['type']](record)
		cache[key] = current
		record['current'] = current
	else:
		print "Unknown package type:",type

	return record

def normalize(v):
	r = []
	v = re.sub('[\sa-zA-Z]+','',v)
	for x in re.split("[._-]+",v):
		if len(x) > 0:
			r.append(int(x))
	return r

def mycmp(version1, version2):
	return cmp(normalize(version1), normalize(version2))

opener = urllib.FancyURLopener()
eggClient = xmlrpclib.ServerProxy('http://pypi.python.org/pypi')
cache = {}
jump_table = {
	'egg-info': checkEgg,
	'package.json': checkJson,
	'wordpress-plugin': checkWPPlugin,
	'wordpress': checkWP,
	'mediawiki': checkMW,
	'timthumb': checkTimthumb,
	'gemspec': checkGem,
	}

if len(sys.argv) > 1:
	f = open(sys.argv[1], 'r')
	for line in f:
		line = re.sub('[\r\n]',"",line)
		array = line.split('\t');
		record = {
			'host': array[0],
			'type': array[1],
			'environment': array[2],
			'package': array[3],
			'version': array[4],
			'path': array[5],
			}
		record = check(record);

		print "Hostname	Type	Environment	Package	Installed Version	Version Available	Install Path"
		if re.match('^[0-9._-]+$',record['current']):
			if re.match('^[0-9._-]+$',record['version']):
				if mycmp(record['current'],record['version']) == 1:
					print "\t".join([record['host'],record['type'],record['environment'],record['package'],record['version'],record['current'],record['path']])
	f.close()
else:
	print "Usage check_version.py [filename]"
	print "\nFile content should be output from find_packages.py"
	print "Output will contain latest version number if greater than the installed version number."

