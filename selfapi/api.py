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
    'created_at': fields.DateTime,
}


class DietList(Resource):
    @marshal_with(diet_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('date', type=unicode)
        args = parser.parse_args()

        if args.date:
            print("with date")
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

        entry.created_at = datetime.now()
        if args.timestamp:
            entry.timestamp = datetime.strptime(args.timestamp, '%Y-%m-%d %H:%M')

        db.session.add(entry)
        db.session.commit()

        return {'status': 'created', 'id': entry.id}, 201


class Diet(Resource):
    @marshal_with(diet_fields)
    def get(self, entry_id):
        entry = DietEntry.query.filter_by(id=entry_id)
        if not entry:
            abort(404, message="Diet Entry {} doesn't exist".format(entry_id))
        return entry

api.add_resource(DietList, '/api/diet')
api.add_resource(Diet, '/api/diet/<string:entry_id>')
