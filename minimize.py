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


class Term:  # TODO Complete term class
    """General term class"""
    pass


# TODO find_prime_implicants() function
def find_print_implicants():
    """

    :return:
    """
    pass


# TODO find_essential_prime_implicants() function
def find_essential_prim_implicants():
    """

    :return:
    """
    pass


# TODO find_solutions() function
def find_solutions():
    """

    :return:
    """
    pass


if __name__ == '__main__':
    pass
