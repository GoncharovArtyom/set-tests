from random import randrange, randint
from typing import List

import pytest

N_TESTS = 10
N_ELEMS = 10


@pytest.mark.parametrize("values", [[randint(0, 100) for _ in range(N_ELEMS)] for _ in range(N_TESTS)])
def test_creation(values: List[int]):
    data = set(values)

    assert len(data) <= len(values)
    for value in values:
        assert value in data


@pytest.mark.parametrize("value", [randint(0, 100) for _ in range(N_TESTS)])
def test_add(value: int):
    data = set()

    data.add(value)

    assert value in data


@pytest.mark.parametrize("ind", [randrange(N_ELEMS) for _ in range(N_TESTS)])
def test_remove(ind: int):
    values = [randint(0, 100) for _ in range(N_ELEMS)]
    value = values[ind]
    data = set(values)

    data.remove(value)

    assert value not in data


def test_union():

    values1 = [randint(0, 100) for _ in range(N_ELEMS)]
    values2 = [randint(0, 100) for _ in range(N_ELEMS)]

    data = set(values1) | set(values2)

    assert all(value in data for value in values1)
    assert all(value in data for value in values2)


def test_difference():
    values1 = [randint(0, 100) for _ in range(N_ELEMS)]
    values2 = [randint(0, 100) for _ in range(N_ELEMS)]

    data = set(values1) - set(values2)

    assert all(value in data or value in values2 for value in values1)
    assert all(value not in data for value in values2)


def test_clear():
    data = set([randint(0, 100) for _ in range(N_ELEMS)])

    data.clear()

    assert not data


def test_disjoint():
    data1 = set([randint(0, 49) for _ in range(N_ELEMS)])
    data2 = set([randint(50, 100) for _ in range(N_ELEMS)])

    assert data1.isdisjoint(data2)
