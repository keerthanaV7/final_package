import setuptools
import os

setuptools.setup(
	name = "check3",
	version="2.0",
	author="Keerthana",
	description=" final Package 3",
	classifiers = [
		"Programming Languages :: Python :: 3",
		"Operating System :: OS Independent"],
	python_requires ='>=3.6',
	install_requires=['pandas==1.1.5'],
	dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0']
	
)
