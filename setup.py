'''
filtertool
'''
from setuptools import setup, find_packages

setup(
    name='filtertool',
    version='0.0.4',
    packages=find_packages(),
    entry_points={
        'console_scripts': 'filtertool = filtertool.main:filtertool_main'
    },
)
