from src.generate_matrix import generate_matrix


def test_matrix_4x4_1():
    value = 1
    lines = 4
    columns = 4
    matrix_result = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    assert generate_matrix(value, lines, columns) == matrix_result


def test_matrix_4x4_0():
    value = 0
    lines = 4
    columns = 4
    matrix_result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert generate_matrix(value, lines, columns) == matrix_result


def test_matrix_5x4_1():
    value = 1
    lines = 5
    columns = 4
    matrix_result = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],
                     [1, 1, 1, 1]]
    assert generate_matrix(value, lines, columns) == matrix_result


def test_matrix_4x5_1():
    value = 1
    lines = 4
    columns = 5
    matrix_result = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],
                     [1, 1, 1, 1]]
    assert generate_matrix(value, lines, columns) == matrix_result
