import os
import sys
import glob
thisFile = os.path.abspath(sys.argv[0])
thisPath = os.path.dirname(thisFile)
root = os.path.abspath(os.path.join(thisPath, os.path.relpath('..')))
sys.path.append(root)

import markdown
import yaml
from io import StringIO
import libs.tools as tools


'''
A school is a collection of subjects, courses, and assignments all defined from a set of YAML files.
A 'value' is a string or number.
An 'item' is an object, list, or value
A 'yo' is a YAML object; i.e. a dict of key/item pairs.
A 'ya' is a YAML list; i.e. a list of items.
'''



def Markdown(md):
  '''
  Return the HTML of a markdown string.
  '''
  if not md: return ''
  try:
    html = markdown.markdown(md, extensions=[
      'pymdownx.arithmatex',
      #'mdx_math',
      'fenced_code',
      'md_mermaid',
      ])
    return html
  except Exception as e:
    print(e)
    html = markdown.markdown(md, extensions=['fenced_code'])
    return html

def FileMarkdown(relPath):
  '''
  Find a *.md file and return the HTML of it.
  '''
  path = tools.GetAncestorPath(relPath)
  if not path:
    return f"Cannot find path '{relPath}'."
  path = os.path.abspath(path)
  if not os.path.exists(path):
    return f"File '{path}' not found."
  md = tools.readFile(path)
  return Markdown(md)



def getRootYaml(path):
  '''
  @path is the path to the root yaml file; e.g. school.yaml
  All supporting yaml files in that folder are included in the root yaml.
  '''
  if not os.path.exists(path):
    raise(Exception(f"Cannot find YAML file '{path}'"))
  dataPath = os.path.dirname(path)
  yaml = tools.ReadYaml(path)
  ya = yaml['subjects']
  for index, item in enumerate(ya):
    id = item.get('id')
    fn = os.path.join(dataPath, f"{id}.yaml")
    if os.path.exists(fn):
      yo = tools.ReadYaml(fn)
      for key, value in yo.items():
        if not key in item:
          item[key] = value
      ya[index] = item
  return yaml

updated = {}
school = None

def getSchool():
  global school
  dirty = False
  data = tools.GetAncestorPath("data")
  for fp in glob.glob(os.path.join(data, '*.yaml')):
    last = os.path.getmtime(fp)
    if fp in updated:
      if updated[fp] != last:
        updated[fp] = last
        dirty = True
    else:
      updated[fp] = last
      dirty = True
  if not school or dirty:
    school = School(os.path.join(data, 'school.yaml'))
  return school


class School:
  def __init__(self, path, parent=None):
    gp = tools.GetAncestorPath('.git')
    self.repoRoot = os.path.join(gp, '..')

    self.yo = getRootYaml(os.path.abspath(path))
    self.yaml = tools.PrettifyYaml(self.yo)
    self.types = {}
    self.items = {}
    ya = self.yo.get('subjects')

    # Add items in inverse order of dependency
    def adds(ya, cls):
      if ya:
        for yo in ya:
          add(yo, cls)

    def add(yo, cls):
      id = yo['id']
      self.types[id] = cls, yo
      adds(yo.get('courses', []), Course)
      adds(yo.get('assignments', []), Assignment)

    for yo in ya:
      add(yo, Subject)

    self.subjects = Items(self, ya, Subject, self)

  def markdown(self, md):
    return Markdown(md)

  def __str__(self):
    return f"School[{len(self.subjects)}]"

  def __repr__(self):
    return f"School[{len(self.subjects)}]"

  def __getitem__(self, id):
    if not id in self.items:
      return None
    return self.items[id]


class Link:
  '''Represents a link to some site.'''
  def __init__(self, yo):
    self.short = ''
    self.description = ''
    if isinstance(yo, str):
      self.url = yo
      self.text = yo
    else:
      self.url = yo.get('url', None)
      if not self.url:
        raise(Exception(f"Missing 'url' property for {yo}"))
      self.text = yo.get('text', self.url)
      self.short = yo.get('short', '')
      self.description = yo.get('description', '')

