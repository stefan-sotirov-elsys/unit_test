import unittest
from temperature import Temperature

class TemperatureTest(unittest.TestCase):

    temp = Temperature("https://tues2022.proxy.beeceptor.com/my/api/test")

    def test_min_temp_read(self):
        
        self.assertEqual(self.temp.min_temp_read(), 3)

    def test_max_temp_read(self):
        
        self.assertEqual(self.temp.max_temp_read(), 8)

    def test_avg_temp_read(self):
        
        self.assertEqual(self.temp.avg_temp_read(), 5)