import unittest
from datetime import datetime

from selfapi import models


class DietEntryTest(unittest.TestCase):
    def test_should_have_required_fields(self):
        entry = models.DietEntry()
        self.assertEqual(entry.required_fields, ['timestamp', 'title', 'value'])

    def test_should_create_correct_default_values(self):
        entry = models.DietEntry()
        self.assertIsNotNone(entry.default_values['timestamp'])
        self.assertDictContainsSubset({'created_at': datetime.now().strftime('%Y-%m-%d %H:%M')}, entry.default_values)


class ProfileTest(unittest.TestCase):
    def test_should_have_required_fields(self):
        profile = models.Profile()
        self.assertEqual(profile.required_fields, ['name', 'birthday', 'height'])


if __name__ == '__main__':
    unittest.main()
