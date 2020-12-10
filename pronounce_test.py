from collections import namedtuple

import pytest
import pytest_check as check

from pronounce import stresses_for_words, any_is_trochaic_tetrameter

Case = namedtuple('TestCase', ['name', 'input', 'expected'])


# def test_stresses_for_words():
#     cases = [
#         Case('basic', 'deck the halls with boughs of holly', '10101010'),
#         Case('secondary stress converted', 'octopus menorah sweater', '10101010'),
#         Case('unrecognized word returns None', 'deck the halls with bababababa', None),
#     ]
#
#     for case in cases:
#         actual = stresses_for_words(case.input)
#         check.equal(case.expected, actual, 'TEST CASE: {}'.format(case.name))


# def test_maybe_eight_syllables():
#     cases = [
#         Case('basic', 'deck the halls with boughs of holly', True),
#         Case('too short', 'deck the halls with boughs', False),
#         Case('too long', 'deck the halls with boughs of holly and ivy', False),
#         Case('ambiguous true', 'extraordinary dinosaur', True),
#         Case('ambiguous false', 'every time we touch i get this feeling', False),
#         Case('bad word', 'deck the halls with bababababa', False),
#     ]
#
#     for case in cases:
#         actual = maybe_eight_syllables(case.input)
#         check.equal(case.expected, actual, 'TEST CASE: {}'.format(case.name))


def test_is_trochaic_tetrameter():
    cases = [
        Case('basic', 'deck the halls with boughs of holly', True),
        # Case('has secondary stresses', 'octopus menorah sweater', True),
        # Case('many stress can be trochaic', 'deck stress stress stress boughs of holly', True),
        # Case('eight syl iambic', 'the lady doth protest too much', False),
        # Case('too short', 'deck the halls with boughs', False),
        # Case('too long', 'deck the halls with boughs of holly and ivy', False),
        # Case('ambiguous true', 'every time we touch i get this', True),
    ]

    for case in cases:
        print('---{}---'.format(case.name))
        actual = any_is_trochaic_tetrameter(case.input)
        check.equal(case.expected, actual, 'TEST CASE: {}'.format(case.name))