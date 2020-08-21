# Hermite function calculator

### Hermite functions
This package calculates the [Hermite functions](https://en.wikipedia.org/wiki/Hermite_polynomials#Hermite_functions), 

<img src="https://github.com/Rob217/Hermite-functions/blob/master/equations/Hermite_functions.png" width="400" />
<!---
\psi_n(x) = \frac{1}{\sqrt{2^n n!}} \frac{1}{\pi^{1/4}} \text{e}^{-x^2/2} H_n(x)
-->

where `n` is a non-negative integer, `x` is a position, and `H_n(x)` are the [Hermite polynomials](https://en.wikipedia.org/wiki/Hermite_polynomials).

### Quantum harmonic oscillator
The Hermite functions are related to the wavefunctions of the [quantum harmonic oscillator](https://en.wikipedia.org/wiki/Quantum_harmonic_oscillator) via the relation

<img src="https://github.com/Rob217/Hermite-functions/blob/master/equations/QHO_wavefunctions.png" width="400" />
<!---
\psi_n^{\mathrm{QHO}}(x) = \left(\frac{1}{2 x_{\mathrm{ZP}}^2}\right)^{1/4}  \psi_n\left(\frac{x}{x_{\mathrm{ZP}} \sqrt{2}}\right)
-->

where `xZP = hbar / 2 m omega` is the zero point motion length, `hbar` is the reduced Planck constant, and `omega` is the harmonic oscillator frequency.

![alt text](https://github.com/Rob217/Hermite-functions/blob/master/examples/QHO_states.png "Quantum harmonic oscillator wavefunctions")


### Calculation method
The Hermite functions can be calculated efficiently using the following recurrence relation

<img src="https://github.com/Rob217/Hermite-functions/blob/master/equations/recurrence_relation.png" width="400" />
<!---
\psi_n(x) = \sqrt{\frac{2}{n}} x \psi_{n-1}(x) - \sqrt{\frac{n-1}{n}} \psi_{n-2}(x)
-->

where the first two Hermite functions are 

<img src="https://github.com/Rob217/Hermite-functions/blob/master/equations/first_Hermite_functions.png" width="400" />
<!---
\psi_0(x) = & \pi^{-1/4} \,\mathrm{e}^{-x^2/2}
\\
\psi_1(x) = & \sqrt{2} \pi^{-1/4} \,x\, \mathrm{e}^{-x^2/2}
-->
