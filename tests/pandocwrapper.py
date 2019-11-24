from pandocwrapper import PandocWrapper
import unittest

class PandocWrapperTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pandoc = PandocWrapper()

    def testScan(self):
        expected = ['./README.md']
        contents = self.pandoc.scan()
        self.assertEqual(contents, expected)

    def testConvert(self):
        completed = self.pandoc.convert('./README.docx')
        self.assertEqual(completed.returncode, 0)
