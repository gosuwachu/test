import unittest
import main
import xmlrunner

class MyTestCase(unittest.TestCase):
    def test_message(self):
        msg = "test message"
        printer = main.Printer(msg)
        self.assertEqual(printer.text, msg)


if __name__ == '__main__':
    with open('test-results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
