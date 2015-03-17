import unittest
import reflex

class NumgameTestCase(unittest.TestCase):
    def setUp(self):
        pass 
    
    def test_format_greater_than_minute(self):
        self.assertEqual(reflex.format(854), "1:25.4")

    def test_format_less_than_minute(self):
        self.assertEqual(reflex.format(122),"0:12.2")

    def test_for_no_seconds(self):
        self.assertEqual(reflex.format(605),"1:00.5")

    def test_for_less_than_ten_seconds(self):
        self.assertEqual(reflex.format(655),"1:05.5")


if __name__ == "__main__":
    unittest.main()
