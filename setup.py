# coding: utf8

import codecs
from distutils.core import setup

import trans

long_description = codecs.open('README.rst', 'r', 'utf-8').read()

description = 'National characters transcription module.'

setup(
    name='trans',
    version=trans.__version__,
    description=description,
    long_description=long_description,
    author='Zelenyak Aleksander aka ZZZ',
    author_email='zzz.sochi@gmail.com',
    url='https://github.com/zzzsochi/trans',
    license='BSD',
    platforms='any',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    py_modules=['trans'],
)
