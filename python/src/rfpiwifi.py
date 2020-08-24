import RPi.GPIO as GPIO
# At the moment of writing this I am working with an mfrc522
from mfrc522 import SimpleMFRC522

# At the moment of writing this I am working with a pi 3 due to it's included wifi capabilities

class ReaderWifi:
    def __init__(self):
        """Initialize ReaderWifi without any initial pin setup"""
        

    def initfromdict(cls, datadict):
        """Suggested method of initialization, associate pin number with names:
        SDA, SCK, MOSI, MISO, IRQ, RST"""
        
        tempdict = dict((k.lower(), v) for k,v in datadict.items())

        self.sda = datadict["sda"]
        self.sck = datadict["sck"]
        self.mosi = datadict["mosi"]
        self.miso = datadict["miso"]
        self.irq = datadict["irq"]
        self.rst = datadict["rst"]

    def initfromargs(self, sda, sck, mosi, miso, irq, rst):
        self.sda = sda
        self.sck = sck
        self.mosi = mosi
        self.miso = miso
        self.irq = irq
        self.rst = rst
    
    def initfromargs_noirq(self, sda, sck, mosi, miso, rst):
        self.sda = sda
        self.sck = sck
        self.mosi =mosi
        slef.miso = miso
        self.irq = None
        self.rst = rst
