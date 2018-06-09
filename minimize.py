"""
Quine McCluskey digital logic simplification
"""
import itertools

__author__ = 'Daniel Copley'
__version__ = 'DEVELOPMENT'


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
    return True if difference == 1 else False


def reduce_bits(nums):
    """
    :param nums: tuple of binary strings
    :return: list of reduced binary strings
    """
    num1, num2 = nums
    result = ""
    for index, bit in enumerate(num1):
        result += bit if bit == num2[index] else '-'
    return result


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
    minterms = [format(i, '0{}b'.format(n_bits)) for i in minterms]
    xterms = [format(i, '0{}b'.format(n_bits)) for i in xterms]
    terms = set(minterms + xterms)

    pairs = get_pairs(terms)
    foo = filter(differ_by_one, pairs)
    bar = map(reduce_bits, foo)

    print(list(bar))
    # while True:
    #     pass


if __name__ == '__main__':
    # n_bits = int(input("Enter number of terms: "))
    # minterms = list(map(int, input("Enter minterms: ").split()))
    # xterms = list(map(int, input("Enter don't care terms: ").split()))

    n_bits = 4
    minterms = [0, 3, 7, 5]
    xterms = [2, 8]

    minimize(n_bits, minterms, xterms)
