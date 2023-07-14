from .square_matrix import square_matrix
from .change_lines_columns import change_line, change_column


def create_cyclotron(particle=None, matrix=None):
    if len(matrix) < 4:
        return 'A matriz deve ter pelo menos 4 linhas!'
    if len(matrix[0]) < 4:
        return 'A matriz deve ter pelo menos 4 colunas!'
    if matrix is None:
        return 'É preciso o envio da matriz!'
    if particle is None:
        return matrix
    if particle != 'e' and particle != 'n' and particle != 'p':
        return "Não é particula!"
    particle_in_cyclotron = change_column(particle, matrix)
    particle_in_cyclotron = change_line(particle, particle_in_cyclotron)
    return particle_in_cyclotron


if __name__ == '__main__':
    matrix3 = square_matrix(4)
    print(create_cyclotron(particle='p', matrix=matrix3))
