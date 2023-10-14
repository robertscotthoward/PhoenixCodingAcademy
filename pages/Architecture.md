# Architecture

>> Architecture is any solution to a prioritize list of constraints.

This page talks about the reasons why certain choices were made when building this site.


[TOC]

# Requirements

Requirements are the constraints of a design; what it must do, what it must not do, and what is not important.

## Use Python 3.10 to serve up the dynamic site
Seems like PCA kids are learning Python, so that makes sense, [and for good reasons](subjects/python). This site uses [Flask](/subjects/flask) to generate its content. It is one of the easier web frameworks to learn, but is quite powerful. There are markdown plugin that are available in Python, thus Flask can access them.

## Use Git

For reasons described [HERE](/subjects/git), Git will be used to manage the changes to this site and to deploy to the public "production" web site. These are professional, mature, collaborative methods with high market value. Best to start learning them in this club.

Anyone can fork the repo (or clone it locally) to modify the site and experimentally run it on their local machine or laptop, without changing the production web site. If changes are made that the author believes should be pushed to the production web site, the author can create a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) "proposal" to other members and present the case. If approved by a quorum, and administrator can merge those changes into the main branch and then update the production site with a simple "git pull".

## Folder Layout

The project folder, which is checked into Github, is organized as follows:

* **data/** - any data files pertinent to the web site.
  * **courses/** - maybe obsolete.
  * **questions/** - contains all the questions used to generate tests for subjects.
  * **school.yaml** - contains the main structure of all subjects plus other parameter used in the web site, such as contact emails and addresses. Any subject (e.g. "flask") is merged in with any matching sibling file (e.g. "flask.yaml") if that file is found. You can put everything into the "school.yaml" file, but you also have the option to split out much of the content into its own file to keep the "school.yaml" file from getting too big, and to make it easier for developers to work on their own subjects without colliding with other developers.
* **pages/** - contains `*.md` markdown files that can be rendered on any page. This page, for example, is the `Architecture.md` file in this folder. You can access it from this [THIS URL](/pages/Architecture.md). Markdown files here will render MathJax
* **projects/** - the root folder for all python and app code.
  * **libs/** - common reusable python library files are stored here that `main.py` and other programs load in to use.
  * **notebooks/** - contains all the `*.ipynb` Jupyter Notebook files. You can run `jupyter notebook` in this folder from the command line to launch the notebook web editor.
  * **web/** - the root of the web server.
    * **static/** - any files that might be served up in a CDN; e.g. js, css, and html files.
    * **templates/** - these are the template files for Flask. `base.html` is the main outer template which all other templates inherit. There is usually one for each root route path; e.g. `http://.../subjects` would show the subjects. So there is a `subjects.html` template in this folder. `http://.../subjects/python` would show the python subject. Therefore, we'd expect to see a `subject.html` file for that entry.
    * **zips/** - contains zip files that can be downloaded with url `/zips/FILENAME.zip`
    * **googleXXX.html** - the file that Google gave us to verify we had the authority to use their search engine.
    * **main.py** - the main entry point to the web application. From the command line, run `python main.py` to start the web server. Put a `--debug run` on the end to run in debug mode where you see more error messages.

## Data Driven

This site reads most of its content from a single [YAML](/data/school.yaml) file that is checked into the repository. It is the database for this web site. Most changes to this site can be performed in YAML files. Adding content should be as easy as cut/paste/modify.

## Auto Organized

Give the data-driven model of YAML, subjects, courses, and assignments can be organized in a [DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph), which is like a tree but a "thing" can have multiple parents too. Although we use the word "tree" in "family tree", by the [discrete mathematical definition](https://en.wikipedia.org/wiki/Tree_(data_structure)), it is not a tree but a directed acyclic graph (DAG). Colloquially, we call it a tree nevertheless.

Given the DAG structure, subjects can be programmatically rendered in an algorithmic way. See [Subjects](/subjects) as an example of a page where all its content is generated from the YAML file.

## Markdown

Unlike HTML, [Markdown](/pages/Markdown.md) is a very convenient method to create content that is rendered nicely and easy on the eyes. People create entire books using markdown because it is so convenient.

