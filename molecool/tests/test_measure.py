"""
Unit and regression test for the measure module.
"""

import molecool
import numpy as np
import pytest

#@pytest.mark.skip    #It's a decorator, it causes the following test to be skipped
#@pytest.mark.slow You can make up your own decorators.

def test_calculate_distance():

        r1 = np.array([0, 0, 0])
        r2 = np.array([0, 1, 0])

        expected_distance = 1

        calculated_distance = molecool.calculate_distance(r1, r2)

        assert expected_distance == calculated_distance
#Useful to check a range of values. Parametrized mark.
@pytest.mark.parametrize(
    "r1, r2, r3, expected_angle",
    [
        (np.array([1, 0, 0]),np.array([0, 0, 0]),np.array([0, 1, 0]),90),
        (np.array([np.sqrt(2)/2]),np.array([np.sqrt(2)/2]), np.array([0, 0, 0]),45),
        (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60)
    ]
)
#The advantage is that we can give multiple arguments, and we can run all of them.
#@pytest.mark.parametrize(
#    "expected_angle",
#    [
#    90,
#    45,
#    60,
#    ]
#)
def test_calculate_angle(r1, r2, r3, expected_angle):

        calculated_angle = round(molecool.calculate_angle(r1, r2, r3), 3)
#The approx function is useful when you do numerical comparisons.
        assert pytest.approx(expected_angle, abs=1e-2) == calculated_angle

def test_molecular_mass():

    symbols = ['C','H','H','H','H']
    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = 16.04

    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass
