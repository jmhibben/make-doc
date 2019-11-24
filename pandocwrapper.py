'''
File: `make-story.py`
Author: James Hibben <jmhibben@gmail.com>
License: MIT
'''

from glob import glob
from os.path import isfile
import subprocess

class PandocWrapper(object):

    def __init__(self, fromType='markdown', toType='docx'):
        self.converter = 'pandoc'
        self.refPath = '/root/.pandoc/docx/story.docx'
        self.fType = fromType
        self.tType = toType
        self.files = []

    '''Get the names of all files in the folder, and make sure they're only files'''
    def scan(self, loc='.', ext='.md'):
        self.files = [f for f in glob(loc + '/*' + ext) if self.verify(f)]
        return self.files

    def stringify(self, fromList):
        return fromList.join(' ')

    def verify(self, name):
        return isfile(name)

    def convert(self, outname):
        self.scan()
        completed = subprocess.run([self.converter, '-f', self.fType, ' '.join(self.files), '-t', self.tType, '--standalone', '-o', outname, '--reference-doc=' + self.refPath], stdout=subprocess.PIPE)
        return completed
