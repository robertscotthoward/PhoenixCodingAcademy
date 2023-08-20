# Overview

The `school.yaml` file contains all the subject, courses, assignments, and questions.

* **Subjects** are broad categories of things, like "Programming Languages", "Data Science", "Mathematics", and "Python". Subjects can form a [DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph); that is, subjects can contain multiple parents and multiple children to for a type of taxonomy. A subject can contain zero or more courses.

* **Courses** are guided learning processes that will help you learn something of value in one or more subjects. A course is a set of assignments that are necessary to do other assignments. When completed, you can take an exam to test your knowledge of the course. The goals of a course are:
* To prove you know the knowledge by taking an exam.
* To know how to help other student who get stuck in the same course.
* To know how to do things required for subsequent courses.

* **Assignments** are sets of instructions that you can follow with some well-defined goal in mind. An assignment has an "Acceptance Criteria" (or just "acceptance") that another participant (preferably a skeptic called the "verifier"; e.g. a grader) can do to verify you have successfully completed an assignment. For example, an assignment might be to install Python 3.11 on your laptop. The verifier will go to your laptop and run a command (or you can in front of the grader) that shows the version of Python installed. An assignment might merely require a minimum score on an exam as the acceptance. You can grade your own assignments too, but your transcript will reflect just that.

The structure of the YAML tree is:
```yaml
subjects:
  SubjectId: OBJECT
    courses: OBJECTS
      assignments: LIST
```

An OBJECT is a collection of these properties:
* `id`: STRING (REQUIRED) that must be unique for all objects in the yaml.
* `title`: STRING that is human readable. If missing, the `id` is used.
* `description`: MARKDOWN that describes the object in detail.
* `parents`: SET of object ids that group such things together and form a DAG.

