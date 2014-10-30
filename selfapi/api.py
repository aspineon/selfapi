from . import db, api
from flask.ext.restful import reqparse, Resource, abort, fields, marshal_with
from datetime import datetime
from bson.objectid import ObjectId
from flask import request

parser = reqparse.RequestParser()


def wrap_as_list(cursor):
    return [x for x in cursor]


diet_fields = {
    '_id': fields.String,
    'title': fields.String,
    'value': fields.Integer,
    'timestamp': fields.DateTime,
    'created_at': fields.DateTime,
}


class DietList(Resource):
    @marshal_with(diet_fields)
    def get(self):
        collection = db.diet
        entries = collection.DietEntry.find()
        if not entries:
            abort(404, message="No entries found")
        return wrap_as_list(entries)

    def post(self):
        parser.add_argument('title', type=unicode, required=True)
        parser.add_argument('value', type=int, required=True)
        parser.add_argument('timestamp', type=unicode)
        args = parser.parse_args()

        collection = db.diet
        entry = collection.DietEntry()

        entry.title = args['title']
        entry.value = args['value']
        entry.created_at = datetime.now()
        if args['timestamp']:
            entry.timestamp = datetime.strptime(args['timestamp'], '%Y-%m-%d %H:%M')
        entry.save()

        return {'status': 'created', 'id': str(entry._id)}, 201


class Diet(Resource):
    @marshal_with(diet_fields)
    def get(self, entry_id):
        collection = db.diet
        entry = collection.DietEntry.find_one({"_id": ObjectId(entry_id)})
        if not entry:
            abort(404, message="Diet Entry {} doesn't exist".format(entry_id))
        return entry

api.add_resource(DietList, '/api/diet')
api.add_resource(Diet, '/api/diet/<string:entry_id>')
