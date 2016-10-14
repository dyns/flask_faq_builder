

from app import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Question: %r>' % (self.title)


