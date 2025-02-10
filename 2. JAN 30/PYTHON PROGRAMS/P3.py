import time
import random
import numpy as np
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Input sizes
input_sizes = list(range(100, 1001, 100))
actual_times = []
runs = 3

# Measure execution time
for size in input_sizes:
    total_time = 0
    for _ in range(runs):
        arr = [random.randint(1, 10000) for _ in range(size)]
        start = time.time()
        insertion_sort(arr)
        end = time.time()
        total_time += (end - start)
    actual_times.append(total_time / runs)

# Fit a quadratic curve to actual data
coeffs = np.polyfit(input_sizes, actual_times, 2)
poly = np.poly1d(coeffs)
fitted_times = poly(input_sizes)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, actual_times, 'o-', color='teal', label='Actual Execution Time', linewidth=2)
plt.plot(input_sizes, fitted_times, 'r--', label='Quadratic Fit (O(n²))', linewidth=2)

# Annotate a few points
for i in range(0, len(input_sizes), 2):
    plt.text(input_sizes[i], actual_times[i], f"{actual_times[i]:.4f}s", fontsize=8, color='teal')

plt.xlabel("Input Size (n)")
plt.ylabel("Avg Execution Time (seconds)")
plt.title("Time Complexity of Insertion Sort")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()