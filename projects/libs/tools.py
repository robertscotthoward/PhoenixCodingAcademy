import os
import yaml

def GetAncestorPath(relBasePath):
  p = os.path.curdir
  lp = None
  while True:
    fp = os.path.abspath(os.path.join(p, relBasePath))
    print(fp)
    if os.path.exists(fp):
      return fp
    p = os.path.abspath(os.path.join(p, '..'))
    if p == lp:
      return None
    lp = p


def GetDataPath(fn):
  '''
  @fn is a relative path; e.g. "x.txt" or "mystuff/x.txt"
  This function defines where these data items are to be stored;
  currently in the "data/" folder, but we might change it later.
  '''
  return os.path.join("data", fn)


def DataFileExists(fn):
  return os.path.exists(GetDataPath(fn))


def subloadYaml(data):
  '''
  Modify data by loading in any references to external files.
  This is sort of like an "include" statement.
  '''
  # If it's a list, then recur on each item.
  if type(data) == list:
    for x in data:
      subloadYaml(x)

  # If it's a dict then look for a 'ref'.
  elif type(data) == dict:
    # Does it have a 'ref' property?
    if 'ref' in data:
      # Yes, so that means to replace it with the external file.
      data['ref'] = ReadYaml(data['ref'])
    else:
      # No, so recur on each property.
      for k in data:
        subloadYaml(data[k])

def ParseYaml(s):
  '''
  Parses a yaml string into an object.
  If any parts of the file refer to other files, read those in recursively.
  See: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
  '''
  data = yaml.safe_load(s)
  subloadYaml(data)
  return data


def readFile(fn):
  dn = GetDataPath(fn)
  with open(dn) as f:
    return f.read()

def writeFile(fn, data):
  with open(fn, 'w') as f:
    f.write(data)


def ReadYaml(fn):
  '''
  Read a *.yaml file from the "data" folder into a dict (i.e. dictionary) object.
  If any parts of the file refer to other files, read those in recursively.
  See: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
  '''
  dn = GetDataPath(fn)
  with open(dn) as f:
    data = yaml.safe_load(f)
    subloadYaml(data)
    return data


def WriteYaml(fn, obj):
  '''
  Write a dict object to a *.yaml file in the "data" folder.
  '''
  dn = GetDataPath(fn)
  dir = os.path.dirname(os.path.abspath(dn))
  os.makedirs(dir, exist_ok=True)
  writeFile(dn, PrettifyYaml(obj))

def PrettifyYaml(obj):
  def str_presenter(dumper, data):
      """configures yaml for dumping multiline strings
      Ref: https://stackoverflow.com/questions/8640959/how-can-i-control-what-scalar-form-pyyaml-uses-for-my-data"""
      if len(data.splitlines()) > 1:  # check for multiline string
          return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
      return dumper.represent_scalar('tag:yaml.org,2002:str', data)

  yaml.add_representer(str, str_presenter)
  yaml.representer.SafeRepresenter.add_representer(str, str_presenter)

  return yaml.dump(obj, indent=2)


def md5(s):
  import hashlib
  hash = hashlib.md5()
  if type(s) == str:
    s = str.encode(s)
  hash.update(s)
  return  hash.hexdigest()


def tests():
  h = md5("The quick brown fox jumps over the lazy dog")
  assert(h == "9e107d9d372bb6826bd81d3542a419d6")

if __name__ == "__main__":
  tests()
