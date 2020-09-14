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

<img src="https://github.com/Rob217/Hermite-functions/blob/master/equations/first_hermite_functions.png" width="250" />
<!---
\psi_0(x) = & \pi^{-1/4} \,\mathrm{e}^{-x^2/2}
\\
\psi_1(x) = & \sqrt{2} \pi^{-1/4} \,x\, \mathrm{e}^{-x^2/2}
-->

## Functions

There are two main functions which employ the efficient recurrence relation method to calculate the Hermite functions:

1. `Hermite_functions(n, x)` : this returns a dictionary with keys given by m for 0 <= m <= n. The recurrence relation calculates every value of m up to n, and so this function returns them all.

2. `Hermite_function(n, x)` : this returns just the final n which means the recurrence calculation can be made more memory efficient. For very large n and dimension of x this is slightly faster than `Hermite_functions` and is already in the same format as x rather than a dictionary.

Additionally, this package provides two subsidiary functions which can be used to check consistency of the calculations:

i. `Hermite_function_analytic(n, x)` : this uses the analytic expressions for psi_n(x) up to n=5.

ii. `Hermite_function_direct(n, x)` : rather than using the recurrence relation, this employs  [```eval_hermite```](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.eval_hermite.html) and [```factorial```](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.factorial.html?highlight=factorial#scipy.special.factorial) from `scipy.special` to directly calculate the Hermite functions. However, because of the intractability of the Hermite polynomials and factorials, this fails for n larger than a couple hundred.

For examples, see [examples](https://github.com/Rob217/Hermite-functions/tree/master/examples) section.


## Installation

To clone and install from GitHub:
```bash
git clone https://github.com/rob217/Hermite-functions.git
cd Hermite-functions
python setup.py install
```

## Final notes

Comments and suggestions are very welcome!
