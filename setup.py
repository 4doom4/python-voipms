#!/usr/bin/env python
import os

from setuptools import setup, find_packages


README = os.path.join(os.path.dirname(__file__), 'README.rst')

# When running tests using tox, README.md is not found
try:
    with open(README) as file:
        long_description = file.read()
except Exception:
    long_description = ''

setup(
    name='voipms',
    packages=find_packages(),  # this must be the same as the name above
    version='0.2.1',
    description='Complete REST API for the voip.ms service',
    long_description=long_description,
    author='Maximilian Ebert',
    author_email='max.ebert@me.com',
    url='https://github.com/4doom4/python-voipms',  # use the URL to the github repo
    keywords='voip.ms voips api client wrapper',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=['requests>=2.7.0'],
)
