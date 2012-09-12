# coding: utf-8

from distutils.core import setup

# python setup.py sdist --formats=bztar
# python setup.py sdist --formats=bztar upload

description = 'National characters transcription module.'

import trans
long_description = open('README.rst', 'rb').read()
version = trans.__version__


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
