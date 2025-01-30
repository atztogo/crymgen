"""Tests for the elemental system."""

import pathlib

from crysgen.generate import BaseGenerator
from crysgen.structure import BaseExpander, BaseStructure

cwd = pathlib.Path(__file__).parent


def test_gen_elemental():
    """Test GenElemental class."""
    ref_spg_numbers = [2, 10, 47, 123, 191, 191, 221]
    crystal_systems = BaseGenerator.CRYSTAL_SYSTEMS

    for val, number in zip(crystal_systems, ref_spg_numbers, strict=True):
        gm = BaseGenerator(val)
        gm.points = [[0.1, 0.2, 0.3]]
        gm.numbers = [1]
        assert gm.find_symmetry_dataset().space_group_number == number


def test_expand_elemental():
    """Test GenElemental class."""
    crystal_systems = BaseGenerator.CRYSTAL_SYSTEMS

    structure_list = []
    for val in crystal_systems:
        gm = BaseGenerator(val)
        gm.points = [[0.1, 0.2, 0.3]]
        gm.numbers = [1]

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
            assert (
                bs_ref.find_symmetry_dataset().space_group_number
                == bs.space_group_number
            )
            assert bs_ref.space_group_number == bs.dataset.number

    # print("Finally found space group structures", len(structure_list))
    # for bs in structure_list:
    #     filename = cwd / f"data/elemental/unitcell_{bs.dataset.number}.yaml"
    #     with open(filename, "w") as f:
    #         print(
    #             f"Structure for space group number: {bs.dataset.number} "
    #             f"is save to {filename}."
    #         )
    #         print(bs, file=f)


def test_gen_binary():
    """Test GenElemental class."""
    ref_spg_numbers = [1, 1, 1, 8, 8, 8, 160]
    crystal_systems = BaseGenerator.CRYSTAL_SYSTEMS

    for val, number in zip(crystal_systems, ref_spg_numbers, strict=True):
        gm = BaseGenerator(val)
        gm.points = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
        gm.numbers = [1, 2]
        assert gm.find_symmetry_dataset().space_group_number == number


def test_expand_binary():
    """Test GenElemental class."""
    crystal_systems = BaseGenerator.CRYSTAL_SYSTEMS

    structure_list = []
    for val in crystal_systems:
        gm = BaseGenerator(val)
        gm.points = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
        gm.numbers = [1, 2]

        for spg_num in gm.crystal_system_class.get_spg_numbers():
            be = BaseExpander().set_structure(gm)
            be.read_symmetry_operations(spg_num)
            be.expand()
            bs = BaseStructure().set_structure(be)
            bs.find_symmetry_dataset()
            if bs.dataset.number == spg_num:
                structure_list.append(bs)

            filename = cwd / f"data/binary/unitcell_{bs.dataset.number}.yaml.xz"
            bs_ref = BaseStructure().load_structure(filename)
            assert (
                bs_ref.find_symmetry_dataset().space_group_number == bs.dataset.number
            )
            assert bs_ref.space_group_number == bs.space_group_number

    # print("Finally found space group structures", len(structure_list))
    # for bs in structure_list:
    #     filename = cwd / f"data/binary/unitcell_{bs.dataset.number}.yaml"
    #     with open(filename, "w") as f:
    #         print(
    #             f"Structure for space group number: {bs.dataset.number} "
    #             f"is save to {filename}."
    #         )
    #         print(bs, file=f)
