<h1 align="center">
  <br>
  <a href="https://github.com/TheBuky/markdown-crazy-emojis"><img src="https://cdn.pixabay.com/photo/2014/04/02/16/21/baby-giraffe-307016_960_720.png" alt="markdown-crazy-emojis" width="250"></a>
  <br>
  markdown-crazy-emojis
  <br>
</h1>


## Introduction

This project was created when I use [django-markdownx](https://github.com/neutronX/django-markdownx) for rendering my markdown on my django website. But at the difference of another projet: [Martor](https://github.com/agusmakmun/django-markdown-editor), [django-markdownx](https://github.com/neutronX/django-markdownx) doesn't contain any emoji implementation for a social part.

Thanks to the developer of [Martor](https://github.com/agusmakmun/django-markdown-editor) who inspire this projet and Markdown team for his great [documentation](https://github.com/Python-Markdown/markdown/wiki/Tutorial:-Writing-Extensions-for-Python-Markdown) about the extension.

**The goal** of this project is offered a list of defects images and you just select which kind of images you want to use on your website.

## Requierements.

* Python >= 3.6.0
* Markdown >= 2.5

_NB:_ fstring was used to formated string, so python 3.6.0 minimum.

## Emojis avaibles.

* [ ]  [Hexadecimal code](http://outils-javascript.aliasdmc.fr/encodage-caracteres-emoji/#comment-lire-tableau)
* [ ]  [Decimal code](http://outils-javascript.aliasdmc.fr/encodage-caracteres-emoji/#comment-lire-tableau)
* [x]  [Github](https://gist.github.com/roachhd/1f029bd4b50b8a524f3c) (name based)
* [ ]  [Github](https://gist.github.com/rxaviers/7360908) (unicode based)
* [X]  [Webpagefx](https://www.webpagefx.com/tools/emoji-cheat-sheet/)
* [ ]  [Samsung](https://emojipedia.org/samsung/)
* [ ]  [Google](https://emojipedia.org/google/)
* [ ]  [Facebook](https://emojipedia.org/facebook/)
* [ ]  [Messenger](https://emojipedia.org/messenger/)
* [ ]  [EmojiOne](https://emojipedia.org/emojione/)
* [ ]  [Miscrosoft](https://emojipedia.org/microsoft/)
* [ ]  [Apple](https://emojipedia.org/apple/)
* [ ]  [Mozilla](https://emojipedia.org/mozilla/)
* [ ]  [LG](https://emojipedia.org/lg/)
* [ ]  [Emojidex](https://emojipedia.org/emojidex/)
* [ ]  [Whatsapp](https://emojipedia.org/whatsapp/)

## Installation
For the moment the projet is only available on GitHub.
```BASH
git clone https://github.com/TheBuky/markdown-crazy-emojis.git
cd markdown-crazy-emojis
```

## How it's work? Just try it
Run python in the project folder and try this commandes lines to test the CrazyEmojis render _(note: I suppose markdwon is already installed)_.
```PYTHON
>>> import markdown
>>> from crazy_emojis import CrazyEmojis
>>> src = "This extension is amazing :open_mouth:" 
>>> html = markdown.markdown(src, extensions=[CrazyEmojis()])
>>> print(html)

<p><img class="emoji" src="https://assets-cdn.github.com/images/icons/emoji/open_mouth.png" /></p>
```
As default, when `kind_emojis` is empty is value is set for `github` emojis render.

But if you want to have an other emoji output, set the markdown extension setting for the kind of emojis you want: `kind_emojis='webpagefx'`
```PYTHON
>>> import markdown
>>> from crazy_emojis import CrazyEmojis
>>> src = "This extension is amazing :open_mouth:" 
>>> html = markdown.markdown(src, extensions=[CrazyEmojis(kind_emojis='webpagefx')])
>>> print(html)

<p><img class="emoji" alt="open_mouth" src="https://www.webpagefx.com/tools/emoji-cheat-sheet/graphics/emojis/open_mouth.png" /></p>
```

List of kind emojis available now:
```
github
webpagefx
```

## Implementation

> coming soon
