from . import db


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(280))
    tag = db.Column(db.String(15))
    date = db.Column(db.String(10))
