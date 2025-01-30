"""Base classe for generating crystals."""

from __future__ import annotations

from typing import Literal, Sequence, TypeAlias, Union, get_args

import numpy as np

from crysgen.crystal_system import (
    Cubic,
    Hexagonal,
    Monoclinic,
    Orthorhombic,
    Tetragonal,
    Triclinic,
    Trigonal,
)

CrystalSystemLiteral: TypeAlias = Literal[
    "triclinic",
    "monoclinic",
    "orthorhombic",
    "tetragonal",
    "trigonal",
    "hexagonal",
    "cubic",
]


class BaseGenerator:
    """Base class for crystal generators."""

    _CRYSTAL_SYSTEMS: tuple[str] = tuple(get_args(CrystalSystemLiteral))

    def __init__(self, crystal_system: CrystalSystemLiteral):
        self.set_basis_vectors(crystal_system)

    @property
    def lattice(self):
        """Return lattice."""
        return self._lattice

    @property
    def points(self) -> np.ndarray:
        """Return points."""
        return self._points

    @points.setter
    def points(self, points: Union[np.ndarray, Sequence]):
        """Set points."""
        self._points = np.array(points, dtype=float)

    @property
    def numbers(self) -> np.ndarray:
        """Return atomic numbers."""
        return self._numbers

    @numbers.setter
    def numbers(self, numbers: Union[np.ndarray, Sequence]):
        """Set atomic numbers."""
        self._numbers = np.array(numbers, dtype=int)

    @property
    def dataset(self):
        """Return symmetry dataset."""
        return self._dataset

    def set_basis_vectors(self, crystal_system: CrystalSystemLiteral):
        """Set basis vectors.

        Basis vectors are represented by a 3x3 matrix in numpy array, and stored
        in self._lattice. Each row corresponds to a basis vector.

        """
        if crystal_system == "triclinic":
            lattice = Triclinic().lattice
        elif crystal_system == "monoclinic":
            lattice = Monoclinic().lattice
        elif crystal_system == "orthorhombic":
            lattice = Orthorhombic().lattice
        elif crystal_system == "tetragonal":
            lattice = Tetragonal().lattice
        elif crystal_system == "trigonal":
            lattice = Trigonal().lattice
        elif crystal_system == "hexagonal":
            lattice = Hexagonal().lattice
        elif crystal_system == "cubic":
            lattice = Cubic().lattice
        else:
            raise ValueError(f"Invalid crystal system: {crystal_system}")
        self._lattice = lattice

    def run_spglib(self) -> "BaseGenerator":
        """Run spglib."""
        from spglib import get_symmetry_dataset

        cell = (self._lattice, self._points, self._numbers)
        self._dataset = get_symmetry_dataset(cell)
        return self

    def __str__(self) -> str:
        """Return string representation."""
        if self.points is None:
            raise ValueError("Points are not set.")
        if self.numbers is None:
            raise ValueError("Atomic numbers are not set.")

        lines = ["unitcell:"]
        lines.append("  lattice:")
        for v in self.lattice:
            lines.append(f"  - [{v[0]:20.14f}, {v[1]:20.14f}, {v[2]:20.14f}]")
        lines.append("  points:")
        for num, v in zip(self.numbers, self.points, strict=True):
            lines.append(f"  - number: {num}")
            lines.append(
                f"    coordinates: [{v[0]:20.14f}, {v[1]:20.14f}, {v[2]:20.14f}]"
            )
        return "\n".join(lines)
