from nose.tools import assert_equal
from rosalind.rosalind_ini6 import main


def test_main():
    sample_dataset = open('./tests/sample_data/ini6_data.txt').read()
    sample_output = open('./tests/sample_data/ini6_answer.txt').read()
    # Line in output can be in any order, so we sort both
    assert_equal(sorted(main(sample_dataset)), sorted(sample_output))
