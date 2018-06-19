"""
Quine McCluskey digital logic simplification
"""
import itertools

__author__ = 'Daniel Copley'
__version__ = 'v0.3-beta'


class Term:
    """
    Term object
    """
    def __init__(self, bin_str):
        self.bin_str = bin_str
        self.covered = False

    def __eq__(self, other):
        if isinstance(other, Term):
            return True if self.bin_str == other.bin_str else False
        elif isinstance(other, str):
            return True if self.bin_str == other else False
        return False

    def __len__(self):
        return len(self.bin_str)

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
    if difference == 1:
        num1.covered, num2.covered = True, True
        return True


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


def reduce_pairs(pairs):
    """
    :param pairs: iterable of tuples
    :return: set of reduced Term objects
    """
    return set(map(reduce_bits, filter(differ_by_one, pairs)))


def format_minimized_expression(prime_implicants):
    """
    :param prime_implicants: list of Term objects
    :return: str formatted logic expression
    """
    if not prime_implicants:  # If no prime implicants, return 0
        return '0'
    elif prime_implicants[0] == '-' * len(prime_implicants[0]):  # If all dashes, return 1
        return '1'

    result = ''
    for iteration, prime_implicant in enumerate(prime_implicants):
        for index, letter in enumerate(prime_implicant):
            if letter == '1':
                result += chr(ord('A') + index)
            elif letter == '0':
                result += chr(ord('A') + index) + "'"
        if iteration != (len(prime_implicants) - 1):  # Check to see if last prime_implicant
            result += ' + '

    return result


def minimize(n_bits, minterms, xterms):
    """
    :param n_bits: number of bits in equation
    :param minterms: list of integer minterms
    :param xterms: list of integer don't care terms
    :return: list of essential prime implicants (as binary strings)
    """
    # Error checking
    if max(minterms, default=0) > 2 ** n_bits or max(xterms, default=0) > 2 ** n_bits:
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

    reduced_pairs = [terms]
    pairs = get_pairs(terms)
    reduced_pairs.append(reduce_pairs(pairs))

    while reduced_pairs[-1]:
        pairs = get_pairs(reduced_pairs[-1])
        reduced_pairs.append(reduce_pairs(pairs))

    reduced_pairs = reduced_pairs[:-1]

    prime_implicants = []

    for item in reduced_pairs:
        for term in item:
            if not term.covered and term not in xterms:
                prime_implicants.append(term)

    # TODO: Implement Petrick's method to find full simplified equation

    return prime_implicants


if __name__ == '__main__':
    variables = int(input("Enter number of terms: "))
    mt = list(map(int, input("Enter minterms: ").split()))
    dc = list(map(int, input("Enter don't care terms: ").split()))

    minimized = minimize(variables, mt, dc)
    formatted_minimized = format_minimized_expression(minimized)

    print('\nPrime Implicants: {}'.format(minimized))
    print('Minimized Expression: {}'.format(formatted_minimized))
