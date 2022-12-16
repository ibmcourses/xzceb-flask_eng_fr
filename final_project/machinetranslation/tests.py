import unittest

import translator


class TestTranslator(unittest.TestCase):
    """
    Tests for translator service
    """
    def test_fr_to_en_bonjour(self):
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')

    def test_fr_to_en_hello(self):
        self.assertNotEqual(translator.french_to_english('Hello'), 'Bonjour')

    def test_fr_to_en_null(self):
        self.assertEqual(translator.french_to_english(''), '')

    def test_fr_to_en_none(self):
        self.assertEqual(translator.french_to_english(None), None)

    def test_en_to_fr_hello(self):
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')

    def test_en_to_fr_bonjour(self):
        self.assertNotEqual(translator.english_to_french('Bonjour'), 'Hello')

    def test_en_to_fr_null(self):
        self.assertEqual(translator.english_to_french(''), '')

    def test_en_to_fr_none(self):
        self.assertEqual(translator.english_to_french(None), None)


if __name__ == '__main__':
    unittest.main()
