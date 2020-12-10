from collections import namedtuple

import pytest
import pytest_check as check

from tweet import clean_tweet

Case = namedtuple('TestCase', ['name', 'input', 'expected'])


def test_clean_tweet():
    cases = [
        Case('already clean', 'this is a tweet', 'this is a tweet'),
        Case('strip whitespace', 'this is a tweet  ', 'this is a tweet'),
        Case('clean RT', 'RT @someone: this is a tweet', 'this is a tweet'),
        Case('RT handle with punctuation', 'RT @underscore_handle: this is a tweet', 'this is a tweet'),
        Case('url beginning', 'https://www.zombo.com this is a tweet', 'this is a tweet'),
        Case('url middle', 'this is https://www.zombo.com a tweet', 'this is a tweet'),
        Case('url end', 'this is a tweet https://www.zombo.com', 'this is a tweet'),
        Case('RT and url', 'RT @zombo: this is a tweet https://www.zombo.com', 'this is a tweet'),
        Case('url multiple', 'https://www.zombo.com this is a tweet https://www.zombo.com', 'this is a tweet'),

    ]

    for case in cases:
        actual = clean_tweet(case.input)
        check.equal(case.expected, actual, 'TEST CASE: {}'.format(case.name))
