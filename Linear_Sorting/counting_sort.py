import random
import matplotlib.pyplot as plt
import math

steps = 0

#k represents the range of the elements in the array
def countingSort(arr, k):
    global steps
    count = [0 for _ in range(k+1)]
    result = [-1 for _ in range(len(arr))]

    #Counting no. of times each element appears in the array
    for j in range(len(arr)):
        steps+=1
        count[arr[j]] += 1

    #Counting no of values less than or equal current element
    for i in range(1,len(count)):
        steps+=1
        count[i]+=count[i-1]

    #Placing the elements accordingly into the result array
    for j in range(len(arr)-1,-1,-1):
        steps+=1
        result[count[arr[j]]-1] = arr[j]
        count[arr[j]] -= 1
    return result

def run_counting_sort(n):
    global steps
    steps = 0
    lst = random.sample(range(2*n), n)
    countingSort(lst, max(lst))
    return steps
    
#Hyper-parameters
sampleSize = 1000

n_values = [n for n in range(1,sampleSize+1)]
cs_steps = [run_counting_sort(n) for n in n_values]

five_linear_n = [5*n for n in n_values]
three_linear_n = [3*n for n in n_values]
nlogn = [n*math.log(n) for n in n_values]

plt.plot(n_values,cs_steps,label='Bucket Sort : θ(n+k)',color='purple')

#Counting sort is supposed to beat the lower bound of comparsion sort θ(nlogn)
plt.plot(n_values, nlogn, label='nlogn',linestyle='dashed',color='orange')

plt.plot(n_values,five_linear_n,label='5*n',color='green',linestyle='dashed')
plt.plot(n_values,three_linear_n,label='3*n',color='red',linestyle='dashed')

plt.xlabel("Input Size (n)")
plt.ylabel("No of Steps")
plt.title("Counting Sort : Time Complexity")
plt.grid(True)
plt.legend()
plt.show()