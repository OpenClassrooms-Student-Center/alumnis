from pelican import signals
from pelican.readers import MarkdownReader

from .markdown_metayaml.meta_yaml import MetaYamlExtension

class MarkdownYAMLReader(MarkdownReader):
    """Reader for Markdown files with YAML metadata"""

    def __init__(self, *args, **kwargs):
        super(MarkdownYAMLReader, self).__init__(*args, **kwargs)
        self.settings['MARKDOWN']['extensions'].append(MetaYamlExtension())

    def _parse_metadata(self, meta):
        """Return the dict containing document metadata"""

        # MarkdownReader _parse_metadata() expects a list of length 1
        # containing a string of comma-seperated values for authors and tags
        for x in ("tags", "authors"):
            if x in meta:
                meta[x] = [",".join(meta[x])]

        return super(MarkdownYAMLReader, self)._parse_metadata(meta)

def add_reader(readers):
    for k in MarkdownYAMLReader.file_extensions:
        readers.reader_classes[k] = MarkdownYAMLReader

def register():
    signals.readers_init.connect(add_reader)
