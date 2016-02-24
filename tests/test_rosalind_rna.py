from nose.tools import assert_equal
from rosalind.rosalind_rna import main


def test_main():
    sample_dataset = "GATGGAACTTGACTACGTAAATT"
    sample_output = "GAUGGAACUUGACUACGUAAAUU"
    assert_equal(main(sample_dataset), sample_output)
