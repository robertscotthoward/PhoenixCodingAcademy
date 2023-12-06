[TOC]

# Overview

This page shows some examples of how to include mathematical formula in your markdown documents, which MathJax renders for you.
Python equivalents will also accompany the formula so you can see the relationship.

# General Usage

There are two ways to put math equations in your markdown (*.md) document: inline or block.

The "inline" use a **single pair of dollar signs**. For example, I put this inline equation $x_5 = x^2 + 2x - 5$ right in this sentence.
The actual text is:

```
I put this inline equation $x_5 = x^2 + 2x - 5$ right in this sentence
```

The "block" method uses **double pairs of dollar signs**, like this:
```
$$
\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}
$$
```

renders as this:
$$
\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}
$$

The use of the backslash is an indication that LaTeX is driving the layout.

# Symbols

Cool site [Detexify](http://detexify.kirelabs.org/classify.html). Draw a symbol with your mouse and get the Tex result.

## Greek Letters
```
\alpha, \beta, \gamma, \delta, \epsilon, \varepsilon, \zeta, \eta, \theta, \vartheta, \iota, \kappa, \lambda, \mu, \nu, \xi, \omicron, \pi, \varpi, \rho, \varrho, \sigma, \varsigma, \tau, \upsilon, \phi, \varphi, \chi, \psi, \omega
```
$$
\alpha, \beta, \gamma, \delta, \epsilon, \varepsilon, \zeta, \eta, \theta, \vartheta, \iota, \kappa, \lambda, \mu, \nu, \xi, \omicron, \pi, \varpi, \rho, \varrho, \sigma, \varsigma, \tau, \upsilon, \phi, \varphi, \chi, \psi, \omega
$$

```
A, B, \Gamma, \Delta, E, Z, H, \Theta, I, K, \Lambda, M, N, \Xi, O, \Pi, P, \Sigma, T, \Upsilon, \Phi, X, \Psi, \Omega
```

$$
A, B, \Gamma, \Delta, E, Z, H, \Theta, I, K, \Lambda, M, N, \Xi, O, \Pi, P, \Sigma, T, \Upsilon, \Phi, X, \Psi, \Omega
$$

NOTE: "\Alpha" is not rendered in every engine. Capital ALPHA in Greek is the same letter as the Roman letter A, among others.

## Spaces

* Thin space: `$A \ B$` = $A \ B$
* Normal space: `$A \; B$` = $A \; B$
* Big space: `$A \quad B$` = $A \quad B$
* Bigger space: `$A \qquad B$` = $A \qquad B$


# Expressions

## General equations and expressions
```
$$
y = mx + b
$$
```
$$
y = mx + b
$$
```python
y = m * x + b
```

## Division and Over
```
$$
f(x) = { (x+3) (2-x) \over (2x-5)}
$$
```
$$
f(x) = { (x+3) (2-x) \over (2x-5)}
$$
```python
def f(x):
  return (x+3) * (2-x) / (2*x-5)
```

## Absolute Value
```
$$
y = \vert {3 \over (2x)} \vert
$$
```
$$
y = \vert {3 \over (2x)} \vert
$$
```python
y = abs(3/(2*x))
```

# Quadratic Formula
```
$$
x = {-b \pm \sqrt{b^2-4ac} \over 2a}
$$
```
$$
x = {-b \pm \sqrt{b^2-4ac} \over 2a}
$$
```python
from math import *
a = 2
b = 5
c = 3
print('x =', (-b + sqrt(b**2 - 4*a*c))/(2*a))
print('x =', (-b - sqrt(b**2 - 4*a*c))/(2*a))
```
```
x = -1.0
x = -1.5
```

# Summation - calculate Euler's constant

To calculate the value of `e`
```
$$
e = \sum_{i=0}^\infty \frac{1}{i!}
$$
```
$$
e = \sum_{i=0}^\infty \frac{1}{i!}
$$
```python
from math import *
s = 0
for i in range(1000):
    s += 1/factorial(i)
print(s)
```
```
2.7182818284590455
```
Mnemonic: Andrew Jackson was the first president to serve 2 terms. He was the 7th president of the USA. He was elected in 1828. A right isosceles triangle has angles 45, 90, and 45.

#
```
$$
$$
```
$$
$$
```python

```

# Vectors

See [Machine Learning](/pages/ML.md)



# Layout

## Putting two expressions side-by-side



# Examples

Einstein Field Equation:
```
$$
R_{\mu \nu} - {1 \over 2} g_{\mu \nu}\,R + g_{\mu \nu} \Lambda = {8 \pi G \over c^4} T_{\mu \nu}
$$
```

$$
R_{\mu \nu} - {1 \over 2} g_{\mu \nu}\,R + g_{\mu \nu} \Lambda = {8 \pi G \over c^4} T_{\mu \nu}
$$


# References

* [MathJax symbol reference](https://bearnok.com/grva/en/knowledge/software/mathjax)