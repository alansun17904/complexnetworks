from hw9.p2_sun_alan_id33 import unique_squares_one_player, unique_squares_two_players


def test_unique_squares_one_player():
    assert unique_squares_one_player("w") == 1
    assert unique_squares_one_player("a") == 1
    assert unique_squares_one_player("s") == 1
    assert unique_squares_one_player("d") == 1
    assert unique_squares_one_player("wa") == 2
    assert unique_squares_one_player("waw") == 3
    assert unique_squares_one_player("wasd") == 4
    assert unique_squares_one_player("waadsdw") == 5


def test_unique_squares_two_players():
    assert unique_squares_two_players("ws") == 2
    assert unique_squares_two_players("wasd") == 3

