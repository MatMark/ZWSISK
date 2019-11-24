from matrix import Matrix
import easygui
import time
import multiprocessing
from functools import partial


def next_permutation(a):
    for i in reversed(range(len(a) - 1)):
        if a[i] < a[i + 1]:
            break
    else:
        return False
    j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])
    a[i], a[j] = a[j], a[i]
    a[i + 1:] = reversed(a[i + 1:])
    return True


def run_bf(cities, permutation):
    cost = 0
    cost += cities[0][permutation[0]]

    for i in range(len(permutation) - 1):
        cost += cities[permutation[i]][permutation[i + 1]]

    cost += cities[permutation[len(permutation) - 1]][0]
    return cost, tuple(permutation)


if __name__ == '__main__':
    file_name = easygui.fileopenbox()
    m = Matrix(file_name)
    cities = m.get_matrix()
    pool = multiprocessing.Pool(processes=int(input("Number of processes: ")))
    path = []
    best_of_the_best = None
    paths_in_one = 2 ** 15

    for i in range(m.get_size()):
        if i != 0:
            path.append(i)

    start = time.time()
    while True:
        end = False
        path_list = []
        for i in range(paths_in_one):
            path_list.append(path.copy())
            end = not next_permutation(path)
            if end:
                break

        bf_process = partial(run_bf, cities)
        result = pool.map(bf_process, path_list)

        dict_res = {}
        for x in result:
            dict_res[x[1]] = x[0]
        best = min(dict_res, key=dict_res.get)

        if best_of_the_best is None:
            best_of_the_best = tuple([best, dict_res[best]])
        elif best_of_the_best[1] > dict_res[best]:
            best_of_the_best = tuple([best, dict_res[best]])

        path_list.clear()
        if end:
            break

    stop = time.time()
    print("Processes: ", len(multiprocessing.active_children()))
    with_start_city = list(best_of_the_best[0])
    with_start_city.insert(0, 0)
    with_start_city.append(0)
    print("Cost: ", best_of_the_best[1], "\nPath: ", with_start_city)
    print("Run time: ", int(stop - start))
