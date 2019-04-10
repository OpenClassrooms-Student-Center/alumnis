import markdown
# import markdown_metayaml
import random
import unittest
import codecs
import time
from codecs import BOM_UTF8, BOM_UTF16_BE, BOM_UTF16_LE, BOM_UTF32_BE, BOM_UTF32_LE

BOMS = (
    (BOM_UTF8, "UTF-8"),
    (BOM_UTF32_BE, "UTF-32-BE"),
    (BOM_UTF32_LE, "UTF-32-LE"),
    (BOM_UTF16_BE, "UTF-16-BE"),
    (BOM_UTF16_LE, "UTF-16-LE"),
)

def check_no_bom(data):
    a = [encoding for bom, encoding in BOMS if data.startswith(bom)]
    return not a

def isUTF8Strict(data):
    try:
        decoded = data.decode('UTF-8')
    except UnicodeDecodeError:
        return False
    else:
        for ch in decoded:
            if 0xD800 <= ord(ch) <= 0xDFFF:
                return False
        return True

# def is_utf8(filename):
#     try:
#         f = codecs.open(filename, encoding='utf-8', errors='strict')
#         for line in f:
#             pass
#         return True
#     except UnicodeDecodeError:
#         return False



class RandomTest(unittest.TestCase):
    
    """Test case utilisé pour tester les fonctions du module 'random'."""

    def meta_check_instance_type(self, filename, meta, metaname, clsList):
        self.assertIsInstance(meta[metaname], clsList, msg="{} in {} aren't a {}".format(metaname, filename, clsList))
            

    def meta_check_equal(self, filename, meta, metaname, value):
        self.assertEqual(meta[metaname], value, msg="{} in {} aren't equal to {}".format(metaname, filename, value))

    def test_meta_is_ok(self):
        """Test si les meta sont bien présente sur chaque fichier"""
        import os
        files = os.listdir("content/students")
        markdowns = filter(lambda file: file.lower().endswith(".md"), files)
        for md_file in markdowns:
            student_file_name = md_file[:-3]
            md = markdown.Markdown(extensions=["full_yaml_metadata"])
            filename = "./content/students/" + md_file
            print(filename)
            fd = open(filename, "rb")
            data = fd.read()
            fd.close()

            self.assertTrue(isUTF8Strict(data) and check_no_bom(data), msg="{} must be in UTF-8 (no BOM)".format(filename))

            fd = open(filename, "r")
            html = md.convert(fd.read())
            fd.close()

            meta = md.Meta

            self.assertIsNotNone(meta, msg="Meta isn't correctly defined in {}".format(filename))
            self.assertIsNotNone(meta["title"], msg="title in {} be present".format(filename))

            self.meta_check_instance_type(filename, meta, "title", str)
            
            self.meta_check_instance_type(filename, meta, "name", str)
            
            self.meta_check_instance_type(filename, meta, "date", str)
            self.assertIsNotNone(time.strptime(meta["date"], "%Y-%m-%d %H:%M"), msg="date in {} aren't good format".format(filename))

            
            self.meta_check_instance_type(filename, meta, "short_description", (str, type(None)))
            self.meta_check_instance_type(filename, meta, "template", str)
            self.meta_check_equal(filename, meta, "template", "students")

            self.meta_check_instance_type(filename, meta, "description", (str, type(None)))
            
            self.meta_check_instance_type(filename, meta, "image", (str, type(None)))
            self.meta_check_equal(filename, meta, "image", "{}.jpg".format(student_file_name))

            self.meta_check_instance_type(filename, meta, "public", bool)
            self.meta_check_equal(filename, meta, "public", True)

            self.meta_check_instance_type(filename, meta, "projects", list)
            projects = meta["projects"]
            self.assertTrue(len(projects) >= 3, msg="not enough project in {} (must be greater or equal than 3)".format(filename))
            for project in projects:
                self.meta_check_instance_type(filename, project, "title", str)
                self.meta_check_instance_type(filename, project, "description", (str, type(None)))
                self.meta_check_instance_type(filename, project, "image", (str, type(None)))
                self.meta_check_instance_type(filename, project, "link", (str, type(None)))
                self.meta_check_instance_type(filename, project, "finished", bool)



    # def test_choice(self):
    #     """Test le fonctionnement de la fonction 'random.choice'."""
    #     liste = list(range(10))
    #     elt = random.choice(liste)
    #     # Vérifie que 'elt' est dans 'liste'
    #     self.assertIn(elt, liste)

    # def test_choice_error(self):
    #     """Test le fonctionnement de la fonction 'random.choice'."""
    #     liste = list(range(10))
    #     elt = random.choice(liste)
    #     self.assertIn(elt, ('a', 'b', 'c'))




md = markdown.Markdown(extensions=["full_yaml_metadata"])
html = md.convert(open("./gilles.md", "r").read())
print(md.Meta)
# a = markdown.markdown(open("./gilles.md", "r").read(), extensions=["meta"])
# print(a.Meta)

unittest.main()