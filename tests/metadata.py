import unittest
from metadata import Metadata

class MetadataTests(unittest.TestCase):
    def setUp(self):
        fname = 'tests/static/meta.json'
        self.meta = Metadata.read(fname)

    def testRead(self):
        self.assertIs(type(self.meta),Metadata)

    def testClassFieldsList(self):
        expected = [
                'author',
                'title',
                'subtitle',
                'files',
                'outfile',
                'from',
                'to',
                'refdoc'
                ]
        self.assertEqual(Metadata.FIELDS, expected)

    #@unittest.skip("meta.parse not yet implemented")
    def testParse(self):
        self.assertEqual(self.meta.get_meta('author'), 'James Hibben')

    def tearDown(self):
        self.meta = None
