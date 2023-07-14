def change_line(particle, matrix):
    particle_line = [particle] * len(matrix[0])
    matrix[0] = particle_line
    if particle == 'p':
        matrix[-1] = [*particle_line]
        matrix[-1][-1] = 1
    return matrix


def change_column(particle, matrix):
    if particle == 'n':
        return matrix
    particle_list = [particle] * len(matrix)
    if particle == 'p':
        for column in matrix:
            column[-1] = particle_list[column[0]]
            column[0] = particle_list[column[0]]
        matrix[-2][-2] = 'p'
        matrix[-1][-1] = 1
        return matrix
    for column in matrix:
        column[-1] = particle_list[column[0]]
    return matrix


if __name__ == '__main__':
    print(change_line('p', [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],
                            [1, 1, 1, 1]]))
