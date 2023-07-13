def change_first_line(particle, matrix):
    particle_list = [particle] * len(matrix[0])
    matrix[0] = particle_list
    return matrix
