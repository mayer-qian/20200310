import unittest
from chapter11.city_country import print_city_country


class city_country_test(unittest.TestCase):
    def city_country(self):
        formatted_name = print_city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago,Chile')

    def city_country_population(self):
        formatted_name = print_city_country('santiago', 'chile', 50000)
        self.assertEqual(formatted_name, 'Santiago,Chile,50000')


unittest.main()
