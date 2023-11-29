# Phoenix Coding Academy Computer Science Club

[Phoenix Coding Academy](/pages/PCA.md) (PCA) has an after-hours Computer Science Club that meets Friday after class. Members will learn modern tools for engineering and university academics. The course is designed for self-driven learners who attend PCA, but anyone is welcome. Attendance can be remote and asynchronous.

- [Phoenix Coding Academy Computer Science Club](#phoenix-coding-academy-computer-science-club)
- [Quick Links](#quick-links)
- [Summary Goals](#summary-goals)
- [Goals](#goals)
- [Strategy](#strategy)
- [Testing](#testing)

# Quick Links
* [Membership](/pages/Membership.md) - *how to join this club.*
* [Quick Start](/pages/QuickStart.md) - *how to pull the code for this site and run it locally on you machine.*
* [How this site works](/pages/Architecture.md) - *general architecture and requirements choices.*
* [Github Organization](https://github.com/PhoenixCodingAcademy)
    * [Main Repo](https://github.com/PhoenixCodingAcademy/PhoenixCodingAcademy)
* For members:
    * [Project Board](https://github.com/orgs/PhoenixCodingAcademy/projects/2/views/1)

# Summary Goals
* Learn by teaching. Help create class content and tests.
* Learn collaborative application development through Git.
* Broad overview of many subjects.
* Prove you know your stuff.
* Think big! Scale out to other schools - perhaps nation-wide.



# Goals
* Primarily learn **what** subjects are important, why knowledge of them will give you a head start at the university or workplace, and increase your value to the world. Quickly know where to find the best online guides and tutorials, and how to get started quickly. Then, if any subject really grabs your interest, you can go further into the subject by following the online tutorials to learn **how** to solve problems. You can become the Subject Matter Expert (SME) for any number of courses in the club to provide new learners a person from which get help. Interested in a subject that is not in "this list"? Create it!
* Pad your resume very quickly with lots of techniques where you can talk for 5 minutes on any subject.
* Learn why these subjects are important in the professional and academic fields and how.
* Help create this class by creating subject content as a team.
* Learn by also teaching and taking practice tests that you create as you learn.

# Strategy
As a participant, you will be any or all of these roles:

* **Learner**, where you follow courses, do assignments, take tests. Learners are students that continue to learn after the completing the courses.

* **Teacher**, where you help other learners, and grade assignments.

* **Author**, where you create courses, assignments, test questions, and other curriculum components.
What you choose to do at any time is what you are.

Any participant (author) will create the content in this school. [Git Workflow](./pages/GitWorkflow.md) is just one of the modern techniques for a community of creators (e.g. developers, teachers, authors) to work together to create a product in a well-managed manner. This course is the product, and so Git Workflow will be taught to all learners and used by all authors.

> *Always strive to be the teacher because no-one learns more than the teacher.*

This class is a series of courses (at least one for each subject) that grow over time that the club members create. Each course can be completed in any order; or skipped altogether. A course will have one or more assignments. The goal of the first assignment will be do the minimal thing needed to allow you to go deeper into the subject. For example, for the "Python" course, you can expect the first assignment to show you how to get Python installed on your machine, or use a web host (e.g. repl.it or w3schools) to enter a single line of code that prints "Hello World". Such an assignment can be completed in 5 minutes, but then other assignments in that course can build on top of the first one. Tutorials will likely be a combination of free online references that successively get more advanced. Each stage of a course will have tests that measure your progress. You can take any test at any time. You can memorize the answers if you wish, but even that takes effort, and you will learn because each question presents the

As a participant, you will do one or more of the following:

* Follow a course to learn new skills in that course
* Complete course assignments that apply what you learn
* Grade other assignment
* Propose and create content and new assignment

Rather than delve deep into any one subject, you'll be encouraged to complete only the first one or two assignments of the first course and then move onto another subject. This will give you a quick broad sweep of many skills that can come together to later to build big complex systems. You'll figure out which courses interest you the most, and then you can create content for those courses to teach yourself more, and perhaps other learners as well.

# Testing
You can actually learn a lot by taking tests, but only if the tests explain why an answer is correct or not; see [reason](data/questions/README.md).
When you take a practice test, you are asked a series of questions. Each question has zero or more correct answers and one or more wrong answers. The answers are randomized and presented as check boxes.
If all are correct, then check all the boxes.
If none are correct, then check no boxes.

Example:
```text
Which of the following are colors:
[ ] Orange
[ ] Dog
[ ] Car
[ ] Blue
[ ] House
```

As an author, you can easily model each question in a YAML file.
The learner chooses:

* A mode:
    * `Learn`
    * `Test`
* A number of questions (N).

The test engine randomizes all questions and picks the first N of them. For each question, the engine randomizes all the answers (right and wrong ones) and then presents all answers (maximum five) as checkboxes. This implies that 5 checkboxes have only 1 in 32 ways to be correct. Each question will have a scoring method, which might (for example) be +1 for each correct answer, -1 for each incorrect one.

In `Learn` mode, the learner answers a question, and then the answers and explanations are shown; correct answers in GREEN, incorrect ones in RED. In `Test` mode, the learner answers all questions first, a score is recorded, and then the learner has the option to review each question just like in `Learn` mode.
