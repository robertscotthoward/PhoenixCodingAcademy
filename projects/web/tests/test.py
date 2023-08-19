from  .. import libs

def test1():
  subjects = libs.subjects.Subjects
  subjects.parseFile(r"../data/courses/subjects.yaml")