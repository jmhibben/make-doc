import unittest
import makestory

class TestScan(unittest.TestCase):

    def testDefaults(self):
        expectedContents = ['./README.md']
        contents = makestory.scan()
        self.assertListEqual(contents, expectedContents)

    def testNamedDir(self):
        expectedContents = ['../make-story/README.md']
        contents = makestory.scan(loc='../make-story')
        self.assertListEqual(contents, expectedContents)

    def testNamedExtension(self):
        expectedContents = ['./makestory.py', './__init__.py', './test.py']
        contents = makestory.scan(ext='.py')
        self.assertListEqual(contents, expectedContents)

    def testNoExt(self):
        expectedContents = ['./makestory.py', './makestory.pyc', './bin', './README.md', './__pycache__', './__init__.py', './test.py']
        contents = makestory.scan(ext='')
        self.assertListEqual(contents, expectedContents)
