import time
import random
import numpy as np
import matplotlib.pyplot as plt

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(capacity, items):
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_value = 0.0

    for item in items:
        if capacity >= item.weight:
            capacity -= item.weight
            total_value += item.value
        else:
            total_value += item.ratio * capacity
            break

    return total_value

input_sizes = list(range(100, 2001, 100))
actual_times = []
runs = 3

for n in input_sizes:
    total_time = 0
    for _ in range(runs):
        items = [Item(random.randint(1, 100), random.randint(1, 50)) for _ in range(n)]
        capacity = random.randint(n, 2*n)
        start = time.time()
        fractional_knapsack(capacity, items)
        end = time.time()
        total_time += (end - start)
    actual_times.append(total_time / runs)

# Expected Time Complexity: O(n log n) due to sorting
nlogn = [n * np.log2(n) for n in input_sizes]
coeffs = np.polyfit(nlogn, actual_times, 1)
fitted = np.poly1d(coeffs)(nlogn)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, actual_times, 'o-', color='teal', linewidth=2, label="Actual Execution Time")
plt.plot(input_sizes, fitted, 'r--', linewidth=2, label="Expected Time (O(n log n))")

# Mark sample points
for i in range(0, len(input_sizes), 2):
    plt.text(input_sizes[i], actual_times[i], f"{actual_times[i]:.4f}s", fontsize=8, color='teal')

plt.xlabel("Number of Items (n)")
plt.ylabel("Average Execution Time (seconds)")
plt.title("Time Complexity of Fractional Knapsack")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
