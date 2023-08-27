* Create an exam from a list of subjects, courses, or assignments. This is resolved into a set of item ids.
* Pick a random seed number, perhaps based on the student's id and exam number.
* For each id in ids:
  * Under the `data/questions` folder find file "{id}.yaml".
  * If the file is not found: continue
  * Add all the questions to a set Q1
* Q2 = 20 random questions from Q1
* For each Q in Q2:
  * Create a list of all right and wrong answers.
  * Pick 5 random answers A
  * Print the question
  * Print each answer in A as a checkbox choice
  * Add check box "None of the above"
  * The student makes the selection
  * If any boxes checks except last one, then the last one gets unchecked.
  * At least one checkbox must be checked for the SUBMIT button to become enabled.
  * The student clicks SUBMIT.
  * If in practice mode, if any are incorrect, the page says so, and the student must try another combination.
  * If in test mode, nothing is shown.

* The exam is completed. The choices are recorded. A score is created.
