from nose.tools import assert_equal
from rosalind.rosalind_ini3 import main


def test_main():
    sample_dataset = open('./tests/sample_data/ini3_data.txt').read()
    sample_output = "Humpty Dumpty"
    assert_equal(main(sample_dataset), sample_output)
