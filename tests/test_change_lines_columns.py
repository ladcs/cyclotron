from src.change_lines_columns import change_line
from src.change_lines_columns import change_column


def test_first_line_matrix_4x4():
    matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    matrix_result = [['e', 'e', 'e', 'e'], [1, 1, 1, 1], [1, 1, 1, 1],
                     [1, 1, 1, 1]]
    assert change_line('e', matrix) == matrix_result


def test_first_line_matrix_4x3():
    matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    matrix_result = [['e', 'e', 'e'], [1, 1, 1], [1, 1, 1],
                     [1, 1, 1]]
    assert change_line('e', matrix) == matrix_result


def test_first_line_matrix_3x4():
    matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    matrix_result = [['e', 'e', 'e', 'e'], [1, 1, 1, 1], [1, 1, 1, 1]]
    assert change_line('e', matrix) == matrix_result


def test_line_with_p_matrix_4x4():
    matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    matrix_result = [['p', 'p', 'p', 'p'], [1, 1, 1, 1], [1, 1, 1, 1],
                     ['p', 'p', 'p', 'p']]
    assert change_line('p', matrix) == matrix_result


def test_line_with_p_matrix_4x3():
    matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    matrix_result = [['p', 'p', 'p'], [1, 1, 1], [1, 1, 1],
                     ['p', 'p', 'p']]
    assert change_line('p', matrix) == matrix_result


def test_first_columns_matrix_4x4():
    matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    matrix_result = [[1, 1, 1, 'e'], [1, 1, 1, 'e'], [1, 1, 1, 'e'],
                     [1, 1, 1, 'e']]
    assert change_column('e', matrix) == matrix_result


def test_first_columns_matrix_4x3():
    matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    matrix_result = [[1, 1, 'e'], [1, 1, 'e'], [1, 1, 'e'],
                     [1, 1, 'e']]
    assert change_column('e', matrix) == matrix_result


def test_first_columns_matrix_3x4():
    matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    matrix_result = [[1, 1, 1, 'e'], [1, 1, 1, 'e'], [1, 1, 1, 'e']]
    assert change_column('e', matrix) == matrix_result


def test_columns_with_p_matrix_4x4():
    matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    matrix_result = [['p', 1, 1, 'p'], ['p', 1, 1, 'p'], ['p', 1, 'p', 'p'],
                     ['p', 1, 1, 1]]
    assert change_column('p', matrix) == matrix_result


def test_columns_with_p_matrix_4x3():
    matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    matrix_result = [['p', 1, 'p'], ['p', 1, 'p'], ['p', 'p', 'p'],
                     ['p', 1, 1]]
    assert change_column('p', matrix) == matrix_result


def test_columns_with_p_matrix_3x4():
    matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    matrix_result = [['p', 1, 1, 'p'], ['p', 1, 'p', 'p'], ['p', 1, 1, 1]]
    assert change_column('p', matrix) == matrix_result
