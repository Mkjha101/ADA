import time
import random
import matplotlib.pyplot as plt

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)

def isInside(x1, y1, x2, y2, x3, y3, x, y):
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x, y, x2, y2, x3, y3)
    A2 = area(x1, y1, x, y, x3, y3)
    A3 = area(x1, y1, x2, y2, x, y)
    return A == A1 + A2 + A3

# Measure time for 10,000 checks
runs = [1000 * i for i in range(1, 11)]
times = []

for r in runs:
    start = time.time()
    for _ in range(r):
        isInside(0, 0, 5, 0, 0, 5, random.randint(-10, 10), random.randint(-10, 10))
    end = time.time()
    times.append(end - start)

plt.plot(runs, times, marker='o', color='teal', label="Actual Time")
plt.plot(runs, [t / runs[-1] * times[-1] for t in runs], 'r--', label="Expected O(1) growth")

plt.xlabel("Number of Checks")
plt.ylabel("Time (s)")
plt.title("Point Inside Triangle - Constant Time Check")
plt.grid(True)
plt.legend()
plt.show()
