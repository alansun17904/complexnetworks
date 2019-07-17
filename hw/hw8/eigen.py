import numpy
import math


def max_eigen(vals):
    return max(vals)


def epidemic_threshold(vals):
    return 1 / max_eigen(vals)


def smallest_beta(tao):
    return 0.5 * tao


def smallest_beta_1(tao):
    return 0.1 * tao

# Modify the two parameters below:
# For an nxn matrix, dim is n
dim = 6
# Input the values of the matrix in order (left to right, top to bottom)
values = [0, 1, 1, 0, 0, 1,
          1, 0, 1, 1, 0, 0,
          1, 1, 0, 1, 1, 0,
          0, 1, 1, 0, 1, 0,
          0, 0, 1, 1, 0, 0,
          1, 0, 0, 0, 0, 0]


# Do not modify anything below this line
arr = []
for x in range(len(values)):
    row = x // dim
    if row >= len(arr):
        arr.append([])
    arr[row].append(values[x])

vals, vectors = numpy.linalg.eig(numpy.array(arr))


print(f'Largest Eigen: {round(max_eigen(vals), 3)}')
print(f'Epidemic Threshold: {round(epidemic_threshold(vals), 3)}')
print(f'Smallest Beta for Delta = 0.5: {round(smallest_beta(epidemic_threshold(vals)), 3)}')
print(f'Smallest Beta for Delta = 0.1: {round(smallest_beta_1(epidemic_threshold(vals)), 3)}')