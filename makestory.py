from argparse import ArgumentParser
from pandoc import PandocWrapper
from metadata import Metadata
import logging

class CLI(object):

    @classmethod
    def init(cls, args):
        fname = args.meta
        meta = Metadata.read(fname)
        log.debug(meta)
        cli = cls(args, meta)
        cli.__add_converter()

    def __init__(self, args, meta):
        self.__args = args
        self.__meta = meta
        self.__converter = None
        self.__options = {}
    
    def __add_converter(self):
        self.__get_options()
        self.__converter = PandocWrapper(self.__options)

    def __get_options(self):
        if self.__options == {}:
            keys = self.__meta.keys()
            for key in keys:
                self.__options[key] = self.__meta[key]
        return self.__options

    def convert(self):
        options = self.__get_options()
        completed = self.__converter.convert(options)
        return completed

def main():
    logging.basicConfig(
            format='%(severity) %(asctime)s %(name)s: %(message)s',
            datefmt='%y/%m/%d %H:%M:%S%p',
            level=log.DEBUG
            )
    log = logging.getLogger(__name__)
    log.info('Starting ' + __name__)

    log.debug('Preparing argparse utility...')
    parser = ArgumentParser('Process a set of files to another filetype.')
    parser.add_argument("meta", type=str, help="The metadata file to use; must be JSON format", default="meta.json")
    log.debug('Parser ready. Parsing CLI args...')
    args = parser.parse_args()
    log.debug('Args parsed: ', args)

    log.info('Initializing converter...')
    pandoc = CLI.init(args)
    log.info('Preparing to convert files...')
    completed = pandoc.convert(args.outfile)
    log.info('Converter completed. Exit code: ' + completed.returncode)


# Only do something if the file is being run directly
if __name__ == "__main__":
    main()
