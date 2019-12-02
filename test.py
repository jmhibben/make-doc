import unittest
import tests
import logging as log

def main():
    log.basicConfig(
            format='%(levelname)s %(asctime)s %(name)s: %(message)s',
            datefmt='%y/%m/%d %H:%M:%S%p',
            level=log.DEBUG
            )
    logger = log.getLogger(__name__)
    unittest.main(module='tests', verbosity=2)

if __name__ == '__main__':
    main()
