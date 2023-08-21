import os
import sys
thisFile = os.path.abspath(sys.argv[0])
thisPath = os.path.dirname(thisFile)
root = os.path.abspath(os.path.join(thisPath, os.path.relpath('..')))
sys.path.append(root)

import  markdown
import yaml
import libs.tools as tools


'''
A school is a collection of subjects, courses, and assignments all defined from a set of YAML files.
A 'value' is a string or number.
An 'item' is an object, list, or value
A 'yo' is a YAML object; i.e. a dict of key/item pairs.
A 'ya' is a YAML list; i.e. a list of items.
'''


class School:
  def __init__(self, path):
    self.yo = tools.ReadYaml(os.path.abspath(path))
    ya = self.yo.get('subjects')
    self.items = {}
    self.subjects = Items(self, ya, Subject)

  def __str__(self):
    return f"School[{len(self.subjects)}]"

  def __repr__(self):
    return f"School[{len(self.subjects)}]"

  def __getitem__(self, id):
    if not id in self.items:
      return None
    return self.items[id]

  def Markdown(self, relPath):
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
    html = markdown.markdown(md, extensions=['fenced_code'])
    return html




class Item:
  '''Base class of many objects, such as Subject, Course, Assignment'''
  def __init__(self, school, yo):
    self.school = school
    self.id = yo.get('id', None)
    self.title = yo.get('title', None) or self.id
    self.description = yo.get('description', None)
    self.short = yo.get('short', '')
    prerequisites = yo.get('prerequisites', None)
    if prerequisites:
      self.prerequisites = set()
      for id in prerequisites.split(' '):
        id = id.strip()
        item = self.school[id]
        if not item:
          s = f"Cannot find prerequisite '{id}' in item '{self.id}'"
          print('ERROR', s)
          raise(s)
        self.prerequisites.add(item)



class Items:
  '''A list of items that do not have duplicate id's.'''
  def __init__(self, school, ya, cls):
    '''
    @ya = YAML array
    @cls = the class to instantiate for each item; e.g. Subject, Course, Assignment
    '''
    self.school = school
    self.list = []
    if not ya: return
    for yo in ya:
      item = cls(school, yo)
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




class Subject(Item):
  def __init__(self, school, yo):
    Item.__init__(self, school, yo)
    ya = yo.get('courses')
    self.courses = Items(school, ya, Course)

  def toMarkdown(self):
    md = f'''
    #{self.id}

    '''
    return md




class Course(Item):
  def __init__(self, school, yo):
    Item.__init__(self, school, yo)
    ya = yo.get('assignments')
    self.assignments = Items(school, ya, Assignment)




class Assignment(Item):
  def __init__(self, school, yo):
    Item.__init__(self, school, yo)






def tests():
  fp = tools.GetAncestorPath("data/school.yaml")
  assert(fp)
  school = School(fp)
  for subject in school.subjects:
    print("SUBJECT", subject.id)
    for course in subject.courses:
      print("  COURSE", course.id)
      for assignment in course.assignments:
        print("    ASSIGNMENT", assignment.id)


if __name__ == "__main__":
  tests()
