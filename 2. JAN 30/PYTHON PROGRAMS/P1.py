import time
import random
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

# Setup
input_sizes = list(range(50, 501, 25))  # More sizes for smooth curve
execution_times = []
runs = 3  # Average over multiple runs

# Measure actual times
for size in input_sizes:
    total_time = 0
    for _ in range(runs):
        arr = [random.randint(1, 10000) for _ in range(size)]
        start = time.time()
        selection_sort(arr)
        end = time.time()
        total_time += (end - start)
    avg_time = total_time / runs
    execution_times.append(avg_time)

# Fit a quadratic curve to actual data
coeffs = np.polyfit(input_sizes, execution_times, 2)
poly = np.poly1d(coeffs)
fitted_times = poly(input_sizes)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, execution_times, 'o-', color='teal', label='Actual Execution Time', linewidth=2, markersize=5)
plt.plot(input_sizes, fitted_times, 'r--', label='Quadratic Fit (O(n²))', linewidth=2)

# Mark selected points with values
for i in range(0, len(input_sizes), 2):
    plt.text(input_sizes[i], execution_times[i], f"{execution_times[i]:.4f}s", fontsize=9, ha='right', color='teal')

plt.xlabel("Input Size (n)")
plt.ylabel("Avg Execution Time (seconds)")
plt.title("Time Complexity of Selection Sort")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
