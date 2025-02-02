"""Base classe for generating crystals."""

from __future__ import annotations

import io
import os
from typing import Literal, Optional, Sequence, TypeAlias, Union

import numpy as np

from crymgen.utils import load_yaml

CrystalSystemLiteral: TypeAlias = Literal[
    "triclinic",
    "monoclinic",
    "orthorhombic",
    "tetragonal",
    "trigonal",
    "hexagonal",
    "cubic",
]

spg_to_hallnum = {
    1: 1,
    2: 2,
    3: 3,
    # 3: 4,
    # 3: 5,
    4: 6,
    # 4: 7,
    # 4: 8,
    5: 9,
    # 5: 10,
    # 5: 11,
    # 5: 12,
    # 5: 13,
    # 5: 14,
    # 5: 15,
    # 5: 16,
    # 5: 17,
    6: 18,
    # 6: 19,
    # 6: 20,
    7: 21,
    # 7: 22,
    # 7: 23,
    # 7: 24,
    # 7: 25,
    # 7: 26,
    # 7: 27,
    # 7: 28,
    # 7: 29,
    8: 30,
    # 8: 31,
    # 8: 32,
    # 8: 33,
    # 8: 34,
    # 8: 35,
    # 8: 36,
    # 8: 37,
    # 8: 38,
    9: 39,
    # 9: 40,
    # 9: 41,
    # 9: 42,
    # 9: 43,
    # 9: 44,
    # 9: 45,
    # 9: 46,
    # 9: 47,
    # 9: 48,
    # 9: 49,
    # 9: 50,
    # 9: 51,
    # 9: 52,
    # 9: 53,
    # 9: 54,
    # 9: 55,
    # 9: 56,
    10: 57,
    # 10: 58,
    # 10: 59,
    11: 60,
    # 11: 61,
    # 11: 62,
    12: 63,
    # 12: 64,
    # 12: 65,
    # 12: 66,
    # 12: 67,
    # 12: 68,
    # 12: 69,
    # 12: 70,
    # 12: 71,
    13: 72,
    # 13: 73,
    # 13: 74,
    # 13: 75,
    # 13: 76,
    # 13: 77,
    # 13: 78,
    # 13: 79,
    # 13: 80,
    14: 81,
    # 14: 82,
    # 14: 83,
    # 14: 84,
    # 14: 85,
    # 14: 86,
    # 14: 87,
    # 14: 88,
    # 14: 89,
    15: 90,
    # 15: 91,
    # 15: 92,
    # 15: 93,
    # 15: 94,
    # 15: 95,
    # 15: 96,
    # 15: 97,
    # 15: 98,
    # 15: 99,
    # 15: 100,
    # 15: 101,
    # 15: 102,
    # 15: 103,
    # 15: 104,
    # 15: 105,
    # 15: 106,
    # 15: 107,
    16: 108,
    17: 109,
    # 17: 110,
    # 17: 111,
    18: 112,
    # 18: 113,
    # 18: 114,
    19: 115,
    20: 116,
    # 20: 117,
    # 20: 118,
    21: 119,
    # 21: 120,
    # 21: 121,
    22: 122,
    23: 123,
    24: 124,
    25: 125,
    # 25: 126,
    # 25: 127,
    26: 128,
    # 26: 129,
    # 26: 130,
    # 26: 131,
    # 26: 132,
    # 26: 133,
    27: 134,
    # 27: 135,
    # 27: 136,
    28: 137,
    # 28: 138,
    # 28: 139,
    # 28: 140,
    # 28: 141,
    # 28: 142,
    29: 143,
    # 29: 144,
    # 29: 145,
    # 29: 146,
    # 29: 147,
    # 29: 148,
    30: 149,
    # 30: 150,
    # 30: 151,
    # 30: 152,
    # 30: 153,
    # 30: 154,
    31: 155,
    # 31: 156,
    # 31: 157,
    # 31: 158,
    # 31: 159,
    # 31: 160,
    32: 161,
    # 32: 162,
    # 32: 163,
    33: 164,
    # 33: 165,
    # 33: 166,
    # 33: 167,
    # 33: 168,
    # 33: 169,
    34: 170,
    # 34: 171,
    # 34: 172,
    35: 173,
    # 35: 174,
    # 35: 175,
    36: 176,
    # 36: 177,
    # 36: 178,
    # 36: 179,
    # 36: 180,
    # 36: 181,
    37: 182,
    # 37: 183,
    # 37: 184,
    38: 185,
    # 38: 186,
    # 38: 187,
    # 38: 188,
    # 38: 189,
    # 38: 190,
    39: 191,
    # 39: 192,
    # 39: 193,
    # 39: 194,
    # 39: 195,
    # 39: 196,
    40: 197,
    # 40: 198,
    # 40: 199,
    # 40: 200,
    # 40: 201,
    # 40: 202,
    41: 203,
    # 41: 204,
    # 41: 205,
    # 41: 206,
    # 41: 207,
    # 41: 208,
    42: 209,
    # 42: 210,
    # 42: 211,
    43: 212,
    # 43: 213,
    # 43: 214,
    44: 215,
    # 44: 216,
    # 44: 217,
    45: 218,
    # 45: 219,
    # 45: 220,
    46: 221,
    # 46: 222,
    # 46: 223,
    # 46: 224,
    # 46: 225,
    # 46: 226,
    47: 227,
    48: 228,
    # 48: 229,
    49: 230,
    # 49: 231,
    # 49: 232,
    50: 233,
    # 50: 234,
    # 50: 235,
    # 50: 236,
    # 50: 237,
    # 50: 238,
    51: 239,
    # 51: 240,
    # 51: 241,
    # 51: 242,
    # 51: 243,
    # 51: 244,
    52: 245,
    # 52: 246,
    # 52: 247,
    # 52: 248,
    # 52: 249,
    # 52: 250,
    53: 251,
    # 53: 252,
    # 53: 253,
    # 53: 254,
    # 53: 255,
    # 53: 256,
    54: 257,
    # 54: 258,
    # 54: 259,
    # 54: 260,
    # 54: 261,
    # 54: 262,
    55: 263,
    # 55: 264,
    # 55: 265,
    56: 266,
    # 56: 267,
    # 56: 268,
    57: 269,
    # 57: 270,
    # 57: 271,
    # 57: 272,
    # 57: 273,
    # 57: 274,
    58: 275,
    # 58: 276,
    # 58: 277,
    59: 278,
    # 59: 279,
    # 59: 280,
    # 59: 281,
    # 59: 282,
    # 59: 283,
    60: 284,
    # 60: 285,
    # 60: 286,
    # 60: 287,
    # 60: 288,
    # 60: 289,
    61: 290,
    # 61: 291,
    62: 292,
    # 62: 293,
    # 62: 294,
    # 62: 295,
    # 62: 296,
    # 62: 297,
    63: 298,
    # 63: 299,
    # 63: 300,
    # 63: 301,
    # 63: 302,
    # 63: 303,
    64: 304,
    # 64: 305,
    # 64: 306,
    # 64: 307,
    # 64: 308,
    # 64: 309,
    65: 310,
    # 65: 311,
    # 65: 312,
    66: 313,
    # 66: 314,
    # 66: 315,
    67: 316,
    # 67: 317,
    # 67: 318,
    # 67: 319,
    # 67: 320,
    # 67: 321,
    68: 322,
    # 68: 323,
    # 68: 324,
    # 68: 325,
    # 68: 326,
    # 68: 327,
    # 68: 328,
    # 68: 329,
    # 68: 330,
    # 68: 331,
    # 68: 332,
    # 68: 333,
    69: 334,
    70: 335,
    # 70: 336,
    71: 337,
    72: 338,
    # 72: 339,
    # 72: 340,
    73: 341,
    # 73: 342,
    74: 343,
    # 74: 344,
    # 74: 345,
    # 74: 346,
    # 74: 347,
    # 74: 348,
    75: 349,
    76: 350,
    77: 351,
    78: 352,
    79: 353,
    80: 354,
    81: 355,
    82: 356,
    83: 357,
    84: 358,
    85: 359,
    # 85: 360,
    86: 361,
    # 86: 362,
    87: 363,
    88: 364,
    # 88: 365,
    89: 366,
    90: 367,
    91: 368,
    92: 369,
    93: 370,
    94: 371,
    95: 372,
    96: 373,
    97: 374,
    98: 375,
    99: 376,
    100: 377,
    101: 378,
    102: 379,
    103: 380,
    104: 381,
    105: 382,
    106: 383,
    107: 384,
    108: 385,
    109: 386,
    110: 387,
    111: 388,
    112: 389,
    113: 390,
    114: 391,
    115: 392,
    116: 393,
    117: 394,
    118: 395,
    119: 396,
    120: 397,
    121: 398,
    122: 399,
    123: 400,
    124: 401,
    125: 402,
    # 125: 403,
    126: 404,
    # 126: 405,
    127: 406,
    128: 407,
    129: 408,
    # 129: 409,
    130: 410,
    # 130: 411,
    131: 412,
    132: 413,
    133: 414,
    # 133: 415,
    134: 416,
    # 134: 417,
    135: 418,
    136: 419,
    137: 420,
    # 137: 421,
    138: 422,
    # 138: 423,
    139: 424,
    140: 425,
    141: 426,
    # 141: 427,
    142: 428,
    # 142: 429,
    143: 430,
    144: 431,
    145: 432,
    146: 433,
    # 146: 434,
    147: 435,
    148: 436,
    # 148: 437,
    149: 438,
    150: 439,
    151: 440,
    152: 441,
    153: 442,
    154: 443,
    155: 444,
    # 155: 445,
    156: 446,
    157: 447,
    158: 448,
    159: 449,
    160: 450,
    # 160: 451,
    161: 452,
    # 161: 453,
    162: 454,
    163: 455,
    164: 456,
    165: 457,
    166: 458,
    # 166: 459,
    167: 460,
    # 167: 461,
    168: 462,
    169: 463,
    170: 464,
    171: 465,
    172: 466,
    173: 467,
    174: 468,
    175: 469,
    176: 470,
    177: 471,
    178: 472,
    179: 473,
    180: 474,
    181: 475,
    182: 476,
    183: 477,
    184: 478,
    185: 479,
    186: 480,
    187: 481,
    188: 482,
    189: 483,
    190: 484,
    191: 485,
    192: 486,
    193: 487,
    194: 488,
    195: 489,
    196: 490,
    197: 491,
    198: 492,
    199: 493,
    200: 494,
    201: 495,
    # 201: 496,
    202: 497,
    203: 498,
    # 203: 499,
    204: 500,
    205: 501,
    206: 502,
    207: 503,
    208: 504,
    209: 505,
    210: 506,
    211: 507,
    212: 508,
    213: 509,
    214: 510,
    215: 511,
    216: 512,
    217: 513,
    218: 514,
    219: 515,
    220: 516,
    221: 517,
    222: 518,
    # 222: 519,
    223: 520,
    224: 521,
    # 224: 522,
    225: 523,
    226: 524,
    227: 525,
    # 227: 526,
    228: 527,
    # 228: 528,
    229: 529,
    230: 530,
}


