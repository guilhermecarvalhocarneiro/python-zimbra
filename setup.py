#!/usr/bin/env python
import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='python-zimbra',
    version='1.0-git',
    packages=['pythonzimbra'],
    include_package_data=True,
    license='specific',
    description='Python classes to access Zimbra SOAP backend with a few utilities.',
    long_description=README,
    url='https://github.com/Zimbra-Community/python-zimbra',
    author='Dennis Ploeger',
    author_email='develop@dieploegers.de',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries'
    ],
)
