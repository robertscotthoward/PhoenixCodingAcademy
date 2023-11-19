[TOC]

# Overview

A **graph** is pretty much a diagram with circles or boxes (called **nodes**) and lines or arrows (called **edges**) that connect them.
Practically all software architecture diagrams are just graphs of some sort.

![Graph](/static/images/graph.png)

The nodes represent "nouns" and the edges represent "verbs" or "relationships".

A directed graph (or **digraph**) is a graph where each edge has one arrow head. An edge with two arrow heads is considered the same as just a edge with no arrow heads. So for convenience, we never draw edges with two arrowheads. The graph below is a **cyclic** digraph because there is a cycle in the graph. That is, you can start on A, go to D, then to C, and back to A. You can **traverse** the graph by starting on A, and then back on A later.

![Alt text](/static/images/digraph.png)

An acyclic digraph (or **directed acyclic graph** or **DAG** or short) is a digraph with no cycles. Examples of DAGs are:

* [Git](/pages/Git.md) commits. [Example1](https://static.javatpoint.com/tutorial/git/images/git-cherry-pick.png), [Example2](https://2.bp.blogspot.com/-9cuZXlUU0q4/WnktmL4fwXI/AAAAAAAAEiM/A4d5PWuDY_M58MAorNte6xEqA3kvfh8zQCLcBGAs/s1600/images.png)
* A family tree, which is not really a tree but a hybrid graph instead. A person node cannot be its own ancestor, but can have multiple parents and multiple children. And a person can have children with another person; e.g. marriage.

When creating a digraph, a DAGs will always result if each time you add a new node to the graph, you create arrows pointing from it to other existing nodes. The only way to get a cycle is to add an arrow to an existing node that points to another existing node. Cycles are not possible with block chain databases like Git.

A **tree** is a digraph with the restriction that a node can not have more than one arrow pointing away from it.

![Alt text](/static/images/tree.png)

