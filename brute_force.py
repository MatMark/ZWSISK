from matrix import Matrix
import easygui
import time
import multiprocessing
import itertools
from functools import partial


def run_bf(cities, permutation):
    cost = 0
    cost += cities[0][permutation[0]]

    for i in range(len(permutation) - 1):
        cost += cities[permutation[i]][permutation[i + 1]]

    cost += cities[permutation[len(permutation) - 1]][0]
    return cost, permutation


if __name__ == '__main__':
    file_name = easygui.fileopenbox()
    m = Matrix(file_name)
    cities = m.get_matrix()
    pool = multiprocessing.Pool()
    path = []

    for i in range(m.get_size()):
        if i != 0:
            path.append(i)

    # poczatek obliczen
    start = time.time()
    all_permutations = list(itertools.permutations(path))
    bf_process = partial(run_bf, cities)
    result = pool.map(bf_process, all_permutations)
    stop = time.time()
    # koniec obliczen

    print("Processes: ", len(multiprocessing.active_children()))
    dict_res = {}
    for x in result:
        dict_res[x[1]] = x[0]
    best = min(dict_res, key=dict_res.get)
    with_start_city = list(best)
    with_start_city.insert(0, 0)
    with_start_city.append(0)
    print("Cost: ", dict_res[best], "\nPath: ", with_start_city)
    print("Run time: ", int(stop - start))
