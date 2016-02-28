# replace PROBLEM on lines 4, 8, and 9

from nose.tools import assert_equal
from rosalind.rosalind_iprb import main


def test_main():
    sample_dataset = "2 2 2"
    sample_output = 0.7833333333333333
    assert_equal(main(sample_dataset), sample_output)
