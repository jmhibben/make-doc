import json
import logging as log

log.getLogger(__name__)

class Metadata(object):
    FIELDS = [
            'author',
            'title',
            'subtitle',
            'files',
            'outfile',
            'from',
            'to',
            'refdoc'
            ]

    def __init__(self, fname, isDebug):
        self.__file = None
        self.__filename = fname
        self.__debug = isDebug
        self.__meta = None
        self.__raw = None

    @classmethod
    def read(cls, filename='meta.json', isDebug=False):
        meta = None
        meta = cls(filename, isDebug)
        meta.load()
        return meta

    def load(self):
        """Loads the meta file using data passed"""
        self.__load()
        self.__parse()

    def __load(self):
        with open(self.__filename) as f:
            self.__file = f
            self.__raw = json.load(self.__file)

    def __parse(self):
        """Parse the metadata document for important information"""
        self.__meta = {}
        keys = Metadata.FIELDS
        for k in keys:
            val = self.get_raw(k)
            if not val is None:
                self.set_meta(k, val)

    def __source(self, source=None):
        """Internal method for reliably fetching a source"""
        meta = None
    
        if source is None or source is 'meta':
            meta = self.__meta
        elif source is 'raw':
            meta = self.__raw
        else:
            log.warning('Unknown source; using meta')
            meta = self.__meta

        return meta

    def __get(self, field, source=None):
        """Internal method for fetching values from a given source"""
        meta = self.__source(source)
        val = None
        
        # Get value from source
        try:
            val = meta.get(field)
        finally:
            return val

    def __set(self, field, value, source=None):
        """Internal method for setting values to a given source"""
        meta = self.__source(source)
        meta[field] = value

    def get_meta(self, field):
        """Gets the given metadata field value; returns `None` and logs a warning if field is not found"""
        val = self.__get(field, 'meta')
        if val is None:
            log.warning('Unable to find ' + field + ' in meta document')
        return val

    def get_raw(self, field):
        """Gets the given metadata from the raw metadata object; returns 'None' and logs a warning if field is not found"""
        val = self.__get(field, 'raw')
        if val is None:
            log.warning('unable to find ' + field + ' in raw document')
        return val

    def set_meta(self, field, value):
        """Sets the value to the given field on the metadata object"""
        self.__set(field, value, 'meta')

