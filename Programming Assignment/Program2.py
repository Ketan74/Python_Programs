""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""

import numpy as np


def procedure_max(lst1):
    return np.max(lst1)


def procedure_min(lst1):
    return np.min(lst1)


def procedure_mean(lst1):
    return np.mean(lst1)


def procedure_standard_deviation(lst1):
    return np.std(lst1)


def procedure_variance(lst1):
    return np.var(lst1)

lst = list(map(int, input().strip().split()))

print(procedure_min(lst))
print(procedure_max(lst))
print(procedure_mean(lst))
print(procedure_standard_deviation(lst))
print(procedure_variance(lst))