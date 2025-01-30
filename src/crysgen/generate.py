"""Classes for generating elemental crystals."""

from __future__ import annotations

from typing import get_args

from crysgen.crystal_system import (
    BaseCrystalSystem,
    Cubic,
    Hexagonal,
    Monoclinic,
    Orthorhombic,
    Tetragonal,
    Triclinic,
    Trigonal,
)
from crysgen.structure import BaseStructure, CrystalSystemLiteral


class BaseGenerator(BaseStructure):
    """Base class for crystal generators."""

    CRYSTAL_SYSTEMS: tuple[str] = tuple(get_args(CrystalSystemLiteral))

    def __init__(self, crystal_system: CrystalSystemLiteral):
        super().__init__()
        self._crystal_system_class = None
        self.set_basis_vectors(crystal_system)

    @property
    def crystal_system_class(self):
        """Return crystal system class."""
        return self._crystal_system_class

    @crystal_system_class.setter
    def crystal_system_class(self, crystal_system_class: BaseCrystalSystem):
        """Set crystal system class."""
        self._crystal_system_class = crystal_system_class

    def set_basis_vectors(self, crystal_system: CrystalSystemLiteral):
        """Set basis vectors.

        Basis vectors are represented by a 3x3 matrix in numpy array, and stored
        in self._lattice. Each row corresponds to a basis vector.

        """
        if crystal_system == "triclinic":
            self._crystal_system_class = Triclinic
        elif crystal_system == "monoclinic":
            self._crystal_system_class = Monoclinic
        elif crystal_system == "orthorhombic":
            self._crystal_system_class = Orthorhombic
        elif crystal_system == "tetragonal":
            self._crystal_system_class = Tetragonal
        elif crystal_system == "trigonal":
            self._crystal_system_class = Trigonal
        elif crystal_system == "hexagonal":
            self._crystal_system_class = Hexagonal
        elif crystal_system == "cubic":
            self._crystal_system_class = Cubic
        else:
            raise ValueError(f"Invalid crystal system: {crystal_system}")
        self._lattice = self._crystal_system_class().lattice

    def set_structure(self, cell: BaseStructure) -> "BaseGenerator":
        """Set structure."""
        return self._set_structure(cell)
