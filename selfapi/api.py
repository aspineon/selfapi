from . import con, api
from flask.ext.restful import reqparse, Resource
from flask import jsonify, request

parser = reqparse.RequestParser()
parser.add_argument('diet', type=str)

class Diet(Resource):
    def get(self):
        collection = con['selfapi'].diet
        entry = collection.DietEntry.find_one()
        return jsonify(timestamp = entry.timestamp,
                   title = entry.title,
                   value = entry.value)

    def post(self):
        args = parser.parse_args()
        collection = con['selfapi'].diet
        entry = collection.DietEntry()
        entry.title = request.form['title']
        entry.value = int(request.form['value'])
        entry.save()
        return {'status': 'success'}, 202

api.add_resource(Diet, '/api/diet')