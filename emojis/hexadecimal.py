#!/usr/bin/env python

'''
markdown-crazy-emojis extension for Python-Markdown
===================================================
This list of emojis is based on http://outils-javascript.aliasdmc.fr/encodage-caracteres-emoji/

Usage
-----
    >>> import markdown
    >>> src = "This extension is amazing :open_mouth:"
    >>> html = markdown.markdown(src, ['markdown-crazy-emojis'])
    >>> print(html)
    <p><span class="emoji">&#x1F62E;</span></p>

Dependencies
------------
* [Markdown 2.0+](http://www.freewisdom.org/projects/python-markdown/)
'''

EMOJIS = {

}