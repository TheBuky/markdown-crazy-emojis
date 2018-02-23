#!/usr/bin/env python


from setuptools import setup
 

setup(
    name = 'markdown-crazy-emojis',
    version = '1.0',
    author = 'Buky',
    author_email = 'buky77@hotmail.fr',
    description = 'Python-Markdown extension for multi rendering emoji.',
    license = 'LGPL-3.0',
    keywords = "emojis markdown",
    url = 'https://github.com/TheBuky/markdown-crazy-emojis',
    install_requires = ['markdown>=2.5'],
    classifiers = [
        'Programming Language :: Python :: 3.6',
    ]
)