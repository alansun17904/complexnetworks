from .context import models
import pytest


@pytest.fixture(scope='module')
def adj_matrix1():
    m = [[0, 1, 0],
         [1, 0, 1],
         [0, 1, 0]]
    return m


def test_deterministic_1(adj_matrix1):
    d = models.DeterministicGraph(0.4, [1], adj_matrix1)
    time_table = d.spread()
    assert len(time_table) == 1
    assert time_table[0][0] == 0
    assert time_table[0][1] == {1}


def test_deterministic_2(adj_matrix1):
    d = models.DeterministicGraph(0.5, [1], adj_matrix1)
    assert d.initialize_nodes() == 1
    time_table = d.spread()
    assert len(time_table) == 2
    assert time_table[0][0] == 0
    assert time_table[0][1] == {1}
    assert time_table[1][0] == 1
    assert 1 in time_table[1][1]
    assert 0 in time_table[1][1]
    assert 2 in time_table[1][1]

