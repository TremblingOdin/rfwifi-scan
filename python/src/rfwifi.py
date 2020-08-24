from enum import Enum
import requests

class ReaderType(Enum):
    PYTHON = 1
    ARDUINO = 2
    OTHER = 3

class RFWIFI:
    def __init__(self, targeturl, readertype):
        """Attempts to initialize the targeturl and creates a reader pased on the passed in enum"""
        
