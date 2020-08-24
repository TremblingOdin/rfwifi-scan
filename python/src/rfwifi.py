from enum import Enum
import requests
import validators
from .rfpi import ReaderPI


def pyreader():
    rfreader = ReaderPI()
    return rfreader

readerswitch = {
    ReaderType.PI: pireader,
    ReaderType.ARDUINO: ardreader,
    ReaderType.OTHER: othreader,
    ReaderType.NEITHER: neireader
}



class ReaderType(Enum):
    PYTHON = 1
    ARDUINO = 2
    OTHER = 3
    NEITHER = 4



class RFWIFI:


    def __init__(self, targeturl, readertype):
        """Attempts to initialize the targeturl and creates a reader pased on the passed in enum"""
        load_readertype(readertype)
        load_url(targeturl)
        
        
        
    def load_readertype(self, readertype):
        """Checks if the passed in reader type is the right variable and assigns it then initalizes a reader"""
        if not isinstance(readertype, ReaderType):
            self.readertype = ReaderType.NEITHER
        else:
            self.readertype = readertype
            return False
        
        
        return True

    

    def load_targeturl(self, targeturl):
        """checks if the passed in url is valid and assigns it"""
        valid = validators.url(targeturl)
        if valid:
            self.targeturl = targeturl
            return True
        else:
            self.targeturl = None
            return False

    def check_properlysetup(self):
        """checks if the necessary aspects of the class are initialized"""
        if self.readertype is None or self.readertype is ReaderType.NEITHER or self.targeturl is None:
            return False
        else:
            return True
