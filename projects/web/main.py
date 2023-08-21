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

os.chdir
sys.path.append(root)

import yaml
import libs.tools as tools
from libs.school import *
from flask import Flask, Blueprint, render_template, request

site = Blueprint('PCA', __name__, template_folder='templates')
app = Flask(__name__)

lastSchoolUpdated = None
school = None
def getSchool():
  global school, lastSchoolUpdated
  path = tools.GetAncestorPath("data/school.yaml")
  last = os.path.getmtime(path)
  if not lastSchoolUpdated or lastSchoolUpdated != last:
    school = School(path)
    lastSchoolUpdated = last
  return school



@app.route('/')
def hello():
  school = getSchool()
  return render_template('main.html', school=school)


@app.route('/info')
def info():
  return f'''
<pre>
PATH: {os.path.abspath('.')}
</pre>
'''


@app.route('/yaml')
def _yaml():
  school = getSchool()
  return render_template('yaml.html', school=school)
  return f'''
<pre>
PATH: {os.path.abspath('.')}
</pre>
'''


@app.route('/subjects')
def _subjects():
  school = getSchool()
  return render_template('subjects.html', school=school)


@app.route('/subjects/<id>')
def _subject(id):
  school = getSchool()
  subject = school[id]
  if not subject:
    return render_template('error.html', message=f"Item '{id}' not found.")
  if not isinstance(subject, Subject):
    return render_template('error.html', message=f"Item '{id}' is not a Subject, but rather a '{type(subject)}'.")
  return render_template('subject.html', subject=subject)


@app.route('/courses/<id>')
def _course(id):
  school = getSchool()
  course = school[id]
  if not course:
    return render_template('error.html', message=f"Item '{id}' not found.")
  if not isinstance(course, Course):
    return render_template('error.html', message=f"Item '{id}' is not a Course, but rather a '{type(course)}'.")
  return render_template('course.html', course=course)


@app.route('/assignments/<id>')
def _assignment(id):
  school = getSchool()
  assignment = school[id]
  if not assignment:
    return render_template('error.html', message=f"Item '{id}' not found.")
  if not isinstance(assignment, Assignment):
    return render_template('error.html', message=f"Item '{id}' is not a Assignment, but rather a '{type(assignment)}'.")
  return render_template('assignment.html', assignment=assignment, Markdown=Markdown)


if __name__ == "__main__":
  app.run()