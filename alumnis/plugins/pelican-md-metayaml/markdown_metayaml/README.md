# YAML Meta Data Extension for [Python-Markdown](https://github.com/waylan/Python-Markdown)

This extension adds YAML meta data handling to markdown.

As in the original, meta data is parsed but not used in processing.

(YAML meta data is used e.g. by [pandoc](http://johnmacfarlane.net/pandoc/))

Dependencies: [PyYAML](http://pyyaml.org/)

Copyright 2014 Bernhard Fisseni

Based on the meta data extension included with Python-Markdown,
Copyright 2007-2008 [Waylan Limberg](http://achinghead.com).

License: BSD (see LICENSE.md for details)


## Basic Usage

    >>> import markdown
    >>> text = '''---
    ... Title: Test Doc.
    ... Author: Waylan Limberg
    ... Blank_Data:
    ... ...
    ...
    ... The body. This is paragraph one.
    ... '''
    >>> md = markdown.Markdown(['meta_yaml'])
    >>> print(md.convert(text))
    <p>The body. This is paragraph one.</p>
    >>> print(md.Meta) # doctest: +SKIP
    {'blank_data': [''], 'author': ['Waylan Limberg'], 'title': ['Test Doc.']}



## Use in Sublime Text 3 with [OmniMarkupPreviewer](https://github.com/timonwong/OmniMarkupPreviewer)

- copy python code e.g. to `Packages/User`
- enable as extension in User Preferences

        "extensions": [
            ...
            "User.meta_yaml", // if installed in Packages/User
            ...
        ]

