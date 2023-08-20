import sys
import os

# Get this file's path so we can find the libs/
thisFile = os.path.abspath(sys.argv[0])
thisPath = os.path.dirname(thisFile)
root = os.path.abspath(os.path.join(thisPath, os.path.relpath('../..')))
sys.path.append(root)

import libs.tools as tools
from libs.school import School

def test1():
  path = tools.GetAncestorPath("data/school.yaml")
  assert(path)
  school = School(path)
  print(school)

test1()