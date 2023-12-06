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

## Physics
```
\abs{-57}, \absolutevalue{2x+3}, \acomm{x}, \acos{x}, \acosecant{x}, \acosine{x}, \acot{x}, \acotangent{x}, \acsc{x}, \admat{x}, \anticommutator{x}, \antidiagonalmatrix{x}
\arccos{x}, \arccosecant{x}, \arccosine{x}, \arccot{x}, \arccotangent{x}, \arccsc{x}, \arcsec{x}, \arcsecant{x}, \arcsin{x}, \arcsine{x}, \arctan{x}, \arctangent{x}, \asec{x}, \asecant{x}, \asin{x}, \asine{x}, \atan{x}, \atangent{x}
\bmqty{x}, \bqty{x}, \Bqty{x}, \bra{x}, \braket{x}, \comm{x}, \commutator{x}, \cos{x}, \cosecant{x}, \cosh{x}, \cosine{x}, \cot{x}, \cotangent{x}, \coth{x}, \cp{x}, \cross{x}, \crossproduct{x}
\csc{x}, \csch{x}, \curl{x}, \dd{x}, \derivative{x}, \det{x}, \determinant{x}, \diagonalmatrix{x}, \diffd{x}, \differential{x}, \div{x}, \divergence{x}, \dmat{x}, \dotproduct{x}, \dv{x}, \dyad{x}, \erf{x}, \ev{x}, \eval{x}, \evaluated{x}, \exp{x}, \expectationvalue{x}, \exponential{x}, \expval{x}, \fderivative{x}, \fdv{x}, \flatfrac{x},\functionalderivative{x}, \grad{x}, \gradient{x}, \gradientnabla{x}
\hypcosecant{x}, \hypcosine{x}, \hypcotangent{x}, \hypsecant{x}, \hypsine{x}, \hyptangent{x}
\mdet{x}, \matrixdeterminant{x}, \matrixdeterminant{x}, \matrixel{n}{A}{m}, \matrixelement{n}{A}{m}, \matrixquantity{x}
\Im{x}, \imaginary{x}, \innerproduct{x}
\ip{x}, \ket{x}, \ketbra{x}, \laplacian{x}, \ln{x}, \log{x}, \logarithm{x}
\mel{x}, \mqty{x}, \naturallogarithm{x}, \norm{x}, \op{x}, \order{x}, \qotherwise{x}, \qq{x}, \qqtext{x}, \qsince{x}, \qthen{x}, \qty{x}, \quantity{x}, \qunless{x}, \qusing{x}
\rank{x}, \Re{x}, \real{x}, \Res{x}, \Residue{x}, \sbmqty{x}, \sec{x}, \secant{x}, \sech{x}, \sin{x}, \sine{x}, \sinh{x}, \smallmatrixquantity{x}, \smdet{x}, \smqty{x}, \spmqty{x}
\sPmqty{x}, \svmqty{x}, \tan{x}, \tangent{x}, \tanh{x}, \tr{x}, \Tr{x}, \trace{x}, \Trace{x}, \va{x}, \var{x}, \variation{x}, \vb{x}, \vdot{x}, \vectorarrow{x}, \vectorbold{x}, \vectorunit{x}, \vmqty{x}, \vnabla{x}, \vqty{x}, \vu{x}
```

$$
\abs{-57}, \absolutevalue{2x+3}, \acomm{x}, \acos{x}, \acosecant{x}, \acosine{x}, \acot{x}, \acotangent{x}, \acsc{x}, \admat{x}, \anticommutator{x}, \antidiagonalmatrix{x}
$$

$$
\arccos{x}, \arccosecant{x}, \arccosine{x}, \arccot{x}, \arccotangent{x}, \arccsc{x}, \arcsec{x}, \arcsecant{x}, \arcsin{x}, \arcsine{x}, \arctan{x}, \arctangent{x}, \asec{x}, \asecant{x}, \asin{x}, \asine{x}, \atan{x}, \atangent{x}
$$

$$
\bmqty{x}, \bqty{x}, \Bqty{x}, \bra{x}, \braket{x}, \comm{x}, \commutator{x}, \cos{x}, \cosecant{x}, \cosh{x}, \cosine{x}, \cot{x}, \cotangent{x}, \coth{x}, \cp{x}, \cross{x}, \crossproduct{x}
$$

$$
\csc{x}, \csch{x}, \curl{x}, \dd{x}, \derivative{x}, \det{x}, \determinant{x}, \diagonalmatrix{x}, \diffd{x}, \differential{x}, \div{x}, \divergence{x}, \dmat{x}, \dotproduct{x}, \dv{x}, \dyad{x}, \erf{x}, \ev{x}, \eval{x}, \evaluated{x}, \exp{x}, \expectationvalue{x}, \exponential{x}, \expval{x}, \fderivative{x}, \fdv{x}, \flatfrac{x},\functionalderivative{x}, \grad{x}, \gradient{x}, \gradientnabla{x}
$$

$$
\hypcosecant{x}, \hypcosine{x}, \hypcotangent{x}, \hypsecant{x}, \hypsine{x}, \hyptangent{x}
$$

$$
\mdet{x}, \matrixdeterminant{x}, \matrixdeterminant{x}, \matrixel{n}{A}{m}, \matrixelement{n}{A}{m}, \matrixquantity{x}
$$

$$
\Im{x}, \imaginary{x}, \innerproduct{x}
$$

$$
\ip{x}, \ket{x}, \ketbra{x}, \laplacian{x}, \ln{x}, \log{x}, \logarithm{x}
$$

$$
\mel{x}, \mqty{x}, \naturallogarithm{x}, \norm{x}, \op{x}, \order{x}, \qotherwise{x}, \qq{x}, \qqtext{x}, \qsince{x}, \qthen{x}, \qty{x}, \quantity{x}, \qunless{x}, \qusing{x}
$$

$$
\rank{x}, \Re{x}, \real{x}, \Res{x}, \Residue{x}, \sbmqty{x}, \sec{x}, \secant{x}, \sech{x}, \sin{x}, \sine{x}, \sinh{x}, \smallmatrixquantity{x}, \smdet{x}, \smqty{x}, \spmqty{x}
$$

$$
\sPmqty{x}, \svmqty{x}, \tan{x}, \tangent{x}, \tanh{x}, \tr{x}, \Tr{x}, \trace{x}, \Trace{x}, \va{x}, \var{x}, \variation{x}, \vb{x}, \vdot{x}, \vectorarrow{x}, \vectorbold{x}, \vectorunit{x}, \vmqty{x}, \vnabla{x}, \vqty{x}, \vu{x}
$$

These cause "misplaced &" errors because the markdown is competing with the MathJax library. TODO.
```
\imat{3}, \identitymatrix{3}, \xmat{1}{2}{3}, \xmatrix{x}, \zeromatrix{x}, \zmat{x}
```

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