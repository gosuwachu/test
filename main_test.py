import unittest
import main

class MyTestCase(unittest.TestCase):
    def test_message(self):
        msg = "test message"
        printer = main.Printer(msg)
        self.assertEqual(printer.text, msg)


if __name__ == '__main__':
    unittest.main()
