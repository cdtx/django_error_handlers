import os
from setuptools import setup

def recursive(paths, rel='.'):
    l = []
    for path in paths:
        for x, y, z in os.walk(os.path.join(rel, path)):
            if z:
                l.append(os.path.relpath(os.path.join(x, '*'), rel))
    return l

setup(
    name='django_error_handlers',
    version='0.0.1',
    description='Custom views and pages for the common http errors',
    author='cdtx',
    classifiers=[
        'Programming Language :: Python :: 3.4',
    ],
    packages=['cdtx.django_error_handlers'],
    package_data={'cdtx.django_error_handlers': recursive(['templates', 'static'], rel='cdtx/django_error_handlers')},
    install_requires = []
)


