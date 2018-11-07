import unittest
import itertools
from minimize import *


class TestMinimization(unittest.TestCase):
    def test_term(self):
        term = Term('1010')
        assert not term.covered
        term.covered = True
        assert term.covered

        assert term == '1010'
        assert term == Term('1010')

        set(term)

        for index, bit in enumerate(term):
            assert bit == term.bin_str[index]

        assert len(term) == len(term.bin_str)

        assert term[0] == '1'


    def test_differ_by_one(self):
        assert differ_by_one((Term('1010'), Term('1000')))
        assert not differ_by_one((Term('1111'), Term('0000')))

    def test_reduce_bits(self):
        assert reduce_bits((Term('0011'), Term('0010'))) == Term('001-')
        assert reduce_bits((Term('1111'), Term('1111'))) == Term('1111')
        assert reduce_bits((Term('0111'), Term('1111'))) == Term('-111')
        assert reduce_bits((Term('1--1'), Term('1--0'))) == Term('1---')

    def test_get_pairs(self):
        terms = [Term(format(i, '04b')) for i in range(10)]
        assert set(get_pairs(terms)) == set(itertools.combinations(terms, 2))

    def test_format_minimized_expression(self):
        assert format_minimized_expression([]) == '0'
        assert format_minimized_expression([Term(i) for i in ['----']]) == '1'

        assert format_minimized_expression([Term(i) for i in ['1010', '00-1', '-101', '11-0', '1--0', '1---']]) == \
               "AB'CD' + A'B'D + BC'D + ABD' + AD' + A"

    def test_minimize(self):
        assert set(minimize(4, [], [])) == set([])
        assert set(minimize(3, [0, 1, 2, 3, 4, 5, 6, 7], [])) == \
               set([Term(i) for i in ['---']])
        assert set(minimize(3, [0, 2, 4, 5], [6])) == \
               set([Term(i) for i in ['10-', '--0']])
        # assert set(minimize(4, [1, 4, 5, 8, 12, 15], [])) == \
        #        set([Term(i) for i in ['1111', '0-01', '010-', '-100', '1-00']])
        # assert set(minimize(7, [0 , 2, 4, 8, 10, 36, 37, 23, 66, 34, 88, 122], [15, 16, 111])) == \
        #        set([Term(i) for i in ['1011000', '0010111', '1111010', '0000-00', '00-0000', '0-00010',
        #                               '-000010', '0-00100', '010010-', '000-0-0']])
