
from flask import render_template 
from app import app
from app.models import Question

@app.route('/')
def index():
	questions = [{'title': 'Some question'}, {'title': 'More Question'}]
	return render_template('questions.html', questions=Question.query.all())

