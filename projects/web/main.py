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
import glob
from libs.school import *
from flask import Flask, Blueprint, render_template, request

site = Blueprint('PCA', __name__, template_folder='templates')
app = Flask(__name__)


@app.route('/')
def hello():
  school = getSchool()
  return render_template('main.html', school=school, FileMarkdown=FileMarkdown)


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
  return render_template('subject.html', subject=subject, Markdown=Markdown)


@app.route('/courses/<id>')
def _course(id):
  school = getSchool()
  course = school[id]
  if not course:
    return render_template('error.html', message=f"Item '{id}' not found.")
  if not isinstance(course, Course):
    return render_template('error.html', message=f"Item '{id}' is not a Course, but rather a '{type(course)}'.")
  return render_template('course.html', course=course, Markdown=Markdown)


@app.route('/exam')
def _exam():
  request.args
  return render_template('exam.html', assignment=assignment, Markdown=Markdown)

@app.route('/assignments/<id>')
def _assignment(id):
  school = getSchool()
  assignment = school[id]
  if not assignment:
    return render_template('error.html', message=f"Item '{id}' not found.")
  if not isinstance(assignment, Assignment):
    return render_template('error.html', message=f"Item '{id}' is not a Assignment, but rather a '{type(assignment)}'.")
  return render_template('assignment.html', assignment=assignment, Markdown=Markdown)

@app.route('/<path:path>')
def _default(path):
  """
  The default catch-all path. If you hit https://DOMAIN/bananasplit, and there is no explicit route for "bananasplit",
  then this route will match, and path will be "bananasplit"
  """
  school = getSchool()

  if os.path.exists(path):
    if path.startswith('data/'):
      dp = tools.GetAncestorPath('data')
      path = os.path.join(dp, '..', path)
      path = os.path.abspath(path)
    if path.lower().endswith('.md'):
      data = tools.readFile(path)
      return render_template('markdown.html', data=data, Markdown=Markdown)
    return render_template(f'{path}.html', school=school)



if __name__ == "__main__":
  app.run()