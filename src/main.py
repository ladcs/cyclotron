from helper.square_matrix import square_matrix
from helper.create_cyclotron import create_cyclotron


def main():
    cyclotron_without_particle = square_matrix(4)
    cyclotron_with_e = square_matrix(4)
    cyclotron_with_p_4 = square_matrix(4)
    cyclotron_with_p_6 = square_matrix(6)
    cyclotron_with_n = square_matrix(4)
    acceleration_cycle = create_cyclotron(matrix=cyclotron_without_particle)
    for row in acceleration_cycle:
        print(row)
    print()
    acceleration_e = create_cyclotron(particle='e', matrix=cyclotron_with_e)
    for row in acceleration_e:
        print(row)
    print()
    acceleration_4 = create_cyclotron(particle='p', matrix=cyclotron_with_p_4)
    for row in acceleration_4:
        print(row)
    print()
    acceleration_6 = create_cyclotron(particle='p', matrix=cyclotron_with_p_6)
    for row in acceleration_6:
        print(row)
    print()
    acceleration_n = create_cyclotron(particle='n', matrix=cyclotron_with_n)
    for row in acceleration_n:
        print(row)
    print()


if __name__ == '__main__':
    main()
