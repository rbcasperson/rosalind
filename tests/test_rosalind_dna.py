from nose.tools import assert_equal
from rosalind.rosalind_dna import main


def test_main():
    sample_dataset = open('./tests/sample_data/dna_data.txt').read()
    sample_output = "20 12 17 21"
    assert_equal(main(sample_dataset), sample_output)
