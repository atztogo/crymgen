"""Pytest conftest.py."""

from __future__ import annotations

import pytest


def pytest_addoption(parser):
    """Add option to generate data."""
    parser.addoption(
        "--gendata",
        action="store_true",
        default=False,
        help="Generate crystal structure data",
    )


def pytest_configure(config):
    """Add markers for generating data."""
    config.addinivalue_line("markers", "gendata: mark test as generating data")


def pytest_collection_modifyitems(config, items):
    """Skip slow tests if not running slow tests."""
    if config.getoption("--gendata"):
        return
    skip_gendata = pytest.mark.skip(reason="need --gendata option to run")
    for item in items:
        if "gendata" in item.keywords:
            item.add_marker(skip_gendata)
