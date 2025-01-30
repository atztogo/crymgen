"""Classes for generating elemental crystals."""

from __future__ import annotations

from crysgen.structure import BaseGenerator, CrystalSystemLiteral


class GenElemental(BaseGenerator):
    """Class for generating elemental crystals."""

    def __init__(self, crystal_system: CrystalSystemLiteral):
        super().__init__(crystal_system)
