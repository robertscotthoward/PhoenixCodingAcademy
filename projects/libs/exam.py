from school import School, getSchool
import libs.tools as tools
from io import StringIO
import yaml
import markdown
import os
import sys
import glob
thisFile = os.path.abspath(sys.argv[0])
thisPath = os.path.dirname(thisFile)
root = os.path.abspath(os.path.join(thisPath, os.path.relpath('..')))
sys.path.append(root)



class Answer():
  def __init__(self, yo):
    if isinstance(yo, str):
      yo = {'answer': yo}
    self.yo = yo
    self.answer = yo.get('answer')
    self.explanation = yo.get('explanation', '')
    self.links = yo.get('links', [])

  def __repr__(self): return f"{self.answer}"
  def __str__(self): self.__repr__()





class Question():
  def __init__(self, school, yo):
    self.school = school
    self.yo = yo
    self.id = yo.get('id')
    self.question = yo.get('question')
    self.right = [Answer(x) for x in yo.get('right', [])]
    self.wrong = [Answer(x) for x in yo.get('wrong', [])]

  def __repr__(self): return f"{self.id}: {self.question}"
  def __str__(self): self.__repr__()




class Test():
  def __init__(self, school, questions):
    """Create a test from a sample of questions.

    Args:
        school (School): an instance of the School class
        questions (Question[]): an array of random questions that meet some selection criteria.
    """
    self.school = school
    self.sample = questions





class Exam():
  def __init__(self, school):
    self.school = school
    self.questions = {}

  def loadQuestions(self, tags = []):
    if isinstance(tags, str):
      tags = tags.split()

    self.questions = {}
    data = tools.GetAncestorPath("data")
    for fp in glob.glob(os.path.join(data, 'questions', '*.yaml')):
      yo = tools.ReadYaml(fp)
      for question in yo['questions']:
        id = question['id']
        qTags = question.get('tags', '').split()

        # Are tags empty (meaning all questions) or one tag in tags is also in qTags?
        if not tags or set(tags).intersection(qTags):
          # Yes
          if id in self.questions:
            raise Exception(f"Duplicate question id found {id}")
          self.questions[id] = Question(self.school, question)

  def createTest(self, nQuestions = 20, seed = None):
    import random
    if seed:
      random.seed = seed
    # nq = number of questions to select; maximum nQuestions
    nq = min(nQuestions, len(self.questions))
    sample = random.sample(self.questions.items(), nq)
    print(len(sample))




def test1():
  school = getSchool()
  exam = Exam(school)
  exam.loadQuestions("programming")
  test = exam.createTest()
  for id, question in exam.questions.items():
    print(id)

if __name__ == "__main__":
  test1()
