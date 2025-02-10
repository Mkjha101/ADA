import time
import random
import numpy as np
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

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
        merge_sort(arr)
        end = time.time()
        total_time += (end - start)
    actual_times.append(total_time / runs)

# Fit nlogn curve using regression
logn = [n * np.log2(n) for n in input_sizes]
coeffs = np.polyfit(logn, actual_times, 1)
fitted_times = np.poly1d(coeffs)(logn)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, actual_times, 'o-', color='teal', linewidth=2, label='Actual Execution Time')
plt.plot(input_sizes, fitted_times, 'r--', linewidth=2, label='Log-Linear Fit (O(n log n))')

# Annotate a few points
for i in range(0, len(input_sizes), 2):
    plt.text(input_sizes[i], actual_times[i], f"{actual_times[i]:.4f}s", fontsize=8, color='teal')

plt.xlabel("Input Size (n)")
plt.ylabel("Avg Execution Time (seconds)")
plt.title("Time Complexity of Merge Sort")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
