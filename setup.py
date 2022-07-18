#!/usr/bin/env python
import codecs
import os
import re
from setuptools import find_packages, setup

# PROJECT SPECIFIC
NAME = 'softdeadline'
PACKAGES = find_packages(where='src')
META_PATH = os.path.join('src', 'softdeadline', '__init__.py')
CLASSIFIERS = [
    'Programming Language :: Python',
]
INSTALL_REQUIRES = ['numpy','datetime']

# END PROJECT SPECIFIC
HERE = os.path.dirname(os.path.realpath(__file__))


def read(*parts):
    with codecs.open(os.path.join(HERE, *parts), 'rb', 'utf-8') as f:
        return f.read()


def find_meta(meta, meta_file=read(META_PATH)):
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta), meta_file, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError('Unable to find __{meta}__ string.'.format(meta=meta))


if __name__ == '__main__':
    setup(
        name=NAME,
        packages=PACKAGES,
        package_dir={'': 'src'},
        include_package_data=True,
        install_requires=INSTALL_REQUIRES,
        classifiers=CLASSIFIERS,
        zip_safe=False,
        options={'bdist_wheel': {'universal': '1'}},
    )
