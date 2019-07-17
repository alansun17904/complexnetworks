from hw9.p1_sun_alan_id33 import final_floor, first_basement, visited_three_times, kudos
import pytest


def test_final_floor():
    assert final_floor(']') == -1
    assert final_floor('[]') == 0
    assert final_floor('[') == 1
    assert final_floor(']][[') == final_floor('][][')
    assert final_floor(']][') == final_floor('][]][[]')
    assert final_floor(']]]][[[]]]][[[]]]][[[') == -3


def test_first_basement():
    assert first_basement('[]]') == 3
    assert first_basement('[[[][]]]]') == 9
    assert final_floor(']]]]]][[[') == -3


def test_visited_three_times():
    assert visited_three_times('[][][]') == 0
    assert visited_three_times('[[]][][]') == 1


def test_kudos():
    pass
    # assert len(kudos()) == 2
    # assert len(kudos()[0]) == 10000
    # assert len(kudos()[1]) == 3