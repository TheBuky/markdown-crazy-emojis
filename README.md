<h1 align="center">
  <br>
  <a href="https://github.com/TheBuky/markdown-crazy-emojis"><img src="https://cdn.pixabay.com/photo/2014/04/02/16/21/baby-giraffe-307016_960_720.png" alt="markdown-crazy-emojis" width="250"></a>
  <br>
  markdown-crazy-emojis
  <br>
</h1>


## Introduction
---
When can read on somes issues's project:
> Please add emojis it's good for social part.
And I want to add it too in my project, so i start to see how this others do. Thanks to [Martor](https://github.com/agusmakmun/django-markdown-editor) project for inspiration and Markdown team for his great [documentation](https://github.com/Python-Markdown/markdown/wiki/Tutorial:-Writing-Extensions-for-Python-Markdown).

The goal is to offer in customisable based to emojis in markdown. You can propose and add a new input easy to the project.

## Requierements

* Python >= 3.6.0
* Markdown >= 2.5

## Emojis avaibles

* [x]  [Github](https://gist.github.com/roachhd/1f029bd4b50b8a524f3c) (name based)
* [ ]  [Github](https://gist.github.com/rxaviers/7360908) (unicode based)
* [X]  [Webpagefx](https://www.webpagefx.com/tools/emoji-cheat-sheet/)
* [ ]  [Hexadecimal code](http://outils-javascript.aliasdmc.fr/encodage-caracteres-emoji/#comment-lire-tableau)
* [ ]  [Apple](https://emojipedia.org/apple/)
* [ ]  [Decimal code](http://outils-javascript.aliasdmc.fr/encodage-caracteres-emoji/#comment-lire-tableau)

## How it's work

The paramter `kind_emojis` is set as default on `github`. So if you want to use it, it's optionnaly.
```PYTHON
>>> import markdown
>>> from crazy_emojis import CrazyEmojis
>>> src = "This extension is amazing :open_mouth:" 
>>> html = markdown.markdown(src, extensions=[CrazyEmojis(kind_emojis='github')])
>>> print(html)

<p><img class="emoji" src="https://assets-cdn.github.com/images/icons/emoji/open_mouth.png" /></p>
```
But if you want to use an other emoji input, give the setting parameter: `kind_emojis='webpagefx'`
```PYTHON
>>> import markdown
>>> from crazy_emojis import CrazyEmojis
>>> src = "This extension is amazing :open_mouth:" 
>>> html = markdown.markdown(src, extensions=[CrazyEmojis(kind_emojis='webpagefx')])
>>> print(html)

<p><img class="emoji" alt="open_mouth" src="https://www.webpagefx.com/tools/emoji-cheat-sheet/graphics/emojis/open_mouth.png" /></p>
```
