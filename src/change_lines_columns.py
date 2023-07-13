def change_line(particle, matrix):
    particle_first_line = [particle] * len(matrix[0])
    matrix[0] = particle_first_line
    if particle == 'p':
        particle_last_line = particle_first_line
        matrix[-1] = particle_last_line
    return matrix


def change_column(particle, matrix):
    particle_list = [particle] * len(matrix)
    if particle == 'p':
        for column in matrix:
            column[-1] = particle_list[column[0]]
            column[0] = particle_list[column[0]]
        matrix[-2][-2] = 'p'
        matrix[-1][-1] = 1
        return matrix
    for column in matrix:
        column[-1] = particle_list[column[-1]]
    return matrix


if __name__ == '__main__':
    print(change_column('p', [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],
                              [1, 1, 1, 1]]))
