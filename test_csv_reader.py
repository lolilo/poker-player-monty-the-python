import unittest

from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.csv_file_name = 'test_preflop_probabilities.csv'
        self.expected_dict = {'AA': 0.73, 'AKo': 0.48, 'AKs': 0.51, 'AQs': 0.49}

    def test_get_probability_dict(self):
        self.assertEqual(self.player.get_probability_dict(self.csv_file_name), self.expected_dict)

if __name__ == '__main__':
    unittest.main()
