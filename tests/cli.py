import unittest
import subprocess

class CLITests(unittest.TestCase):
    def testBasicConvert(self):
        results = subprocess.run(['python3', 'makestory.py', 'tests/static/readme.docx'], stdout=subprocess.PIPE)
        print(results)
        self.assertEqual(results.returncode, 0)
