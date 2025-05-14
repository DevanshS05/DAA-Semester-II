import math
import matplotlib.pyplot as plt
import random

localSteps = 0
steps = 0

def insertionSort(arr):
    global localSteps
    for i in range(1,len(arr)):
        j = i-1
        key = arr[i]
        while(j>=0 and arr[j]>key):
            localSteps+=1
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

def bucketSort(arr):
    global steps,localSteps
    n = len(arr)

    result = [ list() for _ in range(n)]

    #Place the elements into the buckets
    for x in arr:
        steps+=1
        result[math.floor(n*x)].append(x)
    
    #Sort the individual buckets
    for y in range(0,n):
        localSteps = 0
        result[y] = insertionSort(result[y])
        steps+=localSteps
    sortedArr = list()

    #Merge all of the elements from the buckets into a single array
    for i in range(0,n):
        if len(result[i])>0:
            for j in range(0,len(result[i])):
                steps+=1
                sortedArr.append(result[i][j])

    return sortedArr

def run_bucket_sort(n):
    global steps, localSteps
    steps = 0
    localSteps = 0
    lst = [random.random() for _ in range(n)]
    bucketSort(lst)
    return steps

#Hyper-parameters
sampleSize = 1000

n_values = [n for n in range(1,sampleSize+1)]
bs_steps = [run_bucket_sort(n) for n in n_values]
linear_n = [n for n in n_values]
three_linear_n = [3*n for n in n_values]

plt.plot(n_values,bs_steps,label='Bucket Sort : θ(n)',color='purple')
plt.plot(n_values,linear_n,label='n',color='green',linestyle='dashed')
plt.plot(n_values,three_linear_n,label='3*n',color='red',linestyle='dashed')

plt.xlabel("Input Size (n)")
plt.ylabel("No of Steps")
plt.title("Bucket Sort : Time Complexity")
plt.grid(True)
plt.legend()
plt.show()
