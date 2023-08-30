# Architecture

> Architecture is any solution to a prioritize list of constraints.

This page talks about the reasons why certain choices were made when building this site.

# Requirements

## Use Python 3.10 to serve up the dynamic site
Seems like PCA kids are learning Python, so that makes sense, [and for good reasons](subjects/python). This site uses [Flask](/subjects/flask) to generate its content. It is one of the easier web frameworks to learn, but is quite powerful. There are markdown plugin that are available in Python, thus Flask can access them.

## Markdown
