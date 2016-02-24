from nose.tools import assert_equal
from rosalind.rosalind_gc import main


def test_main():
    sample_dataset = open('./tests/sample_data/gc_data.txt').read()
    sample_output = open('./tests/sample_data/gc_answer.txt').read()
    assert_equal(main(sample_dataset), sample_output)
