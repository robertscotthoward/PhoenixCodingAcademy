'''
From the command line, run:
  flask --app main.py --debug run
This will start the Flask web but watch it for changes and automatically reload the site.
'''
import glob
import os
import sys
import yaml

thisFile = os.path.abspath(sys.argv[0])
thisPath = os.path.dirname(thisFile)
root = os.path.abspath(os.path.join(thisPath, os.path.relpath('..')))

sys.path.append(root)

import libs.tools as tools
from libs.school import *
from libs.exam import *
from flask import Flask, Blueprint, render_template, request, send_file

site = Blueprint('PCA', __name__, template_folder='templates')
app = Flask(__name__)


def RepoRoot():
  'Get the absolute folder path that contains the .git folder.'
  gp = tools.GetAncestorPath('.git')
  return os.path.abspath(os.path.join(gp, '..'))



@app.route('/')
def hello():
  school = getSchool()
  return render_template('main.html', school=school, FileMarkdown=FileMarkdown)


@app.route('/info')
def info():
  gp = tools.GetAncestorPath('.git')
  root = os.path.join(gp, '..')
  return f'''
<pre>
os.path.abspath('.'):         {os.path.abspath('.')}
app.instance_path:            {app.instance_path}
os.path.abspath(sys.argv[0]): {os.path.abspath(sys.argv[0])}
Repo Root:                    {os.path.abspath(root)}
.git:                         {os.path.abspath(gp)}
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
  #request.args
  return render_template('exam.html')

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
  rootRepo = RepoRoot()
  webPath = os.path.join(rootRepo, 'projects', 'web')

  if 'favicon.ico' in path:
    print()

  if path.lower().endswith('.md'):
    path = os.path.join(rootRepo, path)
    data = tools.readFile(path)
    return render_template('markdown.html', data=data, Markdown=Markdown)

  p = os.path.join(webPath, 'static', path)
  if os.path.exists(p):
    return send_file(p)
  dp = os.path.join(rootRepo, 'data')
  path = os.path.join(rootRepo, path)
  return render_template(f'{path}.html', school=school)
  #return f"""'{path}' does not exist."""


if __name__ == "__main__":
  app.run()
