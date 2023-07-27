from weather_pkg import my_cool_test_method
import unittest


class WeatherTest(unittest.TestCase):
    def test_my_cool_test_method(self):
        result = my_cool_test_method()
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()