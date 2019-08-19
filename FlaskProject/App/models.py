from App.ext import db


class Person(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    p_name = db.Column(db.String(48))