#!usr/bin/python
from setuptools import setup , find_packages
setup (
	name = 'CliApp',
	version = '0.10',
	packages = find_packages(), # list of all packages
	test_suite="tests", # where to find tests
	entry_points = {
		'console_scripts': [
			'convert = convert.__main__:main', # go to module convert.__main__ and run the method called main
			'app2 = app2.__main__:main'
			]
		}
	)
