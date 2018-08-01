"""
# YAML Meta Data Extension for [Python-Markdown](https://github.com/waylan/Python-Markdown)

This extension adds YAML meta data handling to markdown.

As in the original, meta data is parsed but not used in processing.

(YAML meta data is used e.g. by [pandoc](http://johnmacfarlane.net/pandoc/))

Dependencies: [PyYAML](http://pyyaml.org/)


Basic Usage:

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

Make sure text without Meta Data still works (markdown < 1.6b returns a <p>).

    >>> text = '    Some Code - not extra lines of meta data.'
    >>> md = markdown.Markdown(['meta_yaml'])
    >>> print(md.convert(text))
    <pre><code>Some Code - not extra lines of meta data.
    </code></pre>
    >>> md.Meta
    {}


Copyright 2014 Bernhard Fisseni

Based on the meta data extension included with Python-Markdown,
Copyright 2007-2008 [Waylan Limberg](http://achinghead.com).

License: BSD (see LICENSE.md for details)

"""


from __future__ import absolute_import
from __future__ import unicode_literals
from markdown import Extension
from markdown.preprocessors import Preprocessor
import yaml

try:
    from yaml import CBaseLoader as Loader
except ImportError:
    from yaml import BaseLoader as Loader


# Override the default string handling function to always return unicode objects
def construct_yaml_str(self, node):
    return self.construct_scalar(node)

Loader.add_constructor(u'tag:yaml.org,2002:str', construct_yaml_str)


class MetaYamlExtension(Extension):
    """Extension for parsing YAML-Metadata with Python-Markdown."""

    def extendMarkdown(self, md, md_globals):
        """Add MetaYamlPreprocessor to Markdown instance."""

        md.preprocessors.add("meta_yaml", MetaYamlPreprocessor(md), "<meta")



class MetaYamlPreprocessor(Preprocessor):
    """
    Get Meta-Data.

    A YAML block is delimited by
    - a line '---' at the start
    - and a '...' or '---' line
    at the end.
    """

    def run(self, lines):
        """ Parse Meta-Data and store in Markdown.Meta. """

        yaml_block = []
        line = lines.pop(0)

        if line == "---":
            while lines:
                line = lines.pop(0)
                if line in ("---", "..."):
                    break
                yaml_block.append(line)

        else:
            lines.insert(0, line)

        if yaml_block:
            meta = yaml.load("\n".join(yaml_block), Loader)

            # Compat with PyMarkdown's meta: Keys are lowercase, values are lists
            meta = {k.lower(): v if isinstance(v, list) else [v] for k, v in meta.items()}

#           # this is what the code should look like, if the Markdown "meta"
#           # extension would tolerate other extensions writing to markdown.Meta
#           if hasattr(self.markdown, 'Meta'):
#               self.markdown.update(meta)
#           else:
#               self.markdown.Meta = meta

            # hacky quick fix for the moment (see above)
            if hasattr(self.markdown, 'Meta'):
                self.markdown._Meta_data = self.markdown.Meta
            else:
                self.markdown._Meta_data = {}
            self.markdown.__class__.Meta = property(lambda self: self._Meta_data, lambda self, value: self._Meta_data.update(value))
            self.markdown.Meta = meta

        return lines


def makeExtension(configs={}):
    """set up extension."""

    return MetaYamlExtension(configs=configs)
