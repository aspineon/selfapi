# coding: utf-8

import selfapi
from selfapi import DietEntry, db, app
import unittest
import requests
import json
from datetime import datetime

class DietAPIAcceptanceTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/selfapi_test.db'
        client = app.test_client()

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def createDummmyEntry(self):
        entry = DietEntry(title="foo", value=400)
        db.session.add(entry)
        db.session.commit()
        return entry

    def deleteEntry(self, entry):
        db.session.delete(entry)
        db.session.commit()

    def test_get_diet_entries_should_return_200(self):
        entry = self.createDummmyEntry()

        response = requests.get('http://localhost:5000/api/diet')

        # self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)


    def test_post_entry_should_return_201(self):
        entry = DietEntry(title='Test: Frühstück', value=700, timestamp=datetime.now().strftime('%Y-%m-%d %H:%M'))
        response = requests.post('http://localhost:5000/api/diet', data=entry.__dict__)

        self.assertEqual(response.status_code, 201)
        self.assertDictContainsSubset({'status': 'created'}, response.json())
        self.assertIsNotNone(response.json()["id"])


    def test_post_invalid_entry_should_return_400(self):
        entry = {
            "title": "Invalid Entry",
            "value": "value"
        }

        response = requests.post('http://localhost:5000/api/diet', data=entry)

        self.assertEqual(response.status_code, 400)


    def test_get_single_entry_should_return_200(self):
        entry = self.createDummmyEntry()

        response = requests.get('http://localhost:5000/api/diet/{0}'.format(entry.id))
        self.assertEqual(response.status_code, 200)


    def test_delete_entry_should_return_200(self):
        entry = self.createDummmyEntry()

        response = requests.delete('http://localhost:5000/api/diet/{0}'.format(entry.id))

        self.assertEqual(response.status_code, 200)

        response = requests.get('http://localhost:5000/api/diet/{0}'.format(entry.id))
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
