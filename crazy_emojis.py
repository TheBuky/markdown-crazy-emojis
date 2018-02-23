#!/usr/bin/env python

'''
markdown-crazy-emojis extension for Python-Markdown
===================================================
Find the original project on https://github.com/TheBuky/markdown-crazy-emojis

Usage
-----
    >>> import markdown
    >>> from crazy_emojis import CrazyEmojis
    >>> src = "This extension is amazing :open_mouth:" 
    >>> html = markdown.markdown(src, extensions=[CrazyEmojis()])
    >>> print(html)
    <p><img class="emoji" src="https://assets-cdn.github.com/images/icons/emoji/smile.png" /><</p>

Dependencies
------------
* [Markdown 2.0+](http://www.freewisdom.org/projects/python-markdown/)
'''

from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree, AtomicString

from emojis import *
import re


DELIMITER = ':'
EMOJI_RE = r'(:){1}(.*?):'


class GithubPattern(Pattern):
    ''' Used when 'kind_emojis' in config is github '''

    def handleMatch(self, m):
        emoji = self.unescape(m.group(3))
        
        if emoji not in github.EMOJIS.keys():
            return emoji
        
        url = f'{github.BASE_URL}{github.EMOJIS[emoji]}'
        
        el = etree.Element('img')
        el.set('src', url)
        el.set('alt', emoji)
        el.set('class', 'crazy-emoji')
        el.text = m.group(3)
        
        return el

        
class WebpagefxPattern(Pattern):
    ''' Used when 'kind_emojis' in config is webpagefx '''

    def handleMatch(self, m):
        emoji = self.unescape(m.group(3))
        
        if emoji not in webpagefx.EMOJIS.keys():
            return emoji
        
        url = f'{webpagefx.BASE_URL}{webpagefx.EMOJIS[emoji]}'
        
        el = etree.Element('img')
        el.set('src', url)
        el.set('alt', emoji)
        el.set('class', 'crazy-emoji')
        el.text = m.group(3)
        
        return el


class CrazyEmojis(Extension):

    def __init__(self, *args, **kwargs):
        self.config = {
            'kind_emojis': [ 'github', 'Select the type of emojis for your render' ],
        }
        super(CrazyEmojis, self).__init__(*args, **kwargs)
        
    def extendMarkdown(self, md, md_globals):
        if self.getConfig('kind_emojis') == 'github':
            emoji = GithubPattern(EMOJI_RE, md)
        elif self.getConfig('kind_emojis') == 'webpagefx':
            emoji = WebpagefxPattern(EMOJI_RE, md)
        else:
            emoji = md
        md.inlinePatterns['crazy-emoji'] = emoji
    
    
def makeExtension(*args, **kwargs):
    return CrazyEmojis(*args, **kwargs)