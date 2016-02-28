from nose.tools import assert_equal
from rosalind.rosalind_prot import main


def test_main():
    sample_dataset = open('./tests/sample_data/prot_data.txt').read()
    sample_output = open('./tests/sample_data/prot_answer.txt').read()
    assert_equal(main(sample_dataset), sample_output)
