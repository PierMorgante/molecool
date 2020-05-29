"""
Unit and regression test for the measure module.
"""

import molecool
import numpy as np
import pytest

#@pytest.fixture(scope="module") #This feature is used once and the results are used every time.
#It does not re-run the code. Another scope is "session", or simply without anything.
def methane_molecule():
    symbols = ['C','H','H','H','H']
    coordinates = np.array([
    [1, 1, 1],
    [2.4, 1, 1],
    [-0.4, 1, 1],
    [1, 1, 2.4],
    [1, 1, 0.4],
    ])
    return symbols, coordinates

def test_move_methane(methane_molecule):
    symbols, coordinates = methane_molecule

    coordinates[0] += 5


def test_build_bond_failure():

    coordinates = np.array([
    [1, 1, 1],
    [2.4, 1, 1],
    [-0.4, 1, 1],
    [1, 1, 2.4],
    [1, 1, 0.4],
    ])
    with pytest.raises(ValueError):
        bonds = molecool.build_bond_list(coordinates, min_bond=-1)

def test_molecular_mass(methane_molecule):

    symbols, coordinates = methane_molecule

    calculated_mass = molecool.calculate_molecular_mass(symbols)
    actual_mass = 16.04

    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass
