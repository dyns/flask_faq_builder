
from flask import render_template, jsonify 
from app import app
from app.models import Question
from flask import request
from app import db_service as dbs

@app.route('/')
def index():
	questions = [{'title': 'Some question'}, {'title': 'More Question'}]
	return render_template('questions.html', questions=Question.query.all())

@app.route('/question', methods=['GET','POST'])
def new_question():
	if (request.method == 'GET'):
		return render_template('new_question.html', topics=dbs.topics())
	else:
		question_title = request.form['title']
		topics = []
		if 'topics' in request.form:
			topics = request.form['topics'];
		dbs.new_question_db(question_title, topics)
		return question_title

@app.route('/question/<question_id>', methods=['GET', 'POST'])
def show_question(question_id):
	q = dbs.question_for_id(question_id)
	if request.method == 'GET':
		if q:
			return render_template('question.html', question=q)
		else:
			return 'nothing'
	elif request.method == 'POST':
		# add answer to current question
		answer_content = request.form['answer-content']
		dbs.create_answer(answer_content, q)
		return answer_content

@app.route('/topics')
def get_topics():
	return jsonify( [t.json() for t in dbs.topics()] )

@app.route('/topic', methods=['GET','POST'])
def topic():
	if(request.method == 'GET'):
		return render_template('new_topic.html');
	else:
		dbs.create_topic( request.form['title'] )
		return request.form['title']



