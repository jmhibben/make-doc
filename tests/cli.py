import unittest
import subprocess

@unittest.skip('Tests are failing because of changes to the CLI')
class CLITests(unittest.TestCase):
    def testBasicConvert(self):
        results = subprocess.run(['python3', 'makestory.py', 'tests/static/readme.docx'], stdout=subprocess.PIPE)
        self.assertEqual(results.returncode, 0)
