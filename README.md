# Hermite function calculator

This package calculates the [Hermite functions](https://en.wikipedia.org/wiki/Hermite_polynomials#Hermite_functions):

<img src="https://render.githubusercontent.com/render/math?math=\psi_n(x) = \frac{1}{\sqrt{2^n n!}} \frac{1}{\pi^{1/4}} \text{e}^{-x^2/2} H_n(x)">

where <img src="https://render.githubusercontent.com/render/math?math=H_n(x)"> is the nth physicist's Hermite polynomial.

It does this using the following recurrence relation:

<img src="https://render.githubusercontent.com/render/math?math=\psi_n(x) = \sqrt{\frac{n}{2}} \psi_{n-1}(x) + \sqrt{\frac{n+1}{2}} \psi_{n+1}(x)">

Rearranging gives:

<img src="https://render.githubusercontent.com/render/math?math=\psi_m(x) = \sqrt{\frac{2}{m}} x \psi_{m-1}(x) - \sqrt{\frac{m-1}{m}} \psi_{m-2}(x)">
 
