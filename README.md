# QuineMcCluskey [![Build Status](https://travis-ci.org/djcopley/QuineMcCluskey.svg?branch=master)](https://travis-ci.org/djcopley/QuineMcCluskey)

### Table of Contents
**[Introduction](#introduction)**<br>
**[Requirements](#requirements)**<br>
**[Usage](#usage)**<br>
**[Resources](#resources)**<br>
**[Contributing](#contributing)**<br>
**[License](#license)**<br>

### Introduction
The Quine–McCluskey algorithm (or the method of prime implicants) is a method used for minimization of Boolean functions 
that was developed by Willard V. Quine and extended by Edward J. McCluskey. It is functionally identical to 
Karnaugh mapping, but the tabular form makes it more efficient for use in computer algorithms, and it also gives a 
deterministic way to check that the minimal form of a Boolean function has been reached. It is also referred to as 
the tabulation method.

### Requirements
This program requires python version 3.4 or higher to run.

### Usage
Run the minimize.py file and follow the prompts. Don't care terms are optional, leave blank if there are none. Alternatively import the minimize.py 
file into your project and call the minimize() function. Usage: minimize(n_bits, minterms, xterms). Returns list of 
prime implicants.

![Minimization Gif](https://github.com/djcopley/QuineMcCluskey/blob/master/assets/minimization.gif?raw=true)

### Resources
* [Quine McCluskey Algorithm Wikipedia](https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm)
* [Boolean Algebra](https://en.wikipedia.org/wiki/Boolean_algebra)

### Contributing
If you would like more information, please check out the full set of guidelines [here](https://github.com/djcopley/QuineMcCluskey/blob/master/CONTRIBUTING.md).
Contribution is welcomed!

### License
This project is licensed under the GNU General Public License v3.0