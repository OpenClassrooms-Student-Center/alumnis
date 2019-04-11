import markdown
# import markdown_metayaml
import random
import unittest
import codecs
import time
from codecs import BOM_UTF8, BOM_UTF16_BE, BOM_UTF16_LE, BOM_UTF32_BE, BOM_UTF32_LE
from full_yaml_metadata import FullYamlMetadataExtension
import os

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
        """Helper method to check if instance type is correct in meta"""
        try:
            self.assertIsInstance(meta[metaname], clsList, msg="{} in {} aren't a {}".format(metaname, filename, clsList))
        except KeyError:
            self.assertTrue(False, msg="{} in {} aren't defined and must be".format(metaname, filename))

    def meta_check_equal(self, filename, meta, metaname, value):
        """Helper method to check if value is correct in meta"""
        self.assertEqual(meta[metaname], value, msg="{} in {} aren't equal to {}".format(metaname, filename, value))

    def student_file(self, md_file):
        """Test a student file by checking if corresponding to attempt"""
        student_file_name = md_file[:-3]
        md = markdown.Markdown(extensions=[FullYamlMetadataExtension()])
        filename = "./content/students/" + md_file
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
        self.assertTrue(len(meta["short_description"]) <= 100, msg="Short description project must be lower than or equal to 100 characters in {}".format(filename))
        self.meta_check_instance_type(filename, meta, "template", str)
        self.meta_check_equal(filename, meta, "template", "students")

        self.meta_check_instance_type(filename, meta, "description", (str, type(None)))
        self.assertTrue(len(meta["description"]) <= 500, msg="Description project must be lower than or equal to 500 characters in {}".format(filename))

        self.meta_check_instance_type(filename, meta, "image", (str, type(None)))
        try:
            self.meta_check_equal(filename, meta, "image", "{}.jpg".format(student_file_name))
        except:
            try:
                self.meta_check_equal(filename, meta, "image", "{}.jpeg".format(student_file_name))
            except: 
                self.meta_check_equal(filename, meta, "image", "{}.png".format(student_file_name))
        imagename = "./content/images/students/" + meta["image"]
        self.assertTrue(os.path.isfile(imagename), msg="Image given in {} not exist in folder ./contents/images/students".format(filename))
            
        self.meta_check_instance_type(filename, meta, "public", bool)
        self.meta_check_equal(filename, meta, "public", True)

        self.meta_check_instance_type(filename, meta, "projects", list)
        projects = meta["projects"]
        self.assertTrue(len(projects) >= 3, msg="not enough project in {} (must be greater or equal than 3)".format(filename))

        for project in projects:
            self.meta_check_instance_type(filename, project, "title", str)
            self.meta_check_instance_type(filename, project, "description", str)
            self.assertTrue(len(project["description"]) <= 100, msg="Description project must be lower than or equal to 100 characters (project {} in {})".format(project["title"], filename))
            self.meta_check_instance_type(filename, project, "image", (str, type(None)))
            if project["image"] is not None:
                projectImage = "./content/images/students/" + project["image"]
                self.assertTrue(project["image"].startswith(student_file_name), msg="Image given in project {} in file {} not start with student file name".format(project["title"], filename))
                self.assertTrue(os.path.isfile(projectImage), msg="Image given in project {} in file {} not exist in folder ./contents/images/students/{}".format(project["title"], filename, student_file_name))
            self.meta_check_instance_type(filename, project, "link", (str, type(None)))
            self.meta_check_instance_type(filename, project, "finished", bool)
        
    def test_meta_is_ok(self):
        """Test si les meta sont bien présente sur chaque fichier"""
        files = os.listdir("content/students")
        markdowns = list(filter(lambda file: file.lower().endswith(".md"), files))
        
        # uncomment to list all wrong files
        # for md_file in sorted(markdowns):
        #     try:
        #         self.student_file(md_file)
        #     except:
        #         print(md_file)
        #         pass

        for md_file in sorted(markdowns):
            self.student_file(md_file)






# md = markdown.Markdown(extensions=["full_yaml_metadata"])
# html = md.convert(open("./gilles.md", "r").read())
# print(md.Meta)
# a = markdown.markdown(open("./gilles.md", "r").read(), exensions=["meta"])
# print(a.Meta)

unittest.main()
