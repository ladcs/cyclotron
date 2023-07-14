from .generate_matrix import generate_matrix


def square_matrix(d):
    if d < 4:
        return 'Matriz deve ter dimensão maior que 4!'
    return generate_matrix(1, d, d)