class BaseStructure:
    """Base class for crystal structures."""

    def __init__(self):
        self._lattice = None
        self._points = None
        self._numbers = None
        self._dataset = None
        self._space_group_number = None

    @property
    def lattice(self):
        """Return lattice."""
        return self._lattice

    @lattice.setter
    def lattice(self, lattice: Union[np.ndarray, Sequence]):
        """Set lattice."""
        self._lattice = np.array(lattice, dtype=float)

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

    @property
    def space_group_number(self) -> Optional[int]:
        """Return space group number."""
        return self._space_group_number

    @space_group_number.setter
    def space_group_number(self, spg_num: int):
        """Set space group number."""
        if self.dataset and self.dataset.number != spg_num:
            raise ValueError("Space group number is not consistent with the dataset.")
        self._space_group_number = spg_num

    def find_symmetry_dataset(self, tol: float = 1e-5) -> "BaseStructure":
        """Run spglib."""
        from spglib import get_symmetry_dataset

        cell = (self._lattice, self._points, self._numbers)
        self._dataset = get_symmetry_dataset(cell, symprec=tol)
        self.space_group_number = self._dataset.number
        return self

    def load_structure(
        self, fp: Union[str, bytes, os.PathLike, io.IOBase]
    ) -> "BaseStructure":
        """Load structure in yaml format."""
        yaml_data = load_yaml(fp)
        unitcell_dict = yaml_data["unitcell"]
        if "space_group" in yaml_data:
            space_group_dict = yaml_data["space_group"]
            self.space_group_number = space_group_dict["number"]

        self.lattice = unitcell_dict["lattice"]
        points = []
        numbers = []
        for data in unitcell_dict["points"]:
            points.append(data["coordinates"])
            numbers.append(data["number"])
        self.points = points
        self.numbers = numbers
        return self

    def __str__(self) -> str:
        """Return string representation."""
        if self.points is None:
            raise ValueError("Points are not set.")
        if self.numbers is None:
            raise ValueError("Atomic numbers are not set.")

        lines = []

        if self._dataset and self._dataset.number:
            lines.append("space_group:")
            lines.append(f"  number: {self._dataset.number}")
            lines.append("")

        lines.append("unitcell:")
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

    def set_structure(self, structure: BaseStructure) -> "BaseStructure":
        """Set structure."""
        self._lattice = structure.lattice
        self._points = structure.points
        self._numbers = structure.numbers
        return self


