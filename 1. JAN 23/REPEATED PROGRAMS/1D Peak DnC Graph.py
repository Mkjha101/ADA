# --Aim: 1D Peak

# Importing Libraries
import time
import random
import matplotlib.pyplot as mp

# Defining Array of size 'n'
def array(size):
    a=[]
    for i in range (1,size+1):
        a.append(random.randint(1,size))
    return a

def find_peak(arr, low, high, n):
    mid = low + (high - low) // 2

    # Check if mid is a peak
    if (mid == 0 or arr[mid - 1] <= arr[mid]) and \
       (mid == n - 1 or arr[mid + 1] <= arr[mid]):
        return mid

    # If left neighbor is greater, recurse left
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return find_peak(arr, low, mid - 1, n)

    # Else recurse right
    else:
        return find_peak(arr, mid + 1, high, n)

# Example usage
arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
peak_index = find_peak(arr, 0, n - 1, n)
print(f"Peak element is {arr[peak_index]} at index {peak_index}")
