# -*- coding: utf-8 -*-

from distutils.core import setup
import sys
import trans

# python setup.py sdist --formats=bztar
# python setup.py sdist --formats=bztar upload

version = trans.__version__
if sys.version[0]=='2':
    long_description = open('README.rst', 'rb').read()
else:
    long_description = open('README.rst', 'r').read()
description = 'National characters transcription module.'


setup(
        name='trans',
        version=version,
        description=description,
        long_description=long_description,
        author='Zelenyak Aleksandr aka ZZZ',
        author_email='ZZZ.Sochi@GMail.com',
        url='https://github.com/zzzsochi/trans',
        license='BSD',
        platforms='any',

        classifiers=[
                'Development Status :: 5 - Production/Stable',
                'Intended Audience :: Developers',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Programming Language :: Python :: 2.5',
                'Programming Language :: Python :: 2.6',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3.3'
            ],

        py_modules=['trans'],
    )
