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
sys.path.insert(0, root)
# print("root", root)
# print("sys.path", sys.path)


import libs.tools as tools
from libs.school import *
from libs.exam import *
from flask import Flask, Blueprint, render_template, request, send_file, redirect, send_from_directory

from api import *

#fnStartup = tools.GetAncestorPath('startup.yaml')
#startup = tools.readYaml(fnStartup)


site = Blueprint('PCA', __name__, template_folder='templates')
app = Flask(__name__)

app.register_blueprint(get_name)

def RepoRoot():
  'Get the absolute folder path that contains the .git folder.'
  gp = tools.GetAncestorPath('.git')
  return os.path.abspath(os.path.join(gp, '..'))



@app.route('/')
def hello():
  school = getSchool()
  return render_template('main.html', school=school, FileMarkdown=FileMarkdown, title='PCA')


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
  return render_template('yaml.html', school=school, title='YAML')
  return f'''
<pre>
PATH: {os.path.abspath('.')}
</pre>
'''


@app.route('/subjects')
def _subjects():
  school = getSchool()
  return render_template('subjects.html', school=school, title='Subjects')


@app.route('/subjects/<id>')
def _subject(id):
  school = getSchool()
  subject = school[id]
  if not subject:
    return render_template('error.html', message=f"Item '{id}' not found.")
  if not isinstance(subject, Subject):
    return render_template('error.html', message=f"Item '{id}' is not a Subject, but rather a '{type(subject)}'.", title="ERROR")
  title = subject.title
  return render_template('subject.html', subject=subject, Markdown=Markdown, title=title)


@app.route('/courses/<id>')
def _course(id):
  school = getSchool()
  course = school[id]
  if not course:
    return render_template('error.html', message=f"Item '{id}' not found.")
  if not isinstance(course, Course):
    return render_template('error.html', message=f"Item '{id}' is not a Course, but rather a '{type(course)}'.", title="ERROR")
  title = course.title
  return render_template('course.html', course=course, Markdown=Markdown, title=title)


@app.route('/exams')
def _exam():
  #request.args
  return render_template('exams.html')


@app.route('/assignments/<id>')
def _assignment(id):
  school = getSchool()
  assignment = school[id]
  if not assignment:
    return render_template('error.html', message=f"Item '{id}' not found.")
  if not isinstance(assignment, Assignment):
    return render_template('error.html', message=f"Item '{id}' is not a Assignment, but rather a '{type(assignment)}'.")
  title = assignment.title
  if not isinstance(assignment, Assignment):
    return render_template('error.html', message=f"Item '{id}' is not an Assignment, but rather a '{type(assignment)}'.", title="ERROR")
  title = assignment.title
  return render_template('assignment.html', assignment=assignment, Markdown=Markdown, title=title)





@app.route('/notebooks')
def _notebooks():
  school = getSchool()
  baseUrl = school.yo['data']['notebooks']['baseUrl']
  gitUrl = school.yo['data']['notebooks']['gitUrl']
  notebooksPath = tools.GetAncestorPath('projects/notebooks')
  meta = school.yo['data']['notebooks']['meta']

  cats = []
  for notebook in meta:
    cat = notebook['cat']
    if not cat in cats:
      cats.append(cat)

  html = ''

  for cat in cats:
    html += f'<h2>{cat}</h2>'
    html += '\n<ul>\n'
    for notebook in meta:
      thisCat = notebook['cat'] or 'Other'
      if thisCat != cat: continue
      fn = notebook['id']
      url = os.path.join(baseUrl, fn) + '.ipynb'
      giturl = os.path.join(gitUrl, fn) + '.ipynb'
      description = notebook['short']

      html += f"""<li><a href="{url}">{fn.replace('.ipynb', '')}</a> &nbsp; <a href="{giturl}">GIT</a>"""
      if description:
        html += f''' - <i>{description}</i>'''
      html += "</li>\n"
    html += '</ul>'

  model = {
    "path": notebooksPath,
    "html": html
  }
  return render_template('notebooks.html', model=model, title='Notebooks')

@app.route('/notebooks/<id>')
def _notebook(id):
  '''
  @id (string) name like 'Sympy1.ipynb'
  '''
  school = getSchool()
  baseUrl = school.yo['data']['notebooks']['baseUrl']
  path = os.path.join(baseUrl, 'tree')
  return redirect(path, code=302)




@app.route('/client_example')
def _client_example():
  '''
  Example page that calls an API
  '''
  return render_template('client_example.html')




@app.route('/<path:path>')
def _default(path):
  """
  The default catch-all path. If you hit https://DOMAIN/bananasplit, and there is no explicit route for "bananasplit",
  then this route will match, and path will be "bananasplit"
  """

  try:
    school = getSchool()
    rootRepo = RepoRoot()
    webPath = os.path.join(rootRepo, 'projects', 'web')
    title = path.split('/')[-1]

    if path.lower().endswith('.md'):
      path = os.path.join(rootRepo, path)
      data = tools.readFile(path)
      return render_template('markdown.html', data=data, Markdown=Markdown, title=title)

    p = os.path.join(webPath, 'static', path)
    if os.path.exists(p):
      return send_file(p)

    p = os.path.join(webPath, 'templates', path)
    if os.path.exists(p):
      return render_template(path, title=title)

    p = os.path.join(webPath, 'templates', path + ".html")
    if os.path.exists(p):
      return render_template(path + ".html", school=school, title=title)

    dp = os.path.join(rootRepo, 'data')
    path = os.path.join(rootRepo, path)
    return render_template(f'{path}.html', school=school, title=title)
  except Exception as e:
    return render_template("error.html", message=e, title=title)



@app.route('/zips/<filename>', methods=['GET'])
def download(filename):
    downloads = os.path.join(app.root_path, 'zips')
    return send_from_directory(downloads, filename)



if __name__ == "__main__":
  app.run(host="0.0.0.0")
