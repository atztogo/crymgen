"""Tests for the elemental system."""

import pathlib

from crysgen.elemental import GenElemental
from crysgen.structure import BaseExpander, BaseStructure

cwd = pathlib.Path(__file__).parent


def test_gen_elemental():
    """Test GenElemental class."""
    ref_spg_numbers = [2, 10, 47, 123, 191, 191, 221]
    crystal_systems = GenElemental.CRYSTAL_SYSTEMS

    for val, number in zip(crystal_systems, ref_spg_numbers, strict=True):
        gm = GenElemental(val)
        gm.points = [[0.1, 0.2, 0.3]]
        gm.numbers = [1]
        assert gm.find_symmetry_dataset().dataset.number == number


def test_expand_elemental():
    """Test GenElemental class."""
    ref_spg_numbers = [2, 10, 47, 123, 191, 191, 221]
    crystal_systems = GenElemental.CRYSTAL_SYSTEMS

    structure_list = []
    for val, number in zip(crystal_systems, ref_spg_numbers, strict=True):
        gm = GenElemental(val)
        gm.points = [[0.1, 0.2, 0.3]]
        gm.numbers = [1]
        assert gm.find_symmetry_dataset().dataset.number == number

        for spg_num in gm.crystal_system_class.get_spg_numbers():
            be = BaseExpander().set_structure(gm)
            be.read_symmetry_operations(spg_num)
            be.expand()
            bs = BaseStructure().set_structure(be)
            bs.find_symmetry_dataset()
            if bs.dataset.number == spg_num:
                structure_list.append(bs)

            filename = cwd / f"data/elemental/unitcell_{bs.dataset.number}.yaml.xz"
            bs_ref = BaseStructure().load_structure(filename)
            assert bs_ref.find_symmetry_dataset().dataset.number == bs.dataset.number
            assert bs_ref.space_group_number == bs.dataset.number

    # print("Finally found space group structures", len(structure_list))
    # for bs in structure_list:
    #     filename = cwd / f"data/unitcell_{bs.dataset.number}.yaml"
    #     with open(filename, "w") as f:
    #         print(
    #             f"Structure for space group number: {bs.dataset.number} "
    #             f"is save to {filename}."
    #         )
    #         print(bs, file=f)
