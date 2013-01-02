#!/usr/bin/env python2
import os
import sys
import socket
sys.path.append(os.path.abspath(os.path.split(sys.argv[0])[0])+"/lib") 

# These are our plugins:
from discoverEggInfo import discoverEggInfo
from discoverGemspec import discoverGemspec
from discoverMediawiki import discoverMediawiki
from discoverPackageJson import discoverPackageJson
from discoverTimthumb import discoverTimthumb
from discoverWordpress import discoverWordpress
from discoverWordpressPlugins import discoverWordpressPlugins

# This could all be done better
results = discoverEggInfo().results
results.extend(discoverGemspec().results)
results.extend(discoverMediawiki().results)
results.extend(discoverPackageJson().results)
results.extend(discoverTimthumb().results)
results.extend(discoverWordpress().results)
results.extend(discoverWordpressPlugins().results)

fqdn = socket.getfqdn(socket.gethostname())

for record in results:
	print "\t".join([fqdn,record['type'],record['environment'],record['package'],record['version'],record['path']])
