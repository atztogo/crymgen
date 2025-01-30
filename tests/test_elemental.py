"""Tests for the elemental system."""

from crysgen.elemental import GenElemental


def test_gen_elemental():
    """Test GenElemental class."""
    ref_spg_numbers = [2, 10, 47, 123, 191, 191, 221]
    crystal_systems = GenElemental._CRYSTAL_SYSTEMS

    for val, number in zip(crystal_systems, ref_spg_numbers, strict=True):
        gm = GenElemental(val)
        gm.points = [[0, 0, 0]]
        gm.numbers = [1]
        assert gm.run_spglib().dataset.number == number
