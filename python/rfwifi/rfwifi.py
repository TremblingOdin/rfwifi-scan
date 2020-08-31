from enum import Enum
import requests
import validators
from .rfpi import ReaderPI



class ReaderType(Enum):
    PI = 1
    ARDUINO = 2
    OTHER = 3
    NEITHER = 4



def pireader():
    rfreader = ReaderPI()
    return rfreader



def ardreader():
    return None



def othreader():
    return None



def neireader():
    return None



readerswitch = {
    ReaderType.PI: pireader,
    ReaderType.ARDUINO: ardreader,
    ReaderType.OTHER: othreader,
    ReaderType.NEITHER: neireader
}



def buildroute(baseurl, extendedroute):
    """attempts to build and validate a possible route"""
    if extendedroute is None:
        if baseurl[-1] != "/":
            requrl = baseurl + "/"
    elif baseurl[-1] == "/" and extendedroute[0] == "/":
        requrl = baseurl + extendedroute[1:]
    elif baseurl[-1] != "/" and extendedroute[0] != "/":
        requrl = baseurl + "/" + extendedroute
    elif baseurl[-1] == "/" or extendedroute[0] == "/":
        requrl = baseurl + extendedroute

    return requrl





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
        
        self.reader = readerswitch.get(self.readertype)  
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
        if self.readertype is None or self.readertype is ReaderType.NEITHER or self.targeturl is None or self.reader is None:
            return False
        else:
            return True

    

    def readthen_get(self, processdatafunction, extendedroute):
        """Attempts to build the url, expects forward slashes
        then sends and returns a request with the built authentication tuples, and parameters
        The processdatafunction is expected to return an auth tuple and parameter in that order"""

        requrl = buildroute(self.targeturl, extendedroute)

        authtuple, payload = processdatafunction(self.reader.read())

        r = requests.get(requrl, auth=authtuple, params=payload)

        return r

    def getthen_write(self, extendedroute, get_id, authtuple, payload, processdatafunction):
        """Gets data from the url, then writes it to the rfid
        if you don't mind writing raw json fell free to ignore the process data function
        However if you want the data to be legible pass one in"""
        
        if extendedroute is not None:
            requrl = buildroute(self.targeturl, extendedroute)
            requrl = buildroute(requrl, get_id)
        else:
            requrl = buildroute(self.targeturl, get_it)

        data = requests.get(requrl, auth=authtuple, params=payload)

        if processdatafunction is not None:
            data = processdatafunction(data)

        self.reader.write(data)
