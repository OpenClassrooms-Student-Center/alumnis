pelican-md-metayaml
===================

This [Pelican](https://github.com/getpelican/pelican) plugin adds a reader for Markdown files with [YAML](https://en.wikipedia.org/wiki/YAML) metadata.
As the well-known static site generator [Jekyll](https://github.com/jekyll/jekyll) uses Markdown files with YAML metadata, this eases migration from Jekyll to Pelican.
Also, YAML metadata allows for easier specification of more complex metadata, such as nested lists or dictionaries.

Dependencies
------------

(to be installed via `pip`)

* [`Markdown`](https://pypi.python.org/pypi/Markdown)
* [`PyYAML`](https://pypi.python.org/pypi/PyYAML)

Installation
------------

Clone this repo (and its submodules) into a `pelican-md-metayaml` directory inside the `plugins` directory of your Pelican project (or whatever directory you specified for plugins in Pelican's `PLUGIN_PATHS` setting) and add `'pelican-md-metayaml'` to the list of plugins (Pelican setting `PLUGINS`) of your project. Or just use it as part of [`pelican-plugins`](https://github.com/getpelican/pelican-plugins).

To make sure the submodule is included, use `git clone --recursive [repo] [path]`.
Alternatively, clone without `--recursive`, then run `git submodule update --init` to checkout the submodule.

Usage
-----

All your Markdown files (ending in `.md`, `.markdown`, `.mkd` and `.mdown`) will now be interpreted as using YAML for their metadata.

The following example shows a very simple article (only one line of text at the bottom) but with quite complex metadata (everything between the `---`):

```
---
title: Some title
author: Some person
tags:
  - tag 1
  - tag 2
date: 2014-12-25 00:00
data:
  - name: some name
    options:
       - opt 1
       - opt 2
       - opt 3
    steps:
     - Step 1
     - Step 2
     - Step 3
---

This is the only text in the article.
```
