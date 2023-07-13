from src.change_lines_columns import change_first_line


def test_first_line_matrix_4x4():
    matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    matrix_result = [['e', 'e', 'e', 'e'], [1, 1, 1, 1], [1, 1, 1, 1],
                     [1, 1, 1, 1]]
    assert change_first_line('e', matrix) == matrix_result


def test_first_line_matrix_4x3():
    matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    matrix_result = [['e', 'e', 'e'], [1, 1, 1], [1, 1, 1],
                     [1, 1, 1]]
    assert change_first_line('e', matrix) == matrix_result


def test_first_line_matrix_3x4():
    matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    matrix_result = [['e', 'e', 'e', 'e'], [1, 1, 1, 1], [1, 1, 1, 1]]
    assert change_first_line('e', matrix) == matrix_result
