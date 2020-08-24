import RPi.GPIO as GPIO
# At the moment of writing this I am working with an mfrc522
from mfrc522 import SimpleMFRC522

# At the moment of writing this I am working with a pi 3 due to it's included wifi capabilities

class ReaderWifi:
    def __init__(self):
        """Initialize ReaderWifi without any initial pin setup"""
        

    def loadpinsfrom_dict(cls, datadict):
        """Suggested method of initialization
        associate pin number with case insensitive names:
        SDA, SCK, MOSI, MISO, IRQ, RST"""

        tempdict = dict((k.lower(), v) for k,v in datadict.items())
        
        if "sda" not in tempdict or "sck" not in tempdict or "mosi" not in tempdict or "miso" not in tempdict or "rst" not in tempdict:
            return False

        self.sda = tempdict["sda"]
        self.sck = tempdict["sck"]
        self.mosi = tempdict["mosi"]
        self.miso = tempdict["miso"]
        
        if  'irq' in tempdict:
            self.irq = tempdict["irq"]
        else:
            self.irq = None
            
        self.rst = tempdict["rst"]

        return True

    def loadpinsfrom_args(self, sda, sck, mosi, miso, irq, rst):
        """Method of initialization
        Check that pins match the proper argument"""
        self.sda = sda
        self.sck = sck
        self.mosi = mosi
        self.miso = miso
        self.irq = irq
        self.rst = rst
    
    def loadpinsfrom_args_no_irq(self, sda, sck, mosi, miso, rst):
        """Method of initialization without irq included
        Check that pins match the proper argument"""
        self.sda = sda
        self.sck = sck
        self.mosi =mosi
        slef.miso = miso
        self.irq = None
        self.rst = rst
