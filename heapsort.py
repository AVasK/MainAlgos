### Heaps:
#

import math

# > Binary Heap:
# - Main property:
# -- Parent node contains values <= Child nodes
# ---- this is done to guarantee MIN_VALUE in the root node

class BinaryHeap():
    def __init__(self):
        self.heap_arr = []

    def __str__(self):
        return str(self.heap_arr)

    def heap_swap(self, i, j):
        self.heap_arr[i], self.heap_arr[j] = self.heap_arr[j], self.heap_arr[i]

    def successors(i):
        return (2*i+1, 2*i+2)

    def parent(i):
        return math.floor((i-1)/2)

    def insert(self, elem):
        self.heap_arr.append(elem)
        idx = len(self.heap_arr) - 1
        self.sift_up(idx)

    def sift_up(self, i):
        if i == 0:
            return # No parent for root :(
        p_i = BinaryHeap.parent(i)
        if self.heap_arr[p_i] > self.heap_arr[i]:
            self.heap_arr[p_i], self.heap_arr[i] = self.heap_arr[i], self.heap_arr[p_i] # fancy swap
            self.sift_up(p_i) # Sift-Up has it's name for a reason

    def extract_min(self):
        _min = self.heap_arr[0]
        self.heap_arr[0] = self.heap_arr[-1] # last becomes root
        self.heap_arr.pop(len(self.heap_arr) - 1)
        self.sift_down(0) # Ordering the mess we made...
        return _min

    def sift_down(self, i):
        if 2*i + 2 >= len(self.heap_arr):
            if 2*i + 1 < len(self.heap_arr): # Only left son exists
                if self.heap_arr[i] > self.heap_arr[2*i+1]: # and he's less
                    self.heap_swap(i, 2*i+1)
            return # No children for children...

        c_1, c_2 = BinaryHeap.successors(i) # left & right sons
        k = self.heap_arr[i]     # k = key of i_th element

        if k > min(self.heap_arr[c_1], self.heap_arr[c_2]):
            if self.heap_arr[c_1] < self.heap_arr[c_2]:
                i_min  = c_1
            else:
                i_min  = c_2

            self.heap_swap(i, i_min)
            self.sift_down(i_min) # going down iterative.

    ### We're all done with basic heap operation to make HeapSort :)

def HeapSort(arr : [], show = False):
    heap = BinaryHeap()
    res = []

    for elem in arr:
        heap.insert(elem)
        if show : print(heap)
    for elem in arr:
        res.append(heap.extract_min())
        if show : print(heap)

    return res
