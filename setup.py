import os
from setuptools import setup

README_PATH = open(
    os.path.join(os.path.dirname(__file__), 'README.rst')
)
with README_PATH as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(
    os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))
)

setup(
    name='django-action-log',
    version='0.1',
    packages=[
        'action_log',
        'action_log/migrations',
    ],
    include_package_data=True,
    license='MIT License',
    description='Simple and small action logger for django.',
    long_description=README,
    url='https://github.com/bradojevic/django-action-log',
    download_url='https://github.com/bradojevic/django-action-log/tarball/0.1',
    author='Bojan Radojevic',
    author_email='bradojevic@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
