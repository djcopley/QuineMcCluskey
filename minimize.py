"""
Quine McCluskey digital logic simplification
"""
import itertools

__author__ = 'Daniel Copley'
__version__ = 'v0.4-beta'


class Term:
    """
    Term class is used to keep track of implicants
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

    def get_covered_terms(self):
        """
        Method calculates terms covered by Term object
        :return: generator object of covered terms
        """
        base = 0
        x_index = [index for index, item in enumerate(self.bin_str[::-1]) if item == '-']

        for index, item in enumerate(self.bin_str[::-1]):
            if item == '1':
                base += 2 ** index

        yield base

        for i in range(len(x_index)):
            for items in itertools.combinations(x_index, i + 1):
                accumulator = 0
                for index in items:
                    accumulator += 2 ** index
                yield base + accumulator


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


def terms_covered_once(prime_implicants, m_terms):
    """
    :param prime_implicants: list of prime implicants
    :param m_terms: list of minterms (as integers, not Term objects)
    :return: terms that are only covered once by prime implicants
    """
    covered = []
    for prime_implicant in prime_implicants:
        for covered_term in prime_implicant.get_covered_terms():
            covered.append(covered_term)
    return [i for i in covered if covered.count(i) == 1 and i in m_terms]


def get_term_max_coverage(prime_implicants, m_terms):
    """
    Function sorts prime implicants based on how many m_terms are covered

    :param prime_implicants: list of prime implicants
    :param m_terms: list of minterms (integers, not Term objects)
    :return: remaining minterms
    """

    term_max_coverage = max(prime_implicants,
              key=lambda prime_implicant: len([i for i in prime_implicant.get_covered_terms() if i in m_terms]))

    return term_max_coverage


def minimize(n_bits, m_terms, x_terms):
    """
    :param n_bits: number of bits in equation
    :param m_terms: list of integer minterms
    :param x_terms: list of integer don't care terms
    :return: list of essential prime implicants (Term objects)
    """
    # Error checking
    if max(m_terms, default=0) > 2 ** n_bits or max(x_terms, default=0) > 2 ** n_bits:
        raise ValueError("integer overflow")

    # Minimizing
    minterms = [Term(format(i, '0{}b'.format(n_bits))) for i in m_terms]
    dcterms = [Term(format(i, '0{}b'.format(n_bits))) for i in x_terms]
    terms = set(minterms + dcterms)

    # Step-by-step
    # 1. Get all combination pairs
    # 2. Filter out items that differ by more than one bit
    # 3. Go through each pair that differs by only one bit and create a new Term with covered bits dashed out
    # 4. Repeat until there are no more simplifications
    # 5. Find fully minimized equation using Petrick's method

    reduced_pairs = [terms]
    pairs = get_pairs(terms)
    reduced_pairs.append(reduce_pairs(pairs))

    # Loop while more pairs can be combined
    while reduced_pairs[-1]:
        pairs = get_pairs(reduced_pairs[-1])
        reduced_pairs.append(reduce_pairs(pairs))

    reduced_pairs = reduced_pairs[:-1]

    prime_implicants = []

    # Find prime implicants
    for item in reduced_pairs:
        for term in item:
            if not term.covered and term not in dcterms:
                prime_implicants.append(term)

    essential_terms = terms_covered_once(prime_implicants, m_terms)
    essential_prime_implicants = []

    # Function determines if list 1 and list 2 intersect
    intersect = lambda l1, l2: len([i for i in l1 if i in l2]) > 0

    # Find essential prime implicants
    for prime_implicant in prime_implicants:
        current_term = tuple(prime_implicant.get_covered_terms())
        if intersect(prime_implicant, essential_terms):
            essential_prime_implicants.append(prime_implicant)
            _m_terms = [i for i in m_terms if i not in current_term]

    # Find remaining implicants
    while m_terms:
        max_prime_implicant = get_term_max_coverage(prime_implicants, m_terms)
        essential_prime_implicants.append(max_prime_implicant)
        m_terms = [i for i in m_terms if i not in max_prime_implicant.get_covered_terms()]

    return essential_prime_implicants


if __name__ == '__main__':
    variables = int(input("Enter number of terms: "))
    mt = list(map(int, input("Enter minterms: ").split()))
    dc = list(map(int, input("Enter don't care terms: ").split()))

    minimized = minimize(variables, mt, dc)
    formatted_minimized = format_minimized_expression(minimized)

    print('\nEssential Prime Implicants: {}'.format(minimized))
    print('Minimized Expression: {}'.format(formatted_minimized))
