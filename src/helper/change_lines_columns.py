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
        last_row = [*particle_list]
        last_row[-1] = 1
        for i in range(len(matrix)):
            matrix[i][-1] = last_row[i]
            matrix[i][0] = particle_list[i]
        matrix[-2][-2] = 'p'
        return matrix
    for i in range(len(matrix)):
        matrix[i][-1] = particle_list[i]
    return matrix


if __name__ == '__main__':
    print(change_line('p', [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],
                            [1, 1, 1, 1]]))
