# replace PROBLEM on lines 4, 8, and 9

from nose.tools import assert_equal
from rosalind.rosalind_subs import main


def test_main():
    sample_dataset = "GATATATGCATATACTT\nATAT\n"
    sample_output = "2 4 10"
    assert_equal(main(sample_dataset), sample_output)
