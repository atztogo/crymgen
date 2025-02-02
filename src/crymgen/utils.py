"""Utility functions for crystal generation."""

import io
import os
import pathlib
from typing import Union

import numpy as np
import yaml

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


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


def get_io_module_to_decompress(filename):
    """Return io-module to decompress file.

    This function came from phonopy (BSD3 License).

    Filename extensions of lzma, xz, gzip, bz2 are supported.

    It is supported to use it like `returned_module.open(filename)`.

    """
    ext = pathlib.Path(filename).suffix
    if ext == ".xz" or ext == ".lzma":
        import lzma

        return lzma
    elif ext == ".gz":
        import gzip

        return gzip
    elif ext == ".bz2":
        import bz2

        return bz2
    else:
        import io

        return io


def load_yaml(fp: Union[str, bytes, os.PathLike, io.IOBase]):
    """Load yaml file.

    Parameters
    ----------
    fp : str, bytes, os.PathLike or io.IOBase
        Filename, file path, or file stream.

    lzma and gzip comppressed non-stream files can be loaded.

    """
    if isinstance(fp, io.IOBase):
        yaml_data = yaml.load(fp, Loader=Loader)
    else:
        myio = get_io_module_to_decompress(fp)
        with myio.open(fp) as f:
            yaml_data = yaml.load(f, Loader=Loader)

    return yaml_data
