import os

from pelican import signals
from pelican.readers import MarkdownReader

from .markdown_metayaml.meta_yaml import MetaYamlExtension

PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
STUDENTS_PICTURE_DIR = os.path.join(PROJECT_ROOT_DIR, "content/images/students")
GENERIC_IMAGE = 'oc-logo.svg'


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
        meta = self.replace_empty_pictures_with_generic(meta)
        return super(MarkdownYAMLReader, self)._parse_metadata(meta)

    @staticmethod
    def replace_empty_pictures_with_generic(meta):
        """
        Replace non existant images of students with a generic one
        :param meta: a student meta data
        :return: modified (or not) meta data with generic picture
        """
        student_picture = os.path.join(STUDENTS_PICTURE_DIR, meta['image'][0])
        if not os.path.exists(student_picture) or meta['image'][0].strip() == '':
            print("Students picture %s doesn't exists. It will be replaced by generic image %s." %
                  (meta["image"][0], GENERIC_IMAGE))
            meta["image"] = [GENERIC_IMAGE]
        return meta


def add_reader(readers):
    for k in MarkdownYAMLReader.file_extensions:
        readers.reader_classes[k] = MarkdownYAMLReader


def register():
    signals.readers_init.connect(add_reader)
