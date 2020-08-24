import RPi.GPIO as GPIO
# At the moment of writing this I am working with an mfrc522
from mfrc522 import SimpleMFRC522

# At the moment of writing this I am working with a pi 3 due to it's included wifi capabilities

class ReaderWifi:
    def __init__(self, pins):
        """Initialize ReaderWifi from pinlist, excepted input is SDA, SCK, MOSI, MISO, IRQ, RST"""
        

    @classmethod
    def fromdict(cls, datadict):
        """Suggested method of initialization, associate pin number with names:
        SDA, SCK, MOSI, MISO, IRQ, RST"""
        
        tempdict = dict((k.lower(), v) for k,v in datadict.items())

        self.sda = datadict["sda"]
        self.sck = datadict["sck"]
        self.mosi = datadict["mosi"]
        self.miso = datadict["miso"]
        self.irq = datadict["irq"]
        self.rst = datadict["rst"]


