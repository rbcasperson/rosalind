from nose.tools import assert_equal
from rosalind.rosalind_hamm import main


def test_main():
    sample_dataset = open('./tests/sample_data/hamm_data.txt').read()
    sample_output = 7
    assert_equal(main(sample_dataset), sample_output)
