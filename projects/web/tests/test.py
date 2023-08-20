import sys
import os

# Get this file's path so we can find the libs/
thisFile = os.path.abspath(sys.argv[0])
thisPath = os.path.dirname(thisFile)
root = os.path.abspath(os.path.join(thisPath, os.path.relpath('../..')))
sys.path.append(root)

import libs.tools as tools
import libs.subjects as subjects

def test1():
  subs = subjects.Subjects()
  fp = tools.GetAncestorPath("data/subjects.yaml")
  subs.parseFile(fp)
  print(tools.PrettifyYaml(subs.data))

test1()