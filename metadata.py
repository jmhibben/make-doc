import json
import logging as log

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
            val = self.__get_raw(k)
            if not val is None:
                self.__set_meta(k, val)

    def get_meta(self, field):
        """Gets the given metadata field value. Logs a warning and returns `None` when the field isn't found."""
        val = None
        try:
            val = self.__meta[field]
        except:
            log.warning('Unable to locate ' + field + ' attribute in metadata')
            log.warning('Looking for ' + field + ' in raw...')
            val = self.__get_raw(field)
        return val

    def __set_meta(self, field, value):
        """Sets the value to the given field on the meta object"""
        #self.__meta.update((field, value))
        self.__meta[field] = value

    def __get_raw(self, field):
        """Gets the data from the raw metadata file object. Returns 'None' and logs a warning when the field isn't found."""
        val = None
        try:
            val = self.__raw[field]
        except:
            log.warning('Unable to locate ' + field + ' attribute in meta file')
        return val
