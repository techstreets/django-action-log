from distutils.core import setup
setup(
    name='django-action-log',
    packages=['django-action-log'],
    version='0.1',
    description='Simple and small action logger for django.',
    long_description=open('README.md').read(),
    author='Bojan Radojevic',
    author_email='bradojevic@gmail.com',
    url='https://github.com/bradojevic/django-action-log',
    download_url='https://github.com/bradojevic/django-action-log/tarball/0.1',
    dependency_links=['https://github.com/bradojevic/django-action-log/tarball/0.1'],
    keywords=[
        'django',
        'logging',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
