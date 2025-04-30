import time
import matplotlib.pyplot as mp
import math
import random

def find_peak(arr, low, high, n):
    mid = low + (high - low) // 2
    if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
        return mid
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return find_peak(arr, low, mid - 1, n)
    else:
        return find_peak(arr, mid + 1, high, n)

def run_and_plot():
    sizes = list(range(1000, 100001, 5000))
    times = []

    for n in sizes:
        arr = [random.randint(1, 1000000) for _ in range(n)]
        start = time.perf_counter()
        find_peak(arr, 0, n - 1, n)
        end = time.perf_counter()
        times.append((end - start) * 1000)  # in milliseconds

    # Scaling factor so both curves start at same point
    scale_factor = times[0] / math.log2(sizes[0])
    log_curve = [math.log2(n) * scale_factor for n in sizes]

    # Plot
    mp.plot(sizes, times, marker='o', label="Actual Time", color='teal')
    mp.plot(sizes, log_curve, linestyle='--', label="~ log₂(n)", color='crimson')

    mp.title("Time Complexity: 1D Peak Finding (Divide and Conquer)")
    mp.xlabel("Input Size (n)")
    mp.ylabel("Execution Time (ms)")
    mp.legend()
    mp.grid(True)
    mp.tight_layout()
    mp.show()

run_and_plot()
