from matrix import Matrix
from tsp import TSP
import easygui
import time

MAX_INT = 2147483647


def next_permutation(a):
    """Generate the lexicographically next permutation inplace.

    https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    Return false if there is no next permutation.
    """
    # Find the largest index i such that a[i] < a[i + 1]. If no such
    # index exists, the permutation is the last permutation
    for i in reversed(range(len(a) - 1)):
        if a[i] < a[i + 1]:
            break  # found
    else:  # no break: not found
        return False  # no next permutation

    # Find the largest index j greater than i such that a[i] < a[j]
    j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])

    # Swap the value of a[i] with that of a[j]
    a[i], a[j] = a[j], a[i]

    # Reverse sequence from a[i + 1] up to and including the final element a[n]
    a[i + 1:] = reversed(a[i + 1:])
    return True


if __name__ == '__main__':

    file_name = easygui.fileopenbox()
    m = Matrix(file_name)
    cities = m.get_matrix()

    start = time.time()
    path = []

    for i in range(m.get_size()):
        if i != 0:
            path.append(i)

    tsp = TSP([], MAX_INT)

    while next_permutation(path):
        cost = 0
        cost += cities[0][path[0]]

        for i in range(len(path) - 1):
            cost += cities[path[i]][path[i + 1]]

        cost += cities[path[len(path) - 1]][0]

        if cost < tsp.get_cost():
            tsp.set_path(path)
            tsp.set_cost(cost)

    stop = time.time()

    tsp.show_result()
    print("Run time: ", int(stop - start))
