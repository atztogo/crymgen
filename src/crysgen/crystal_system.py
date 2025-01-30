"""Tools for crystal systems."""

from typing import Optional

import numpy as np

from crysgen.utils import get_cell_matrix


class BaseCrystalSystem:
    """Base class for crystal systems."""

    def __init__(
        self,
        a: Optional[float] = None,
        b: Optional[float] = None,
        c: Optional[float] = None,
        alpha: Optional[float] = None,
        beta: Optional[float] = None,
        gamma: Optional[float] = None,
    ):
        self._a = None
        self._b = None
        self._c = None
        self._alpha = None
        self._beta = None
        self._gamma = None
        self._set_a(a)
        self._set_b(b)
        self._set_c(c)
        self._set_alpha(alpha)
        self._set_beta(beta)
        self._set_gamma(gamma)

    @property
    def a(self) -> float:
        """Return the lattice parameter a."""
        return self._a

    @property
    def b(self) -> float:
        """Return the lattice parameter b."""
        return self._b

    @property
    def c(self) -> float:
        """Return the lattice parameter c."""
        return self._c

    @property
    def alpha(self) -> float:
        """Return the angle alpha."""
        return self._alpha

    @property
    def beta(self) -> float:
        """Return the angle beta."""
        return self._beta

    @property
    def gamma(self) -> float:
        """Return the angle gamma."""
        return self._gamma

    @property
    def lattice(self) -> np.ndarray:
        """Return basis vectors."""
        assert self.a is not None
        assert self.b is not None
        assert self.c is not None
        assert self.alpha is not None
        assert self.beta is not None
        assert self.gamma is not None
        return get_cell_matrix(
            self.a, self.b, self.c, self.alpha, self.beta, self.gamma
        )

    @classmethod
    def get_spg_numbers(self) -> tuple[int]:
        """Return the space group numbers."""
        return tuple(range(self._SPG_NUMBER_RANGE[0], self._SPG_NUMBER_RANGE[1]))

    def _set_a(self, a: float):
        self._a = float(a)

    def _set_b(self, b: float):
        self._b = float(b)

    def _set_c(self, c: float):
        self._c = float(c)

    def _set_alpha(self, alpha: float):
        self._alpha = float(alpha)

    def _set_beta(self, beta: float):
        self._beta = float(beta)

    def _set_gamma(self, gamma: float):
        self._gamma = float(gamma)


class Triclinic(BaseCrystalSystem):
    """Class for triclinic crystal system."""

    _DEFAULT_A = 10.0
    _DEFAULT_B_OVER_A = 1.1
    _DEFAULT_C_OVER_A = 1.2
    _DEFAULT_ALPHA = 103.0
    _DEFAULT_BETA_OVER_ALPHA = 1.1
    _DEFAULT_GAMMA_OVER_ALPHA = 1.2

    _SPG_NUMBER_RANGE = (1, 3)  # 1-2

    def __init__(
        self,
        a: Optional[float] = None,
        b: Optional[float] = None,
        c: Optional[float] = None,
        alpha: Optional[float] = None,
        beta: Optional[float] = None,
        gamma: Optional[float] = None,
    ):
        self._a = None
        self._b = None
        self._c = None
        self._alpha = None
        self._beta = None
        self._gamma = None
        if a is None:
            self._set_a(self._DEFAULT_A)
        else:
            self._set_a(a)
        if b is None:
            self._set_b(self._a * self._DEFAULT_B_OVER_A)
        else:
            self._set_b(b)
        if c is None:
            self._set_c(self._a * self._DEFAULT_C_OVER_A)
        else:
            self._set_c(c)
        if alpha is None:
            self._set_alpha(self._DEFAULT_ALPHA)
        else:
            self._set_alpha(alpha)
        if beta is None:
            self._set_beta(self._alpha * self._DEFAULT_BETA_OVER_ALPHA)
        else:
            self._set_beta(beta)
        if gamma is None:
            self._set_gamma(self._alpha * self._DEFAULT_GAMMA_OVER_ALPHA)
        else:
            self._set_gamma(gamma)


class Monoclinic(BaseCrystalSystem):
    """Class for monoclinic crystal system."""

    _DEFAULT_A = 10.0
    _DEFAULT_B_OVER_A = 1.1
    _DEFAULT_C_OVER_A = 1.2
    _DEFAULT_BETA_OVER_ALPHA = 1.1

    _SPG_NUMBER_RANGE = (3, 16)  # 3-15

    def __init__(
        self,
        a: Optional[float] = None,
        b: Optional[float] = None,
        c: Optional[float] = None,
        beta: Optional[float] = None,
    ):
        self._a = None
        self._b = None
        self._c = None
        self._alpha = None
        self._beta = None
        self._gamma = None
        if a is None:
            self._set_a(self._DEFAULT_A)
        else:
            self._set_a(a)
        if b is None:
            self._set_b(self._a * self._DEFAULT_B_OVER_A)
        else:
            self._set_b(b)
        if c is None:
            self._set_c(self._a * self._DEFAULT_C_OVER_A)
        else:
            self._set_c(c)
        self._set_alpha(90)
        if beta is None:
            self._set_beta(self._alpha * self._DEFAULT_BETA_OVER_ALPHA)
        else:
            self._set_beta(beta)
        self._set_gamma(90)


