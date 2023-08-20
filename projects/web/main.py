'''
From the command line, run:
  flask --app main.py --debug run
This will start the Flask web but watch it for changes and automatically reload the site.
'''
import os
import sys
thisFile = os.path.abspath(sys.argv[0])
thisPath = os.path.dirname(thisFile)
root = os.path.abspath(os.path.join(thisPath, os.path.relpath('..')))
sys.path.append(root)

import yaml
import libs.tools as tools
from libs.school import School, Subject, Course, Assignment

path = tools.GetAncestorPath("data/school.yaml")
assert(path)
school = School(path)

from flask import Flask, Blueprint, render_template, request

site = Blueprint('PCA', __name__, template_folder='templates')
app = Flask(__name__)


@app.route('/')
def hello():
  return render_template('main.html', user="Fred")


@app.route('/info')
def info():
  return f'''
<pre>
PATH: {os.path.abspath('.')}
</pre>
'''


@app.route('/school')
def _school():
  return render_template('school.html', school=school)


@app.route('/subject/<id>')
def _subject(id):
  subject = school[id]
  if not subject:
    return render_template('error.html', message=f"Item '{id}' not found.")
  if not isinstance(subject, Subject):
    return render_template('error.html', message=f"Item '{id}' is not a Subject, but rather a '{type(subject)}'.")
  return render_template('subject.html', subject=subject)


@app.route('/course/<id>')
def _course(id):
  course = school[id]
  if not course:
    return render_template('error.html', message=f"Item '{id}' not found.")
  if not isinstance(course, Course):
    return render_template('error.html', message=f"Item '{id}' is not a Course, but rather a '{type(course)}'.")
  return render_template('course.html', course=course)


@app.route('/assignment/<id>')
def _assignment(id):
  assignment = school[id]
  if not assignment:
    return render_template('error.html', message=f"Item '{id}' not found.")
  if not isinstance(assignment, Assignment):
    return render_template('error.html', message=f"Item '{id}' is not a Assignment, but rather a '{type(assignment)}'.")
  return render_template('assignment.html', assignment=assignment)


if __name__ == "__main__":
  app.run()