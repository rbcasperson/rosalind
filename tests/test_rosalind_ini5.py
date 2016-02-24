from nose.tools import assert_equal
from rosalind.rosalind_ini5 import main


def test_main():
    sample_dataset = open('./tests/sample_data/ini5_data.txt').read()
    sample_output = open('./tests/sample_data/ini5_answer.txt').read()
    assert_equal(main(sample_dataset), sample_output)