class Orthorhombic(BaseCrystalSystem):
    """Class for orthorhombic crystal system."""

    _DEFAULT_A = 10.0
    _DEFAULT_B_OVER_A = 1.1
    _DEFAULT_C_OVER_A = 1.2

    _SPG_NUMBER_RANGE = (16, 75)  # 16-74

    def __init__(
        self,
        a: Optional[float] = None,
        b: Optional[float] = None,
        c: Optional[float] = None,
    ):
        self._a = None
        self._b = None
        self._c = None
        self._alpha = None
        self._beta = None
        self._gamma = None
        if a is None:
            self._set_a(self._DEFAULT_A)
        else:
            self._set_a(a)
        if b is None:
            self._set_b(self._a * self._DEFAULT_B_OVER_A)
        else:
            self._set_b(b)
        if c is None:
            self._set_c(self._a * self._DEFAULT_C_OVER_A)
        else:
            self._set_c(c)
        self._set_alpha(90)
        self._set_beta(90)
        self._set_gamma(90)


class Tetragonal(BaseCrystalSystem):
    """Class for tetragonal crystal system."""

    _DEFAULT_A = 10.0
    _DEFAULT_C_OVER_A = 1.1

    _SPG_NUMBER_RANGE = (75, 143)  # 75-142

    def __init__(
        self,
        a: Optional[float] = None,
        c: Optional[float] = None,
    ):
        self._a = None
        self._b = None
        self._c = None
        self._alpha = None
        self._beta = None
        self._gamma = None
        if a is None:
            self._set_a(self._DEFAULT_A)
        else:
            self._set_a(a)
        self._set_b(self._a)
        if c is None:
            self._set_c(self._a * self._DEFAULT_C_OVER_A)
        else:
            self._set_c(c)
        self._set_alpha(90)
        self._set_beta(90)
        self._set_gamma(90)


class Trigonal(BaseCrystalSystem):
    """Class for trigonal crystal system."""

    _DEFAULT_A = 10.0
    _DEFAULT_C_OVER_A = 1.1

    _SPG_NUMBER_RANGE = (143, 168)  # 143-167

    def __init__(
        self,
        a: Optional[float] = None,
        c: Optional[float] = None,
    ):
        self._a = None
        self._b = None
        self._c = None
        self._alpha = None
        self._beta = None
        self._gamma = None
        if a is None:
            self._set_a(self._DEFAULT_A)
        else:
            self._set_a(a)
        self._set_b(self._a)
        if c is None:
            self._set_c(self._a * self._DEFAULT_C_OVER_A)
        else:
            self._set_c(c)
        self._set_alpha(90)
        self._set_beta(90)
        self._set_gamma(120)


class Hexagonal(BaseCrystalSystem):
    """Class for hexagonal crystal system."""

    _DEFAULT_A = 10.0
    _DEFAULT_C_OVER_A = 1.1

    _SPG_NUMBER_RANGE = (168, 195)  # 168-194

    def __init__(
        self,
        a: Optional[float] = None,
        c: Optional[float] = None,
    ):
        self._a = None
        self._b = None
        self._c = None
        self._alpha = None
        self._beta = None
        self._gamma = None
        if a is None:
            self._set_a(self._DEFAULT_A)
        else:
            self._set_a(a)
        self._set_b(self._a)
        if c is None:
            self._set_c(self._a * self._DEFAULT_C_OVER_A)
        else:
            self._set_c(c)
        self._set_alpha(90)
        self._set_beta(90)
        self._set_gamma(120)


class Cubic(BaseCrystalSystem):
    """Class for cubic crystal system."""

    _DEFAULT_A = 10.0

    _SPG_NUMBER_RANGE = (195, 231)  # 195-230

    def __init__(
        self,
        a: Optional[float] = None,
    ):
        self._a = None
        self._b = None
        self._c = None
        self._alpha = None
        self._beta = None
        self._gamma = None
        if a is None:
            self._set_a(self._DEFAULT_A)
        else:
            self._set_a(a)
        self._set_b(self._a)
        self._set_c(self._a)
        self._set_alpha(90)
        self._set_beta(90)
        self._set_gamma(90)
