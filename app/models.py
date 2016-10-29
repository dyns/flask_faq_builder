
from app import db

topics = db.Table('topics',
    db.Column('topic_id', db.Integer, db.ForeignKey('topic.id')),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id'))
)

class Person(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), index=True, unique=True)	

class Question(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), unique=True)
	tldr = db.Column(db.String(140))
	topics = db.relationship('Topic', secondary=topics)
	answers = db.relationship('Answer')

	def __init__(self, title, topics=[]):
		self.title = title
		self.topics = topics
		self.answers = []

	def __repr__(self):
		return '<Question: %r>' % (self.title)

	def json(self):
		topics_json = [t.json() for t in self.topics]
		answers_json = [a.json() for a in self.answers]
		data = {'id':self.id, 'title':self.title, 'topics':topics_json, 'answers':answers_json}
		return data


class Answer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(280))
	tldr = db.Column(db.String(140))
	question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

	def __init__(self, content, tldr):
		self.content = content
		self.tldr = tldr

	def __repr__(self):
		return '<Answer %s>' % (self.content)

	def json(self):
		data = {'id':self.id, 'tldr':self.tldr, 'content':self.content}
		return data

class Topic(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), index=True, unique=True)

	def __init__(self, title):
		self.title = title

	def __repr__(self):
		return '<Topic %s>' % (self.title)

	def json(self):
		data = {'id':self.id, 'title':self.title}
		return data



