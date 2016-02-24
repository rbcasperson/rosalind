from nose.tools import assert_equal
from rosalind.rosalind_ini4 import main


def test_main():
    sample_dataset = open('./tests/sample_data/ini4_data.txt').read()
    sample_output = 7500
    assert_equal(main(sample_dataset), sample_output)
