# coding: utf-8

import selfapi
import unittest
import requests
import json
from selfapi import models
from datetime import datetime

class DietAPIFT(unittest.TestCase):

    def setUp(self):
        selfapi.app.config['TESTING'] = True
        self.app = selfapi.app.test_client()


    def tearDown(self):
        yield

    def test_get_diet_entries_should_return_200(self):
        response = requests.get('http://localhost:5000/api/diet')

        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)


    def test_post_entry_should_return_200(self):
        entry = models.DietEntry()
        entry.timestamp = u'2014-10-10 10:00'
        entry.title = u'Frühstück'
        entry.value = 700

        response = requests.post('http://localhost:5000/api/diet', data=entry)

        self.assertEqual(response.status_code, 202)


if __name__ == '__main__':
    unittest.main()
