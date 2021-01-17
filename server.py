#!/usr/bin/env python
import os
import sys
import falcon
import argparse
import configparser
import wsgiref.simple_server

import WebResources

# Testing
# Test 4

# Gather the command line arguments we need
parser = argparse.ArgumentParser(description='Specialist redirector to handle commits.kde.org permanent links')
parser.add_argument('--config', help='Path to the configuration file to work with', required=True)
parser.add_argument('--repository-metadata', help='Path to the project metadata tree', required=True)
args = parser.parse_args()

# Make sure our configuration file exists
if not os.path.exists( args.config ):
	print("Unable to locate specified configuration file: {}".format(args.config))
	sys.exit(1)

# Make sure the repository metadata tree exists too
if not os.path.exists( args.repository_metadata ):
	print("Unable to locate the repository metadata tree specified: {}".format(args.repository_metadata))
	sys.exit(1)

# Read in our configuration
configuration = configparser.ConfigParser( interpolation=configparser.ExtendedInterpolation() )
configuration.read( args.config, encoding='utf-8' )

# Setup the main application
app = falcon.API( middleware=[
])

# Setup the falcon controllers
commitRedirector = WebResources.CommitRedirector( configuration, args.repository_metadata )

# Add our various routes
app.add_sink(commitRedirector.on_get, r'/(?P<path>.*)')

# Useful for debugging problems in your API; works with pdb.set_trace(). You
# can also use Gunicorn to host your app. Gunicorn can be configured to
# auto-restart workers when it detects a code change, and it also works
# with pdb.
if __name__ == '__main__':
	# Read in the appropriate configuration
	listenOnHost = configuration.get('Webservice', 'server-host')
	listenOnPort = configuration.getint('Webservice', 'server-port')

	# Setup the webserver...
	httpd = wsgiref.simple_server.make_server( listenOnHost, listenOnPort, app)
	httpd.serve_forever()
