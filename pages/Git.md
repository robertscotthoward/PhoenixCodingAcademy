[TOC]

# Overview

**Version Control** is any method that keeps track of changes to files in a folder tree. A classic methodology is to make copies of files and rename them with the date and time in the file name, and perhaps who was the last person to make the changes, and then email to your friends so they have a copy.

**Git** is a free program that does version control, but in a more professional and convenient manner.

A **Git Repository** is:

* A folder that contains a hidden `.git` subfolder in it (created by `git clone` or `git init`).
* Allows the owner to keep track of the changes (via commits) and to show a history of who changed what when.
* Can reside on local personal computer, or be in the "cloud"; e.g. Github (the most popular), or Bitbucket, GitLab, Perforce, Beanstalk, Amazon AWS CodeCommit, Codebase, Microsoft Azure DevOps, Launchpad, SourceForge, and Google Cloud Source Repositories.
* Can be linked to one or more other repositories so that changes in one can be easily synchronized to another; e.g. merging, rebasing, pull requests.
* A cryptographic block chain of changes to the folder (called **commits**). Each commit can contain changes to one or more files or folders. As a block chain, it is a [directed graph](/pages/Graphs.md). Since each commit is the cryptographic hash (SHA-256) of zero or more other existing commits, then it is a [DAG](/pages/Graphs.md).

Git is a program that you install on your machine, and is primarily a method to have two or more repositories that both evolve independently (files and folders change over time), but are periodically synchronized together in some manner.

# Workflow

The following methods are very often followed to create a project that multiple people can work on simultaneously by independently. Hereafter, we'll assume **Github** as the chosen remote repository cloud application.

## Create Repository

There are two methods to create a repository:

* **METHOD 1**: From scratch:
  * Locally, in a new folder on your machine, where you run `git init` in that folder.
  * Remotely, where you create the repository in Github using its web interface.

* **METHOD 2**: As a copy of another repository:
  * Locally, in a parent folder on your machine, where you run `git clone {Existing Repository Location}`
  * Remotely, where you have two methods:
    * Copy an existing remote repository (called **forking**) into another remote repository.
    * Copy a local repository to a remote location (called **pushing**).

## Commit Changes

When you make changes to the folders and files in your repository, you'll want to add all (or some) into a set (called **staging**) to create a commit. To stage all changes:

```
git add .
```

To stage just some files, repeat any of the following commands, where FILE and FOLDER can contains wildcards to match:

```
git add FILE
git add FOLDER
```

## Status

To see what is staged and what has changed:

```
git status
```