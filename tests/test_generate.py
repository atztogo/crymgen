"""Tests for the elemental system."""

from __future__ import annotations

import pathlib

import pytest

from crymgen.generate import BaseGenerator
from crymgen.structure import BaseExpander, BaseStructure

cwd = pathlib.Path(__file__).parent


def test_gen_binary():
    """Test BaseGenerator class for binary system."""
    ref_spg_numbers = [1, 1, 1, 8, 8, 8, 160]
    crystal_systems = BaseGenerator.CRYSTAL_SYSTEMS

    for val, number in zip(crystal_systems, ref_spg_numbers, strict=True):
        gm = BaseGenerator(val)
        gm.points = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
        gm.numbers = [1, 2]
        assert gm.find_symmetry_dataset().space_group_number == number


@pytest.mark.parametrize("tol", [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6])
def test_expand_binary(tol: float):
    """Test BaseGenerator class for binary system."""
    for crystal_system, bs in _generate_binary_crystal_structures(tol):
        filename = (
            cwd / f"data/binary/{crystal_system}/unitcell_{bs.space_group_number}.yaml"
        )
        bs_ref = BaseStructure().load_structure(filename)
        assert (
            bs_ref.find_symmetry_dataset().space_group_number == bs.space_group_number
        )
        assert bs_ref.space_group_number == bs.space_group_number

    # print("Finally found space group structures", len(structure_list))


@pytest.mark.gendata
def test_generate_data_for_expand_binary():
    """Generate text data of crystal structures for binary system."""
    for crystal_system, bs in _generate_binary_crystal_structures(1e-5):
        filename = (
            cwd / f"data/binary/{crystal_system}/unitcell_{bs.space_group_number}.yaml"
        )
        with open(filename, "w") as f:
            print(
                f"Structure for space group number: {bs.space_group_number} "
                f"is save to {filename}."
            )
            print(bs, file=f)


def _generate_binary_crystal_structures(tol: float):
    """Generate crystal structures for binary system.

    [[0.3719972, 0.40875639, 0.06329474], [0.515574, 0.1637679, 0.56800529]]

    These numbers were used to generate crystal structures covering all 230
    space group types. They were determined empirically through trial and error.

    """
    crystal_systems = BaseGenerator.CRYSTAL_SYSTEMS

    points = [[0.3719972, 0.40875639, 0.06329474], [0.515574, 0.1637679, 0.56800529]]

    for crystal_system in crystal_systems:
        gm = BaseGenerator(crystal_system)
        gm.points = points
        gm.numbers = [1, 2]

        for spg_num in gm.crystal_system_class.get_spg_numbers():
            be = BaseExpander().set_structure(gm)
            be.read_symmetry_operations(spg_num)
            be.expand()
            bs = BaseStructure().set_structure(be)
            bs.find_symmetry_dataset(tol=tol)
            assert bs.space_group_number == spg_num
            _check_distance(bs)

            yield crystal_system, bs


def _check_distance(bs: BaseStructure):
    import numpy as np
    from phonopy.structure.cells import get_smallest_vectors

    svecs, _ = get_smallest_vectors(
        bs.lattice, bs.points, bs.points, store_dense_svecs=False, symprec=1e-5
    )
    distances = np.linalg.norm(svecs[:, :, 0] @ bs.lattice, axis=-1)
    distances += np.eye(svecs.shape[0]) * 100
    min_dist = np.min(distances)
    assert min_dist > 3e-1
    print(min_dist)
