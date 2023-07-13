from src.square_matrix import square_matrix


def test_square_matrix_3x3():
    d = 3
    value = 'Matrix deve ter dimensão maior que 4!'
    assert square_matrix(d) is value


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
