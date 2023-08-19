import yaml
import tools

class Subjects:
  def __init__(self):
    pass

  def parseFile(self, path):
    self.data = tools.ReadYaml(path)


class Subject:
  def __init__(self, json):
    self.parse(json)

  def parse(self, data):
    self.data = data