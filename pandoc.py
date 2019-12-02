'''
File: `make-story.py`
Author: James Hibben <jmhibben@gmail.com>
License: MIT
'''

from glob import glob
from os.path import isfile
import subprocess
import logging

log = logging.getLogger(__name__)

class PandocWrapper(object):

    def __init__(self, options):
        self.__options = options
        self.__optslist = []

    '''Get the names of all files in the folder, and make sure they're only files'''
    def scan(self, loc='.', ext='.md'):
        self.files = [f for f in glob(loc + '/*' + ext) if self.verify(f)]
        return self.files

    def verify(self, name):
        return isfile(name)

    def convert(self, options=None):
        opts = options
        if opts == None:
            opts = self.__options
        if self.__optslist == []:
            self.__build_opts_list(opts)
        completed = subprocess.run(self.__optslist, stdout=subprocess.PIPE)
        return completed

    def __build_opts_list(self, options):
        keys = options.keys()
        optslist = []

        try:
            # build the basic options list for required options
            optslist.append('pandoc')
            optslist.append('-f')
            optslist.append(options['from'])
            optslist.append(' '.join(options['files']))
            optslist.append('-t')
            optslist.append(options['to'])

            if 'standalone' in keys:
                optslist.append('--standalone')

            optslist.append('-o')
            optslist.append(options['outfile'])

            if 'refdoc' in keys:
                optslist.append('--reference-doc=' + options['refdoc'])
        except KeyError as ke:
            log.error('Unable to find one or more required keys from the meta document')
            log.error(ke)

        self.__optslist = optslist
