from setuptools import setup

setup(
	name='filtertool',
	version='0.0.1',
	entry_points={
		'console_scripts': 'filtertool = filtertool.main:filtertool_main'
	},
)
