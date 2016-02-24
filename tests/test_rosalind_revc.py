from nose.tools import assert_equal
from rosalind.rosalind_revc import main


def test_main():
    # there's a new line at the end of sample_dataset to match rosalind's file
    sample_dataset = open('./tests/sample_data/revc_data.txt').read()
    sample_output = "ACCGGGTTTT"
    assert_equal(main(sample_dataset), sample_output)