class BaseExpander(BaseStructure):
    """Base class for expanding structures."""

    def __init__(self):
        super().__init__()

    def expand(self, tol: float = 1e-3):
        """Expand the cell by symmetry operations."""
        if self._dataset is None:
            raise ValueError("Symmetry dataset is not set. Execute run_spglib() first.")

        points = self.points.copy()
        numbers = self.numbers.copy()

        for r, t in zip(
            self._dataset["rotations"], self._dataset["translations"], strict=True
        ):
            new_points = np.dot(self._points, r.T) + t
            for npt, num in zip(new_points, self._numbers, strict=True):
                diff = points - npt
                diff -= np.rint(diff)
                dist = np.linalg.norm(diff @ self._lattice, axis=1)
                overlap_idx = np.where(dist < tol)[0]
                if len(overlap_idx) == 0:
                    points = np.vstack((points, [npt]))
                    numbers = np.hstack((numbers, num))
                else:
                    for oid in overlap_idx:
                        if numbers[oid] != num:
                            raise ValueError("Some broken symmetry found.")

        self.points = points
        self.numbers = numbers

    def set_structure(self, structure: BaseStructure) -> "BaseExpander":
        """Set structure."""
        super().set_structure(structure)
        return self

    def read_symmetry_operations(self, spg_num: int):
        """Run spglib."""
        from spglib import get_symmetry_from_database

        self._dataset = get_symmetry_from_database(spg_to_hallnum[spg_num])


def isclose(
    a: BaseStructure,
    b: BaseStructure,
    rtol: float = 1e-5,
    atol: float = 1e-8,
) -> bool:
    """Check equivalence of two structures.

    Parameters
    ----------
    a : BaseStructure
        Reference cell.
    b : BaseStructure
        Cell to be compared.
    rtol : float, optional
        Relative tolerance in Cartesian coordinates. Default is 1e-5.
    atol : float, optional
        Tolerance in Cartesian distance. Default is 1e-8.

    """
    if len(a) != len(b):
        return False

    if not np.allclose(a.lattice, b.lattice, rtol=rtol, atol=atol):
        return False

    if (a.numbers != b.numbers).any():
        return False

    diff = a.points - b.points
    diff -= np.rint(diff)
    dist = np.sqrt((np.dot(diff, a.lattice) ** 2).sum(axis=1))
    if (dist > atol).any():
        return False

    return True
