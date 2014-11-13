from selfapi import db, DietEntry


def clean():
    db.drop_all()

def init():
    db.create_all()
    entry = DietEntry(title="Foobar", value=600)
    db.session.add(entry)
    db.session.commit()
