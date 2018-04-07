###                                           ###
#  counting sort implementation with lists :    #
###                                           ###

import time
import random

def counting_sort(A, k):
    """
    Args: 
    > array A,
    > k - len of array
    Hidden args:
    > n - number of different keys
    for short enough k we have linear time sorting.
    """
    
    n = len(A)
    L = [[] for _ in range(k)]
    for j in range(n):
        L[A[j]].append(A[j])
    output = []
    for i in range(k):
        output.extend(L[i])
    return output
        
# testing:
A = [10, 12, 1, 34, 13, 15, 2, 1, 9, 7]
# testing with any N & K
N = 100000
K = 40
B = [int(random.random() * K) for _ in range(N)]


def time_measuring(func, *args):
    start = time.clock()
    res = func(*args)
    end = time.clock()
    # getting function name & formatting it:
    func_name = str(func).split()
    func_name[0] = func_name[0][1:]
    if func_name[-2] == 'at': func_name = func_name[:-2]
    # output:
    print(' '.join(func_name), ':', end - start)
        
    
def dumb_sort(A):
    A = A.copy()
    n = len(A)
    for x in range(n):
        _min = A[x]
        pos_min = x
        for j in range(x, n):
            if A[j] < _min:
                _min = A[j]
                pos_min = j
        A[x], A[pos_min] = A[pos_min], A[x]
        
    return A
    
    
print('\nTimes for N = 10, k = 34')
time_measuring(counting_sort, A, 35)
time_measuring(dumb_sort, A)
time_measuring(sorted, A)

print('\nTimes for N = {0}, K = {1}'.format(N, K))
time_measuring(counting_sort, B, K)
time_measuring(dumb_sort, B)
time_measuring(sorted, B)
