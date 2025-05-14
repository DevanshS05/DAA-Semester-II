import matplotlib.pyplot as plt
import random

steps = 0

# Function to perform counting sort based on the digit represented by exp (10^i)
def counting_sort(arr, exp):
    global steps
    n = len(arr)
    output = [0] * n  # Output array to store sorted values
    count = [0] * 10  # Count array for digits (0-9)

    # Count occurrences of digits
    for i in range(n):
        steps+=1
        index = arr[i] // exp
        count[index % 10] += 1

    # Change count[i] to be the actual position of this digit in output[]
    for i in range(1, 10):
        steps+=1
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        steps+=1
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    global steps
    # Find the maximum number to know the number of digits
    max_num = max(arr)
    # Do counting sort for every digit. The exp is 10^i for current digit.
    exp = 1
    while max_num // exp > 0:
        steps+=1
        counting_sort(arr, exp)
        exp *= 10
    return steps

def run_radix_sort(n):
    global steps
    steps = 0
    lst = random.sample(range(size), n)
    radix_sort(lst)
    return steps

#Hyper-parameter
size = 100

n_values = [n for n in range(1,size+1)]
rs_steps = [run_radix_sort(n) for n in n_values]
lower_bound = [ 2*n+10 for n in n_values]
upper_bound = [3*(2*n+10) for n in n_values]


plt.plot(n_values, rs_steps, label='Radix Sort : θ(d(n+k))', color='black')
plt.plot(n_values,lower_bound,label='2*n+10',color='green',linestyle='dashed')
plt.plot(n_values,upper_bound,label='3*(2*n+10)',color='red',linestyle='dashed')
plt.legend()
plt.xlabel("Input Size (n)")
plt.ylabel("No of steps")
plt.title("Radix Sort : Time Complexity")
plt.show()
