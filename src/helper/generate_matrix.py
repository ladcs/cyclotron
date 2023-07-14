from functools import partial


def generate_matrix(value, n_columns, n_lines):
    columns = [value] * n_lines
    return [columns] * n_columns


if __name__ == '__main__':
    lines = 4
    matrix_nxn = partial(generate_matrix, 0, lines)
    print(matrix_nxn(lines))
