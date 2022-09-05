# Compare a lista de arquivos em duas pastas distintas.
# Mostre os nomes dos arquivos que tem conteúdos diferentes e/ou que existem em apenas uma das pastas.


import os.path
import glob


def arq_list():
    list1 = []
    list2 = []
    for arq in sorted(glob.glob('Pasta 1\*')):
        size = os.path.getsize(arq)
        list1.append((arq, size))
    for arq in sorted(glob.glob('Pasta 2\*')):
        size = os.path.getsize(arq)
        list2.append((arq, size))
    list3 = []
    list3 = list3 + list1
    list3 = list3 + list2
    i = 0
    j = 0
    without_repeated = []
    repeated = []

    for x in list3:
        for y in list3:
            if x[1] == y[1]:
                if i != j:
                    repeated += [x]
            j += 1
        i += 1
        j = 0

    byte = [repeated[0][1]]
    for y in repeated:
        for b in byte:
            if b != y[1]:
                byte += [y[1]]

    for x in list3:
        for b in byte:
            if x[1] != b:
                without_repeated += [x]
    return repeated, without_repeated


repeated, without_repeated = arq_list()
print('Os repetidos são:', repeated)
print('Os não repetidos são:', without_repeated)