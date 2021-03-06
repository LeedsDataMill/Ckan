from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-leedsdatamilltheme',
	version=version,
	description="Leeds Data Mill Theme",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Bloom Agency',
	author_email='',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.leedsdatamilltheme'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	leedsdatamilltheme=ckanext.leedsdatamilltheme.plugin:LeedsDataMillThemePlugin
	""",
)