class Item:
  '''Base class of many objects, such as Subject, Course, Assignment'''
  def __init__(self, school, yo, parent):
    self.school = school
    self.parent = parent
    self.id = yo.get('id', None)
    self.title = yo.get('title', None) or self.id
    self.description = yo.get('description', None)
    self.short = yo.get('short', '')
    self.purpose = yo.get('purpose', '')

    links = yo.get('links', [])
    self.links = []
    for link in links:
      self.links.append(Link(link))

    self.parents = set()
    parents = yo.get('parents', None)
    if parents:
      for id in parents.split(' '):
        id = id.strip()
        item = self.school[id]
        if not item:
          cls,yo = self.school.types[id]
          item = cls(self.school, yo, parent)
        self.parents.add(item)

    self.prerequisites = set()
    prerequisites = yo.get('prerequisites', None)
    if prerequisites:
      for id in prerequisites.split(' '):
        id = id.strip()
        item = self.school[id]
        if not item:
          s = f"Cannot find prerequisite '{id}' in item '{self.id}'"
          print('ERROR', s)
          raise(Exception(s))
        self.prerequisites.add(item)

  def includeLinksSection(self):
    s = ""
    if self.links:
      s = f"\n<h2>Links</h2>\n"
      s += "<ul>\n"
      for link in self.links:
        s += f"""<li><a href="{link.url}">{link.text}</a>"""
        if link.short:
          s += f""" - <i>{link.short}</i>"""
        if link.description:
          s += f"""<div style="margin-left: 10px; font-size: smaller;">{Markdown(link.description)}</div>"""
      s += "</ul>\n"
    return s

  def Breadcrumbs(self):
    s = ''
    if self.parent and not isinstance(self.parent, School):
      s = self.parent.Breadcrumbs()
      if s: s += " > "
      s += f'''<a href="/{self.parent.plural}/{self.parent.id}">{self.parent.title}</a>'''
    return s




class Items:
  '''A list of items that do not have duplicate id's.'''
  def __init__(self, school, ya, cls, parent):
    '''
    @ya = YAML array
    @cls = the class to instantiate for each item; e.g. Subject, Course, Assignment
    '''
    self.school = school
    self.parent = parent
    self.list = []
    if not ya: return
    for yo in ya:
      item = cls(school, yo, parent)
      if item in self:
        raise Exception(f"Duplicate id '{item.id}' found for Items of '{cls}'")
      self.list.append(item)
      if item.id in self.school.items:
        raise Exception(f"Duplicate id '{item.id}' found for Items of '{cls}'. Ids must be globally unique.")
      self.school.items[item.id] = item

  def __contains__(self, item):
    for x in self.list:
      if x.id == item.id: return True
    return False
  def __iter__(self):
    return iter(self.list)
  def __len__(self):
    return len(self.list)

  def Dag(self):
    html = StringIO()
    self._Dag1(html)
    html.seek(0)
    return html.read()

  def _Dag1(self, html, parent=None):
    if not self.list:
      return ''

    first = self.list[0]


    html.write('<ul>')
    children = [x for x in self if parent in x.parents or (not parent and not x.parents)]
    for item in children:
      html.write('<li>')
      type = ''
      if isinstance(first, Subject):
        type = 'subjects'
        if item.courses:
          html.write(f'''<a href="/{type}/{item.id}">{item.title}</a> (<span title="Number of courses">{len(item.courses)}</span>) <i>{item.short}</i>''')
        else:
          html.write(f'''<a href="/{type}/{item.id}">{item.title}</a> <i>{item.short}</i>''')
      elif isinstance(first, Course):
        type = 'courses'
        html.write(f'''<a href="/{type}/{item.id}">{item.title}</a> <i>{item.short}</i>''')
      elif isinstance(first, Assignment):
        type = 'assignments'
        html.write(f'''<a href="/{type}/{item.id}">{item.title}</a> <i>{item.short}</i>''')
      else:
        raise(Exception(f"Unrecognized type '{type(first)}'"))

      self._Dag1(html, item)
      html.write('</li>')

    html.write('</ul>')




class Subject(Item):
  singular = "subject"
  plural = "subjects"

  def __init__(self, school, yo, parent):
    Item.__init__(self, school, yo, parent)
    ya = yo.get('courses')
    self.courses = Items(school, ya, Course, self)

  def toFileMarkdown(self):
    md = f'''
    #{self.id}

    '''
    return md




class Course(Item):
  singular = "course"
  plural = "courses"

  def __init__(self, school, yo, parent):
    Item.__init__(self, school, yo, parent)
    ya = yo.get('assignments')
    self.assignments = Items(school, ya, Assignment, self)




class Assignment(Item):
  singular = "assignment"
  plural = "assignments"

  def __init__(self, school, yo, parent):
    Item.__init__(self, school, yo, parent)
    self.steps = yo.get('steps', '')
    self.acceptance = yo.get('acceptance', '')






def tests():
  school = getSchool()
  for subject in school.subjects:
    print("SUBJECT", subject.id)
    for course in subject.courses:
      print("  COURSE", course.id, subject)
      for assignment in course.assignments:
        print("    ASSIGNMENT", assignment.id, course)
        print(assignment.Breadcrumbs())


if __name__ == "__main__":
  tests()
