from nose.tools import assert_equal
from rosalind.rosalind_fib import main


def test_main():
    sample_dataset = "5 3"
    sample_output = 19
    assert_equal(main(sample_dataset), sample_output)
