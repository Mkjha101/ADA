import random
import time
import matplotlib.pyplot as plt

def orientation(a, b, c):
    return (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])

def convex_hull(points):
    points = sorted(points)
    if len(points) < 3:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

input_sizes = [100 * i for i in range(1, 11)]
actual_times = []

for n in input_sizes:
    pts = [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(n)]
    start_time = time.time()
    convex_hull(pts)
    end_time = time.time()
    actual_times.append(end_time - start_time)

expected_times = [x * actual_times[-1] / input_sizes[-1] * (1 + 0.2) for x in input_sizes]  # Approximating O(n log n)

plt.plot(input_sizes, actual_times, marker='o', color='teal', label='Actual Time')
plt.plot(input_sizes, expected_times, 'r--', label='Expected O(n log n)')
plt.title("Convex Hull (Graham's Scan) Time Complexity")
plt.xlabel("Number of Points")
plt.ylabel("Time (s)")
plt.grid(True)
plt.legend()
plt.show()
