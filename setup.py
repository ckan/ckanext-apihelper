from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-apihelper',
    version=version,
    description="API Helper page for CKAN",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Nigel Babu',
    author_email='nigel@nigelb.me',
    url='http://github.com/okfn/ckanext-apihelper',
    license='AGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.apihelper'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        apihelper=ckanext.apihelper.plugin:APIHelperPluginClass
    ''',
)
