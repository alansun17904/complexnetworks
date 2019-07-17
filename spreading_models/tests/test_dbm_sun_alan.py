from spreading_models.tests.context import *
import pytest


def test_read_graph():
    m = models.read_graph('../data/dbm_graded_input.txt')
    assert len(m) == 4
    assert m[0] == 15
    assert m[1] == 0.1
    assert m[2] == [0, 4, 6, 8]
    assert len(m[3]) == 22


def test_read_graph2():
    m = models.read_graph('../data/dbm_graded_input2.txt')
    assert len(m) == 4
    assert m[0] == 15
    assert m[1] == 0.1
    assert m[2] == [1, 12, 14]
    assert len(m[3]) == 23


def test_make_adj_matrix():
    g = models.read_graph('../data/dbm_graded_input.txt')
    adj = models.make_adj_matrix(g[0], g[3])
    assert len(adj) == 15  # test matrix dimensions 15 x 15
    for row in adj:
        assert len(row) == 15
    # no self loops
    for row in range(len(adj)):
        assert adj[row][row] == 0


def test_make_adj_matrix2():
    g = models.read_graph('../data/dbm_graded_input2.txt')
    adj = models.make_adj_matrix(g[0], g[3])
    assert len(adj) == 15  # test matrix dimensions 15 x 15
    for row in adj:
        assert len(row) == 15
    # no self loops
    for row in range(len(adj)):
        assert adj[row][row] == 0
