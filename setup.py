# coding: utf8

from distutils.core import setup

import trans

# python setup.py sdist --formats=bztar
# python setup.py sdist --formats=bztar upload

version = trans.__version__
long_description = open('README.rst', 'rb').read()
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
            ],

        py_modules=['trans'],
    )
