"""Tests for the elemental system."""

import pathlib

import pytest

from crymgen.generate import BaseGenerator
from crymgen.structure import BaseExpander, BaseStructure

cwd = pathlib.Path(__file__).parent


def test_gen_elemental():
    """Test BaseGenerator class for elemental system."""
    ref_spg_numbers = [2, 10, 47, 123, 191, 191, 221]
    crystal_systems = BaseGenerator.CRYSTAL_SYSTEMS

    for val, number in zip(crystal_systems, ref_spg_numbers, strict=True):
        gm = BaseGenerator(val)
        gm.points = [[0.1, 0.2, 0.3]]
        gm.numbers = [1]
        assert gm.find_symmetry_dataset().space_group_number == number


def test_expand_elemental():
    """Test BaseGenerator class for elemental system.

    Space group numbers covered:
    2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 43, 47, 48,
    49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
    68, 69, 70, 71, 72, 73, 74, 76, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
    90, 91, 92, 93, 94, 95, 96, 97, 98, 109, 110, 111, 112, 113, 114, 115, 116,
    117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
    132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 151, 152, 153, 154,
    160, 164, 166, 178, 179, 180, 181, 187, 191, 194, 195, 197, 198, 199, 200,
    201, 204, 205, 206, 207, 208, 211, 212, 213, 214, 215, 216, 217, 218, 220,
    221, 222, 223, 224, 225, 227, 229, 230

    """
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
            if bs.space_group_number == spg_num:
                structure_list.append(bs)

            filename = cwd / f"data/elemental/unitcell_{bs.space_group_number}.yaml.xz"
            bs_ref = BaseStructure().load_structure(filename)
            assert (
                bs_ref.find_symmetry_dataset().space_group_number
                == bs.space_group_number
            )
            assert bs_ref.space_group_number == bs.space_group_number

    # print("Finally found space group structures", len(structure_list))
    # for bs in structure_list:
    #     filename = cwd / f"data/elemental/unitcell_{bs.space_group_number}.yaml"
    #     with open(filename, "w") as f:
    #         print(
    #             f"Structure for space group number: {bs.space_group_number} "
    #             f"is save to {filename}."
    #         )
    #         print(bs, file=f)


@pytest.mark.parametrize("tol", [1e-2, 1e-3, 1e-4, 1e-5, 1e-6])
def test_expand_elemental_cubic(tol: float):
    """Test BaseGenerator class for elemental system for cubic.

    Space group numbers covered:
    196-230 (all cubic)

    """
    structure_list = []
    gm = BaseGenerator("cubic")
    gm.points = [[0.03345665, 0.1586839, 0.42135608]]
    gm.numbers = [1]

    for spg_num in gm.crystal_system_class.get_spg_numbers():
        be = BaseExpander().set_structure(gm)
        be.read_symmetry_operations(spg_num)
        be.expand()
        bs = BaseStructure().set_structure(be)
        bs.find_symmetry_dataset(tol=tol)
        if bs.space_group_number == spg_num:
            structure_list.append(bs)

        filename = (
            cwd / f"data/elemental_cubic/unitcell_{bs.space_group_number}.yaml.xz"
        )
        bs_ref = BaseStructure().load_structure(filename)
        assert (
            bs_ref.find_symmetry_dataset().space_group_number == bs.space_group_number
        )
        assert bs_ref.space_group_number == bs.space_group_number

    # print("Finally found space group structures", len(structure_list))
    # for bs in structure_list:
    #     filename = cwd / f"data/elemental_cubic/unitcell_{bs.space_group_number}.yaml"
    #     with open(filename, "w") as f:
    #         print(
    #             f"Structure for space group number: {bs.space_group_number} "
    #             f"is save to {filename}."
    #         )
    #         print(bs, file=f)


def test_gen_binary():
    """Test BaseGenerator class for binary system."""
    ref_spg_numbers = [1, 1, 1, 8, 8, 8, 160]
    crystal_systems = BaseGenerator.CRYSTAL_SYSTEMS

    for val, number in zip(crystal_systems, ref_spg_numbers, strict=True):
        gm = BaseGenerator(val)
        gm.points = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
        gm.numbers = [1, 2]
        assert gm.find_symmetry_dataset().space_group_number == number


def test_expand_binary():
    """Test BaseGenerator class for binary system.

    Space group numbers not covered:
    196, 202, 203, 209, 210, 219, 226, 228

    Space group number covered:
    1 - 195, 197 - 201, 204 - 208, 211 - 218, 220 - 225, 227, 229, 230

    """
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
            if bs.space_group_number == spg_num:
                structure_list.append(bs)

            filename = cwd / f"data/binary/unitcell_{bs.space_group_number}.yaml.xz"
            bs_ref = BaseStructure().load_structure(filename)
            assert (
                bs_ref.find_symmetry_dataset().space_group_number
                == bs.space_group_number
            )
            assert bs_ref.space_group_number == bs.space_group_number

    # print("Finally found space group structures", len(structure_list))
    # for bs in structure_list:
    #     filename = cwd / f"data/binary/unitcell_{bs.space_group_number}.yaml"
    #     with open(filename, "w") as f:
    #         print(
    #             f"Structure for space group number: {bs.space_group_number} "
    #             f"is save to {filename}."
    #         )
    #         print(bs, file=f)
