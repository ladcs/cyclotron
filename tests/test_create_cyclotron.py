from src.helper.create_cyclotron import create_cyclotron


def test_less_4_lines_create_cyclotron():
    value = 'A matriz deve ter pelo menos 4 linhas!'
    matrix1 = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    matrix2 = [[1, 1, 1, 1], [1, 1, 1, 1]]
    matrix3 = [[1, 1, 1, 1]]
    assert create_cyclotron(matrix=matrix1) == value
    assert create_cyclotron(matrix=matrix2) == value
    assert create_cyclotron(matrix=matrix3) == value


def test_less_4_rows_create_cyclotron():
    value = 'A matriz deve ter pelo menos 4 colunas!'
    matrix1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    matrix2 = [[1, 1], [1, 1], [1, 1], [1, 1]]
    matrix3 = [[1], [1], [1], [1]]
    assert create_cyclotron(matrix=matrix1) == value
    assert create_cyclotron(matrix=matrix2) == value
    assert create_cyclotron(matrix=matrix3) == value


def test_is_not_particle():
    value = "Não é particula!"
    matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    particle1 = 1
    particle2 = 'a'
    assert create_cyclotron(particle=particle1, matrix=matrix) == value
    assert create_cyclotron(particle=particle2, matrix=matrix) == value


def test_without_particle():
    matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    assert create_cyclotron(matrix=matrix) == matrix


def test_particle_in_cyclotron():
    particle1 = 'n'
    particle2 = 'e'
    particle3 = 'p'
    matrix1 = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    matrix2 = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    matrix3 = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    matrix4 = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
    value1 = [['n', 'n', 'n', 'n'], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    value2 = [['e', 'e', 'e', 'e'], [1, 1, 1, 'e'], [1, 1, 1, 'e'],
              [1, 1, 1, 'e']]
    value3 = [['p', 'p', 'p', 'p'], ['p', 1, 1, 'p'], ['p', 1, 'p', 'p'],
              ['p', 'p', 'p', 1]]
    value4 = [['p', 'p', 'p', 'p', 'p', 'p'], ['p', 1, 1, 1, 1, 'p'],
              ['p', 1, 1, 1, 1, 'p'], ['p', 1, 1, 1, 1, 'p'],
              ['p', 1, 1, 1, 'p', 'p'], ['p', 'p', 'p', 'p', 'p', 1]]
    assert create_cyclotron(particle=particle1, matrix=matrix1) == value1
    assert create_cyclotron(particle=particle2, matrix=matrix2) == value2
    assert create_cyclotron(particle=particle3, matrix=matrix3) == value3
    assert create_cyclotron(particle=particle3, matrix=matrix4) == value4
