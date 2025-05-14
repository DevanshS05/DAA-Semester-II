from minHeap import MinHeap
import math
import random
import matplotlib.pyplot as plt

steps = 0

def heap_sort(arr):
    global steps
    h = MinHeap()
    h.build_min_heap(arr[:]) #Construct a heap out of the elements of the array
    steps+=len(arr) #build_mean_heap takes O(n) time
    sorted_arr = []
    while h.heap:
        sorted_arr.append(h.extract_min())
        steps+=1
        if len(h.heap)!=0:
            #each extract_min calls heapfiy once
            steps+=math.log2(1+len(h.heap))
    return arr

def run_heap_sort(n):
    global steps
    steps = 0
    lst = random.sample(range(size), n)
    heap_sort(lst)
    return steps

#Hyper-parameter
size = 1000

n_values = [n for n in range(1,size+1)]
hs_steps = [run_heap_sort(n) for n in n_values]
n_logn = [n*math.log2(n) for n in n_values]

plt.plot(n_values, hs_steps, label='Heap Sort : O(nlgn)', color='black')
plt.plot(n_values, n_logn, label='nlgn', linestyle='dashed', color='red')
plt.plot(n_values, n_values, label='n', linestyle='dashed', color='green')
plt.legend()
plt.xlabel('Input Size (n)')
plt.ylabel('No. of Steps')
plt.title("Heap Sort : Time Complexity")
plt.show()
