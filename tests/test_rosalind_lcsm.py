from nose.tools import assert_equal
from rosalind.rosalind_lcsm import main

def test_main():
    sample_dataset = open('./tests/sample_data/lcsm_data.txt').read()
    assert main(sample_dataset) in ['AC', 'CA', 'TA']
