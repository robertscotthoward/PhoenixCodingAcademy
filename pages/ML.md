[TOC]

# Overview

Machine Learning (ML) is described with math.

# Vectors

\begin{equation}
\begin{split}
A & = \frac{\pi r^2}{2} \\
  & = \frac{1}{2} \pi r^2
\end{split}
\end{equation}

A vector is an ordered list of numbers denoted in various ways:

$$\vec{a} = (1, 2, 3)$$
$$\vec{b} = [1, 2, 3]$$
$$\vec{c} = \langle 1, 2, 3 \rangle$$


The three vectors above are the same vector, but with different names. The arrow over the top of the variable tells us that it represents a vector. But the thing to the right of the equal sign is clearly a vector, so we know the variable must be a vector. Thus, we often **omit the arrow**. The notation above are row vectors since they are shown with rows. We can also show them as columns:

$$
a = \begin{bmatrix} 1 \\\\ 2 \\\\ 3 \end{bmatrix}
b = \begin{bmatrix} 4 \\\\ 5 \\\\ 6 \end{bmatrix}
$$

Row or column vectors, they are all the same. Elements are indexed beginning with 1. In Python, C, JavaScript, Rust, and others, indices start with 0. Thus, from above, $b_1 = 4$. To be blatantly clear, we often see the following to tell us what the vector name is "b", what the element names are, and the values:

$$
\newcommand\V[1]{\begin{bmatrix}#1\end{bmatrix}}
\begin{aligned}
b = \V{b_1 \\\\ b_2 \\\\ b_3} = \V{4\\\\5\\\\6}
\end{aligned}
$$

# Dot Product

In neural networks, the dot product between two vectors shows up everywhere.

GIVEN:
$$
\newcommand\V[1]{\begin{bmatrix}#1\end{bmatrix}}
\begin{aligned}
a = \V{1\\\\2\\\\3} \qquad
b = \V{4\\\\5\\\\6}
\end{aligned}
$$

THEN the dot product between a and be is:
$$
a \cdot b = a {^\mathsf T} b = a_1 b_1 + a_2 b_2 + a_3 b_3 = (1 \times 4) + (2 \times 5) + (3 \times 6) = 32
$$

AND the general notation is:

$$
a \cdot b = a {^\mathsf T} b =  \sum_{i=1}^n a_i b_i = a_1 b_1 + a_2 b_2 + \cdots + a_n b_n
$$

In Python:
```python
def dot(a, b):
    if len(a) != len(b): raise Exception("a and b must be the same length")
    s = 0
    for i in range(len(a)):
        s += a[i] * b[i]
    return s

a = [1, 2, 3]
b = [4, 5, 6]
print(dot(a, b))
```

```
32
```

In Python Numpy, which is a lot faster and already defined for you:
```python
import numpy
a = [1, 2, 3]
b = [4, 5, 6]
print(numpy.dot(a, b))
```




# References
