import time
import matplotlib.pyplot as mp
import math
import random

# 1D Peak Finding using Divide and Conquer
def find_peak(arr, low, high, n):
    mid = low + (high - low) // 2
    if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
        return mid
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return find_peak(arr, low, mid - 1, n)
    else:
        return find_peak(arr, mid + 1, high, n)

# Generate and time the algorithm
sizes = list(range(1000, 100001, 5000))
actual_times = []

for size in sizes:
    total_time = 0
    trials = 10  # Averaging over 10 trials
    for _ in range(trials):
        arr = [random.randint(1, 1000000) for _ in range(size)]
        start = time.perf_counter()
        find_peak(arr, 0, size - 1, size)
        end = time.perf_counter()
        total_time += (end - start)
    avg_time = (total_time / trials) * 1000  # Convert to ms
    actual_times.append(avg_time)

# Prepare scaled theoretical log₂(n)
scale = actual_times[0] / math.log2(sizes[0])
expected_times = [math.log2(n) * scale for n in sizes]

# Plot
mp.figure(figsize=(10, 7))
mp.plot(sizes, actual_times, marker='o', label='Actual Time', color='teal')
mp.plot(sizes, expected_times, linestyle='--', label='~ log₂(n)', color='crimson')
mp.title("Time Complexity: 1D Peak Finding (Divide and Conquer)")
mp.xlabel("Input Size (n)")
mp.ylabel("Execution Time (ms)")
mp.legend()
mp.grid(True)
mp.tight_layout()
mp.show()
