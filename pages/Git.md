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

## Notation

Your git environment has these named items that point to commits:
*

Commits are often drawn as nodes in a graph. Suppose you are on the `main` branch. When you create your first commit, you have a first commit:

![Alt text](/static/images/commit0.png)



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

You'll see something like this:

```
On branch main
Your branch is up to date with 'upstream/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   ../../pages/Git.md
        new file:   ../../pages/GitCommands.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../../data/git.yaml
        modified:   main.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ../../data/assets/
        ../../pages/DocumentationSystems.md
        ../../pages/Graphs.md
        static/images/
```

This tells you the following:
* `Your branch is up to date with 'upstream/main'` means there has been no new changes in the remote branch since you started working on it.
* `Changes to be committed:` says you staged these files
* `Changes not staged for commit:` there are some files you haven't staged yet.
* `Untracked files:` new files you created but haven't added them yet. VS Code does all this for you when you commit.

## Add all new and modified files

You'll often just do this to add all the recent changes; i.e. stage them.

```
git add .
```

## Commit the staged files

Run this command to commit the staged files under a commit message, which will show up in your commit history.
```
git commit -m "Added files for graphs"
```

You'll see the following
```
[main aeb3443] Added files for graphs
10 files changed, 116 insertions(+), 43 deletions(-)
create mode 100644 data/assets/graphs.vsdx
copy pages/{Git.md => DocumentationSystems.md} (98%)
rewrite pages/Git.md (99%)
create mode 100644 pages/GitCommands.md
create mode 100644 pages/Graphs.md
create mode 100644 projects/web/static/images/digraph.png
create mode 100644 projects/web/static/images/graph.png
create mode 100644 projects/web/static/images/tree.png
```

Notice the `aeb3443` is the new hash (the commit id) of the commit.

## Push the changes to Github

Now that we have the changes stored locally in the commit history, we want to push them to the server so that we can see them over there.

```
git push
```

```
Enumerating objects: 28, done.
Counting objects: 100% (28/28), done.
Delta compression using up to 8 threads
Compressing objects: 100% (18/18), done.
Writing objects: 100% (19/19), 50.24 KiB | 7.18 MiB/s, done.
Total 19 (delta 8), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (8/8), completed with 8 local objects.
To https://github.com/PhoenixCodingAcademy/PhoenixCodingAcademy.git
   63f58da..aeb3443  main -> main
```

## History

To see the commit log history:

```
git log | less
```

For a prettier view:

```
git log --pretty=format:"%h %Cgreen%ad%Creset %an %Cgreen%s%Creset" --date=format:"%a %Y-%m-%d %I:%M %p"
```

to show:

```
c945957 Thu 2023-11-16 03:12 PM Rob Howard requirements.txt created by pipreqs --encoding utf-8
0ce2df2 Thu 2023-11-16 03:12 PM Rob Howard requirements.txt created by pipreqs --encoding utf-8
44abc9a Sat 2023-11-11 04:43 PM Rob Howard Spelling
406eaaa Sat 2023-11-11 04:28 PM Rob Howard Improved timer
38bb121 Sat 2023-11-11 04:12 PM Rob Howard Bitcoin
2b4c345 Mon 2023-11-06 04:53 PM Rob Howard History save
64cdab5 Mon 2023-10-16 08:27 PM Rob Howard Turing
33f2664 Mon 2023-10-16 08:23 AM Rob Howard Fix to style sheet
419f701 Mon 2023-10-16 08:22 AM Rob Howard YAML parsing errors show more details now.
8d32bf8 Sun 2023-10-15 12:46 PM Rob Howard Turing Machines and CadQuery
73c5a47 Sat 2023-10-14 05:16 PM Rob Howard History and Programming Languages Quiz
1f64886 Sat 2023-10-14 01:46 PM Rob Howard Switched back to nbviewer
```

It's good to save this as an alias instead of typing this who thing:

```
git config --global alias.l   "log --pretty=format:'%h %Cgreen%ad%Creset %an %Cgreen%s%Creset' --date=format:'%a %Y-%m-%d %I:%M %p'"
```

Now you can just run this:

```
git l
```

You can create other aliases in time.