"""
Quine McCluskey digital logic simplification
"""
import itertools

__author__ = 'Daniel Copley'
__version__ = 'DEVELOPMENT'


class Term():
    """
    Term object
    """
    def __init__(self, bin_str):
        self.bin_str = bin_str
        self.covered = False

    def __eq__(self, other):
        return True if self.bin_str == other.bin_str else False

    def __hash__(self):
        return hash(self.bin_str)

    def __str__(self):
        return self.bin_str

    def __repr__(self):
        return str(self)

    def __iter__(self):
        for bit in self.bin_str:
            yield bit

    def __getitem__(self, index):
        return self.bin_str[index]

    def __setitem__(self, index, value):
        self.bin_str[index] = value


def differ_by_one(nums):
    """
    :param nums: tuple of binary strings
    :return: true if it differs by only one bit, else false
    """
    num1, num2 = nums
    difference = 0
    for index, bit in enumerate(num1):
        if bit != num2[index]:
            difference += 1
    if difference == 1:
        num1.covered, num2.covered = True, True
        return True
    return False


def reduce_bits(nums):
    """
    :param nums: tuple of binary strings
    :return: list of reduced binary strings
    """
    num1, num2 = nums
    result = ""
    for index, bit in enumerate(num1):
        result += bit if bit == num2[index] else '-'
    return Term(result)


def get_pairs(terms):
    """
    :param terms: iterable of minterms & xterms
    :return: generator of combinations
    """
    return itertools.combinations(terms, 2)


def minimize(n_bits, minterms, xterms):
    """
    :param n_bits: number of bits in equation
    :param minterms: list of integer minterms
    :param xterms: list of integer don't care terms
    :return: list of essential prime implicants (as binary strings)
    """
    # Error checking
    if max(minterms) > 2 ** n_bits or max(xterms) > 2 ** n_bits:
        raise ValueError("integer overflow")

    # Minimizing
    minterms = [Term(format(i, '0{}b'.format(n_bits))) for i in minterms]
    xterms = [Term(format(i, '0{}b'.format(n_bits))) for i in xterms]
    terms = set(minterms + xterms)

    # The structure:
    # 1. Get all combination pairs
    # 2. Filter out items that differ by more than one bit
    # 3. Go through each pair that differs by only one bit and create a new Term with covered bits dashed out
    # 4. Repeat until there are no more simplifications
    # 5. Find fully minimized equation using Petrick's method

    pairs = get_pairs(terms)
    foo = list(filter(differ_by_one, pairs))
    bar = map(reduce_bits, foo)


if __name__ == '__main__':
    # n_bits = int(input("Enter number of terms: "))
    # minterms = list(map(int, input("Enter minterms: ").split()))
    # xterms = list(map(int, input("Enter don't care terms: ").split()))

    n_bits = 4
    minterms = [0, 3, 7, 5]
    xterms = [2, 8]

    minimize(n_bits, minterms, xterms)
