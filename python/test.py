import unittest
from rfwifi import buildroute, RFWIFI, ReaderType


class TestRFWIFI(unittest.TestCase):
    def test_create(self):
        testurl = "https://google.com/"
        testurlnoslash = "https://google.com"
        testextension = "/extended"
        testextensionnoslash = "extended"

        testbuild = buildroute(testurl, testextension)
        testbuildnoslash = buildroute(testurlnoslash, testextensionnoslash)
        testbuildfirstslash = buildroute(testurl, testextensionnoslash)
        testbuildsecondslash = buildroute(testurlnoslash, testextension)

        self.assertEqual(testbuild, testbuildnoslash)
        self.assertEqual(testbuildfirstslash, testbuildsecondslash)
        self.assertEqual(testbuild, testbuildfirstslash)

        rfwifi = RFWIFI()        




if __name__ == '__main__':
    unittest.main()
