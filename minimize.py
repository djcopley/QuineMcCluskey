"""
Quine McCluskey digital logic simplification
"""
import itertools
import logging

__author__ = 'Daniel Copley'
__version__ = 'v0.1-beta'


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)


class Term:
    """General term class"""

    def __init__(self, value):
        """
        :param value: either int or tuple
        """
        self.value = value
        self.covered = False

        if isinstance(value, int):
            self.binary = format(value, 'b')
        elif isinstance(value, list):
            for i in value:
                self.binary = self._get_binary(i)

    def __str__(self):
        return '{}'.format(self.value, self.covered)

    def __repr__(self):
        return str(self)

    def __xor__(self, other):
        if isinstance(other, Term):
            return other.value ^ self.value
        else:
            return other ^ self.value

    def _get_binary(self, term):
        return term
