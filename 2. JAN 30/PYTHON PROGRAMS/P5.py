import time
import random
import numpy as np
import matplotlib.pyplot as plt

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Input sizes
input_sizes = list(range(100, 2001, 100))
actual_times = []
runs = 3

# Measure execution time
for size in input_sizes:
    total_time = 0
    for _ in range(runs):
        arr = [random.randint(1, 10000) for _ in range(size)]
        start = time.time()
        heap_sort(arr)
        end = time.time()
        total_time += (end - start)
    actual_times.append(total_time / runs)

# Expected O(n log n) fit
nlogn = [n * np.log2(n) for n in input_sizes]
coeffs = np.polyfit(nlogn, actual_times, 1)
fitted_times = np.poly1d(coeffs)(nlogn)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, actual_times, 'o-', color='teal', linewidth=2, label='Actual Execution Time')
plt.plot(input_sizes, fitted_times, 'r--', linewidth=2, label='Log-Linear Fit (O(n log n))')

# Annotate a few points
for i in range(0, len(input_sizes), 2):
    plt.text(input_sizes[i], actual_times[i], f"{actual_times[i]:.4f}s", fontsize=8, color='teal')

plt.xlabel("Input Size (n)")
plt.ylabel("Avg Execution Time (seconds)")
plt.title("Time Complexity of Heap Sort")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
