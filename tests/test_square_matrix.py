from src.helper.square_matrix import square_matrix


def test_square_matrix_d_less_4():
    value = 'Matriz deve ter dimensão maior que 4!'
    assert square_matrix(3) == value
    assert square_matrix(2) == value
    assert square_matrix(1) == value


def test_square_matrix_4x4():
    d = 4
    value = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    assert square_matrix(d) == value


def test_square_matrix_8x8():
    d = 8
    value = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]]
    assert square_matrix(d) == value
