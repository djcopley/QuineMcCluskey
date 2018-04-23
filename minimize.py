"""
Quine McCluskey digital logic simplification
"""
import itertools

__author__ = 'Daniel Copley'
__version__ = 'v0.1-beta'


class Term:
    """General term super class"""
    def __init__(self, value):
        self.value = value
        self.covered = False

    def __repr__(self):
        return '{} : {}'.format(self.value, self.covered)

    def __xor__(self, other):
        if isinstance(other, Term):
            return self.value ^ other.value
        else:
            return self.value ^ other


class Minterm(Term):
    """Class for minterms"""
    pass


class XTerms(Term):
    """Class for don't care terms"""
    pass


class Combinations:
    """Class for successfully reduced combinations"""
    def __init__(self, terms):
        self.value = terms
        self.reduced_value = 0

    def __repr__(self):
        return str(self.value)


class Minimize:
    def __init__(self, num_of_vars, minterms, x_terms):
        self.num_of_vars = num_of_vars
        self.collection = set(minterms + x_terms)

    def count_ones_difference(self):
        for element in list(itertools.combinations(self.collection, 2)):
            print(element)


if __name__ == '__main__':
    vars_input = 3

    minterms_input = [0, 1, 4, 6]
    if max(minterms_input) >= 2 ** vars_input:
        raise ValueError('minterm out of variable range')

    x_terms_input = [2, 7]
    if max(x_terms_input) >= 2 ** vars_input:
        raise ValueError('x_term out of range')

    minterms_l = [Minterm(i) for i in minterms_input]
    x_terms_l = [XTerms(i) for i in x_terms_input]

    m = Minimize(vars_input, minterms_l, x_terms_l)
    print(m.count_ones_difference())
