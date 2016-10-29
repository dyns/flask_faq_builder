
from app import db
from app.models import Question
from app.models import Topic
from app.models import Answer

def new_question_db(title, topic_ids):
	topics = Topic.query.filter(Topic.id.in_(topic_ids)).all()
	q = Question(title, topics)
	db.session.add(q)
	db.session.commit()

def question_for_id(q_id):
	q = Question.query.get(q_id)
	return q

def topics():
	return Topic.query.all()

def create_topic(title):
	t = Topic(title)
	db.session.add(t)
	db.session.commit()

def create_answer(content, question):
	a = Answer(content, 'tldr')
	db.session.add(a)
	question.answers.append(a)
	db.session.commit()






