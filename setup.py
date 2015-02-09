import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

PROJECT_NAME = 'var_js'

setup(
    name='django-var-js',
    version='1.0',
    packages=[
        PROJECT_NAME,
        PROJECT_NAME+'.dj_var_js', 
        PROJECT_NAME+'.static.var_js'
    ],
    include_package_data=True,
    license='BSD License', 
    description='Application variables passed from the server to the client.',
    long_description=README,
    url='https://github.com/mapeveri/django-var-js',
    author='Peveri Martin',
    author_email='martinpeveri@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)