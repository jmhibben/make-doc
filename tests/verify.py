import unittest
import makestory

class TestVerify(unittest.TestCase):

    def testIsFile(self):
        self.assertTrue(makestory.verify('./makestory.py'))
        self.assertFalse(makestory.verify('./bin'))

if __name__ == '__main__':
    unittest.main(verbosity=2)
