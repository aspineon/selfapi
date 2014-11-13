from . import db, api, DietEntry, Profile
from flask.ext.restful import reqparse, Resource, abort, fields, marshal_with
from datetime import datetime, timedelta

def wrap_as_list(cursor):
    return [x for x in cursor]


diet_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'value': fields.Integer,
    'timestamp': fields.DateTime,
    'creation_date': fields.DateTime,
}


class DietList(Resource):

    @marshal_with(diet_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('date', type=unicode)
        args = parser.parse_args()

        if args.date:
            date = datetime.strptime(args.date, '%Y-%m-%d')
            entries = DietEntry.query.filter(DietEntry.timestamp.between(date, date + timedelta(days=1)))
        else :
            entries = DietEntry.query.all()

        if not entries:
            abort(404, message="No entries found")

        return wrap_as_list(entries)


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=unicode, required=True)
        parser.add_argument('value', type=int, required=True)
        parser.add_argument('timestamp', type=unicode)
        args = parser.parse_args()

        entry = DietEntry(title=args.title, value=args.value)

        if args.timestamp:
            entry.timestamp = datetime.strptime(args.timestamp, '%Y-%m-%d %H:%M')

        db.session.add(entry)
        db.session.commit()

        return {'status': 'created', 'id': entry.id}, 201


class Diet(Resource):
    def find(self, entry_id):
        entry = DietEntry.query.get(entry_id)
        if not entry:
            abort(404, message="Diet Entry {} doesn't exist".format(entry_id))
        return entry

    @marshal_with(diet_fields)
    def get(self, entry_id):
        return self.find(entry_id)


    def delete(self, entry_id):
        entry = self.find(entry_id)
        db.session.delete(entry)
        db.session.commit()


api.add_resource(DietList, '/api/diet')
api.add_resource(Diet, '/api/diet/<int:entry_id>')
