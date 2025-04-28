import time
import matplotlib.pyplot as mp
import math
import random

# Function to find a peak using Divide and Conquer
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

# Function to run and plot time complexity
def run_and_plot():
    sizes = list(range(1000, 100001, 5000))
    times = []

    for size in sizes:
        arr = [random.randint(1, 1000000) for _ in range(size)]
        start = time.time()
        find_peak(arr, 0, size - 1, size)
        end = time.time()
        times.append((end - start) * 1000)  # in milliseconds

    # Reference logarithmic curve (scaled)
    log_n = [math.log2(n) * 0.01 for n in sizes]

    # Plotting
    mp.plot(sizes, times, marker='o', label="Actual Time", color='blue')
    mp.plot(sizes, log_n, linestyle='--', label="~ log₂(n)", color='orange')

    mp.title("Time Complexity: 1D Peak Finding (Divide and Conquer)")
    mp.xlabel("Input Size (n)")
    mp.ylabel("Execution Time (ms)")
    mp.legend()
    mp.grid(True)
    mp.show()

# Main Execution
if __name__ == "__main__":
    arr = [1, 3, 20, 4, 1, 0]
    n = len(arr)
    start = time.time()
    peak_index = find_peak(arr, 0, n - 1, n)
    end = time.time()
    print(f"Peak element is {arr[peak_index]} at index {peak_index}")
    print(f"Execution Time: {(end - start) * 1000:.5f} ms")

    run_and_plot()
