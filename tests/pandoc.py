from pandoc import PandocWrapper
import unittest

class PandocWrapperTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pandoc = PandocWrapper({'meta': 'meta.json'})

    @unittest.skip("Shouldn't be calling scan anymore")
    def testScan(self):
        expected = ['./README.md']
        contents = self.pandoc.scan()
        self.assertEqual(contents, expected)

    def testConvert(self):
        completed = self.pandoc.convert()
        self.assertEqual(completed.returncode, 0)
