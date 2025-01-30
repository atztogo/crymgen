"""Test for crystal system classes."""

import pytest

from crysgen.crystal_system import (
    Cubic,
    Hexagonal,
    Monoclinic,
    Orthorhombic,
    Tetragonal,
    Triclinic,
)


def test_triclinic():
    """Test triclinic crystal system."""
    triclinic = Triclinic(a=1, b=2, c=3, alpha=90, beta=95, gamma=100)
    assert triclinic.a == pytest.approx(1)
    assert triclinic.b == pytest.approx(2)
    assert triclinic.c == pytest.approx(3)
    assert triclinic.alpha == pytest.approx(90)
    assert triclinic.beta == pytest.approx(95)
    assert triclinic.gamma == pytest.approx(100)


def test_triclinic_default():
    """Test triclinic crystal system with default values."""
    triclinic = Triclinic()
    assert triclinic.a == pytest.approx(10)
    assert triclinic.b == pytest.approx(11)
    assert triclinic.c == pytest.approx(12)
    assert triclinic.alpha == pytest.approx(103)
    assert triclinic.beta == pytest.approx(113.3)
    assert triclinic.gamma == pytest.approx(123.6)


def test_monoclinic():
    """Test monoclinic crystal system."""
    monoclinic = Monoclinic(a=1, b=2, c=3, beta=95)
    assert monoclinic.a == pytest.approx(1)
    assert monoclinic.b == pytest.approx(2)
    assert monoclinic.c == pytest.approx(3)
    assert monoclinic.alpha == pytest.approx(90)
    assert monoclinic.beta == pytest.approx(95)
    assert monoclinic.gamma == pytest.approx(90)


def test_monoclinic_default():
    """Test monoclinic crystal system with default values."""
    monoclinic = Monoclinic()
    assert monoclinic.a == pytest.approx(10)
    assert monoclinic.b == pytest.approx(11)
    assert monoclinic.c == pytest.approx(12)
    assert monoclinic.alpha == pytest.approx(90)
    assert monoclinic.beta == pytest.approx(99)
    assert monoclinic.gamma == pytest.approx(90)


def test_orthorhombic():
    """Test orthorhombic crystal system."""
    orthorhombic = Orthorhombic(a=1, b=2, c=3)
    assert orthorhombic.a == pytest.approx(1)
    assert orthorhombic.b == pytest.approx(2)
    assert orthorhombic.c == pytest.approx(3)


def test_orthorhombic_default():
    """Test orthorhombic crystal system with default values."""
    orthorhombic = Orthorhombic()
    assert orthorhombic.a == pytest.approx(10)
    assert orthorhombic.b == pytest.approx(11)
    assert orthorhombic.c == pytest.approx(12)


def test_tetragonal():
    """Test tetragonal crystal system."""
    tetragonal = Tetragonal(a=1, c=3)
    assert tetragonal.a == pytest.approx(1)
    assert tetragonal.b == pytest.approx(1)
    assert tetragonal.c == pytest.approx(3)


def test_tetragonal_default():
    """Test tetragonal crystal system with default values."""
    tetragonal = Tetragonal()
    assert tetragonal.a == pytest.approx(10)
    assert tetragonal.b == pytest.approx(10)
    assert tetragonal.c == pytest.approx(11)


def test_hexagonal():
    """Test hexagonal crystal system."""
    hexagonal = Hexagonal(a=1, c=3)
    assert hexagonal.a == pytest.approx(1)
    assert hexagonal.b == pytest.approx(1)
    assert hexagonal.c == pytest.approx(3)


def test_hexagonal_default():
    """Test hexagonal crystal system with default values."""
    hexagonal = Hexagonal()
    assert hexagonal.a == pytest.approx(10)
    assert hexagonal.b == pytest.approx(10)
    assert hexagonal.c == pytest.approx(11)


def test_cubic():
    """Test cubic crystal system."""
    cubic = Cubic(a=1)
    assert cubic.a == pytest.approx(1)
    assert cubic.b == pytest.approx(1)
    assert cubic.c == pytest.approx(1)


def test_cubic_default():
    """Test cubic crystal system with default values."""
    cubic = Cubic()
    assert cubic.a == pytest.approx(10)
    assert cubic.b == pytest.approx(10)
    assert cubic.c == pytest.approx(10)
