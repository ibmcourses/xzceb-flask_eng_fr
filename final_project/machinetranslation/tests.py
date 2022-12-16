"""
Tests for AI Powered English/French Translator
"""
import unittest

import translator  # pylint: disable=import-error


class TestTranslator(unittest.TestCase):
    """
    Tests for translator service
    """
    def test_fr_to_en_bonjour(self):
        """
        Checks correct French to English translation of Bonjour
        """
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')

    def test_fr_to_en_hello(self):
        """
        Checks that French to English translation of Hello is not Bonjour
        """
        self.assertNotEqual(translator.french_to_english('Hello'), 'Bonjour')

    def test_fr_to_en_empty(self):
        """
        Checks correct handling of empty strings
        """
        self.assertEqual(translator.french_to_english(''), '')

    def test_fr_to_en_none(self):
        """
        Checks correct handling of None value
        """
        self.assertEqual(translator.french_to_english(None), None)

    def test_en_to_fr_hello(self):
        """
        Checks correct English to French translation of Hello
        """
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')

    def test_en_to_fr_bonjour(self):
        """
        Checks that English to French translation of Bonjour is not Hello
        """
        self.assertNotEqual(translator.english_to_french('Bonjour'), 'Hello')

    def test_en_to_fr_empty(self):
        """
        Checks correct handling of empty strings
        """
        self.assertEqual(translator.english_to_french(''), '')

    def test_en_to_fr_none(self):
        """
        Checks correct handling of None value
        """
        self.assertEqual(translator.english_to_french(None), None)


if __name__ == '__main__':
    unittest.main()
