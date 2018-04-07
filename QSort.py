##              ##
#   QuickSort    #
##              ##


""" 
About:

A Divide & Conquer algorithm for sorting
with worst-case performance O(n^2), but
its average performance is O(n log_n) 
so it outperforms many others
__________________________________________

Algorithm:

1) Divide step: Dividing input array in two arrays:
A[start..end] -> A[start..q-1] & A[q+1..end], 
where A[start..q-1] contains elements less than A[q]
and A[q+1..end] contains those who are bigger than A[q]

2) Conquer step: Sub-arrays are sorted in the same fashion (using step 1)

3) Combining step: Not needed, the arrays are already sorted in place.

"""

import random

def random_partition(A, start, end):
    i = random.randint(start, end)
    A[end], A[i] = A[i], A[end]
    return partition(A, start, end)

def partition(A, start, end):
    """
    Partitions the array. 
    Helper func to qSort.
    """
    border = start - 1
    for pos in range(start, end):
        if A[pos] <= A[end]:
            border += 1
            A[border], A[pos] = A[pos], A[border]
    A[border + 1], A[end] = A[end], A[border + 1]
    return (border + 1)

def qSort(A, start, end):
    """
    Helper function.
    """
    if start < end:
        q = random_partition(A, start, end)
        qSort(A, start, q - 1)
        qSort(A, q + 1, end)

# Wrapper function to make it look better.
def QuickSort(A):
    """
    (Wrapper function) 
    Use THIS function for sorting!
    > Parameters:
    A - list of numbers or 
    any objects than can be compared.
    > Warning: 
    Changes list <!>
    """
    qSort(A, 0, len(A)-1)
    
    

#Testing:   
#A = [random.randint(0, 123) for _ in range(100)]
#QuickSort(A)
#print(A)
        
