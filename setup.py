# coding: utf8

from distutils.core import setup

import trans

long_description = open('README.rst', 'r').read()

description = 'National characters transcription module.'

setup(
        name='trans',
        version=trans.__version__,
        description=description,
        long_description=long_description,
        author='Zelenyak Aleksandr aka ZZZ',
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
        ],

        py_modules=['trans'],
)
