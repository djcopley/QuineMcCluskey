import itertools


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
        Method calculates and returns terms covered by Term object
        :return: integer generator of covered terms
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
