# QuineMcCluskey

### Table of Contents
**[Introduction](#introduction)**<br>
**[Requirements](#requirements)**<br>
**[Usage](#usage)**<br>
**[Resources](#resources)**<br>
**[License](#license)**<br>

### Quine–McCluskey Algorithm Python Library

Welcome to the Quine–McCluskey Python library – a powerful tool for minimizing Boolean functions with ease!
Developed by Willard V. Quine and extended by Edward J. McCluskey, this algorithm is your go-to method for
simplifying Boolean expressions efficiently.

### Installation

Now you can install the Quine–McCluskey Python library using `pip`. Just run the following command:

```bash
pip install simpliqm
```

### Getting Started

Once installed, you can leverage the library's public API directly from Python. Two essential functions are at
your disposal:

1. **`minimize`**: Minimize Boolean functions with the provided minterms and optional don't care terms.
2. **`format_minimized_expression`**: Format the minimized expression for clearer representation.

### Command Line Interface

Additionally, the library provides a convenient command-line interface. After installation, you can use the
'qm' entry point directly from the terminal:

```bash
qm
```

### Requirements

Ensure you have Python version 3.6 or higher installed to use this library.

### Usage

#### From Python:

```python
from simpliqm import minimize, format_minimized_expression

n_bits = 4
minterms = [0, 1, 2, 4, 8, 10, 12, 15]
xterms = [5, 6]

minimized_result = minimize(n_bits, minterms, xterms)
formatted_result = format_minimized_expression(minimized_result)

print(f"Minimized Expression: {formatted_result}")
```

#### From the Terminal:

```bash
qm
```

Follow the prompts to input your Boolean function details.

![Minimization Gif](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2JheWlrcWpmdDNqMnNsdThuc2t1eGVxZ25qN2Z1bGJjdHppZnR6MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DFDib94LuHfto0PREA/giphy.gif)

### Resources

* [Quine McCluskey Algorithm Wikipedia](https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm)
* [Boolean Algebra](https://en.wikipedia.org/wiki/Boolean_algebra)

### License

This project is licensed under the [GNU General Public License v3.0](https://github.com/djcopley/QuineMcCluskey/blob/master/LICENSE).