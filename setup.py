#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""It's the ``setup.py``; you know the drill."""
import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    """Read and return the contents of a file."""
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='cwmon-mysql',
    version='0.1.0',
    license='BSD',
    description='A cwmon plugin for monitoring MySQL.',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Hank Gay',
    author_email='hank@rescuetime.com',
    url='https://github.com/RescueTime/cwmon-mysql',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities',
    ],
    keywords=[
        'monitoring',
        'AWS',
        'CloudWatch',
        'MySQL',
    ],
    install_requires=[
        'click',
        'click-plugins',
    ],
    extras_require={
        'dev': [
            'tox',
            'twine',
            'wheel',
            'bumpversion',
            'gitchangelog',
        ],
    },
    entry_points={
        'console_scripts': [
            'cwmon-mysql = cwmon_mysql.cli:main',
        ]
    },
)
