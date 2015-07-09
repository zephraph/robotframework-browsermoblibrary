from setuptools import setup

DESCRIPTION = """
BrowserMobLibrary is a robotfamework library that interfaces with BrowserMob
Proxy, a simple utility that makes it easy to capture performance data from
browsers.
"""

setup(name    		= 'robotframework-browsermoblibrary',
	  version		= '0.1.0',
	  description   = 'Browser performance proxy library for Robot Framework',
	  long_description = DESCRIPTION,
	  author		= 'Zephraph',
	  author_email	= 'zephraph@gmail.com',
	  url			= 'https://github.com/zephraph/robotframework-browsermoblibrary',
	  license       = 'Apache License 2.0',
	  keywords		= 'robotframework testing browsermob proxy selenium2library',
	  platforms     = 'any',
	  classifiers   = [
	    "Development Status :: 1 - Planning",
	  	"License :: OSI Approved :: Apache Software License",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
		"Topic :: Software Development :: Testing"
	  ],
	  install_requires = [
	  	'browsermob-proxy-py >= 0.7.0'
	  ],
	  packages		   = ['BrowserMobLibrary']
