"""
Quine McCluskey digital logic simplification
"""
import itertools

__author__ = 'Daniel Copley'
__version__ = 'v0.1-beta'


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
        if difference > 1:
            return False
    return True


def minimize(n_bits, minterms, xterms):
    """
    :param minterms: list of integer minterms
    :param xterms: list of integer don't care terms
    :return: list of essential prime implicants (as binary strings)
    """
    # Error checking
    if max(minterms) > 2 ** n_bits or max(xterms) > 2 ** n_bits:
        raise ValueError("integer overflow")

    # Minimizing
    minterms = [format(i, '0{}b'.format(n_bits)) for i in minterms]
    xterms = [format(i, '0{}b'.format(n_bits)) for i in xterms]
    terms = set(minterms + xterms)

    pairs = []

    for pair in itertools.combinations(terms, 2):
        pairs.append(pair)

    print(list(filter(differ_by_one, pairs)))


if __name__ == '__main__':
    # n_bits = int(input("Enter number of terms: "))
    # minterms = list(map(int, input("Enter minterms: ").split()))
    # xterms = list(map(int, input("Enter don't care terms: ").split()))

    n_bits = 4
    minterms = [0, 3, 5, 7]
    xterms = [2, 8]

    minimize(n_bits, minterms, xterms)
