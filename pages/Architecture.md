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

## Data Driven

This site reads most of its content from a single [YAML](/subjects/yaml) file that is checked into the repository. It is the database for this web site. Most changes to this site can be performed in YAML files. Adding content should be as easy as cut/paste/modify.

## Auto Organized

Give the data-driven model of YAML, subjects, courses, and assignments can be organized in a [DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph), which is like a tree but a "thing" can have multiple parents too. Although we use the word "tree" in "family tree", by the [discrete mathematical definition](https://en.wikipedia.org/wiki/Tree_(data_structure)), it is not a tree but a directed acyclic graph (DAG). Colloquially, we call it a tree nevertheless.

Given the DAG structure, subjects can be programmatically rendered in an algorithmic way. See [Subjects](/subjects) as an example of a page where all its content is generated from the YAML file.

## Markdown

Unlike HTML, [Markdown](/pages/Markdown.md) is a very convenient method to create content that is rendered nicely and easy on the eyes. People create entire books using markdown because it is so convenient.

