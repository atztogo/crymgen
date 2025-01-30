"""Utility functions for crystal generation."""

import numpy as np


def get_cell_matrix(
    a: float,
    b: float,
    c: float,
    alpha: float,
    beta: float,
    gamma: float,
    is_radian=False,
) -> np.ndarray:
    """Return basis vectors in another orientation.

    This function came from phonopy (BSD3 License).

    Parameters
    ----------
    a, b, c : float
        Basis vector lengths.
    alpha, beta, gamm : float
        Angles between basis vectors in radian.

    Returns
    -------
    ndarray
        shape=(3, 3), dtype='double', order='C'.
        [[a_x,   0,   0],
        [b_x, b_y,   0],
        [c_x, c_y, c_z]]

    """
    if not is_radian:
        alpha *= np.pi / 180
        beta *= np.pi / 180
        gamma *= np.pi / 180
    b1 = np.cos(gamma)
    b2 = np.sin(gamma)
    b3 = 0.0
    c1 = np.cos(beta)
    c2 = (2 * np.cos(alpha) + b1**2 + b2**2 - 2 * b1 * c1 - 1) / (2 * b2)
    c3 = np.sqrt(1 - c1**2 - c2**2)
    lattice = np.zeros((3, 3), dtype="double", order="C")
    lattice[0, 0] = a
    lattice[1] = np.array([b1, b2, b3]) * b
    lattice[2] = np.array([c1, c2, c3]) * c
    return lattice
