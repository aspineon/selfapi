from . import db, api
from flask.ext.restful import reqparse, Resource
from flask import jsonify, request
from datetime import datetime
import json
from bson import json_util
from bson.objectid import ObjectId

parser = reqparse.RequestParser()
parser.add_argument('diet', type=str)

def toJson(data):
    return json.dumps(data, default=json_util.default)

class Diet(Resource):
    def get(self):
        collection = db.diet
        entries = collection.DietEntry.find()
        json_entries = []
        for entry in entries:
            json_entries.append(entry)
        return toJson(json_entries)

    def post(self):
        args = parser.parse_args()
        collection = db.diet
        entry = collection.DietEntry()
        entry.title = request.form['title']
        entry.value = int(request.form['value'])
        entry.created_at = datetime.now()
        if request.form['timestamp']:
            entry.timestamp = datetime.strptime(request.form['timestamp'], '%Y-%m-%d %H:%M')
        entry.save()
        return {'status': 'success'}, 202

api.add_resource(Diet, '/api/diet')