import random
import time
import matplotlib.pyplot as plt

def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    count = 0
    last_end = -1
    for start, end in activities:
        if start >= last_end:
            count += 1
            last_end = end
    return count

input_sizes = [100 * i for i in range(1, 11)]
actual_times = []

for n in input_sizes:
    activities = [(random.randint(0, 50), random.randint(51, 100)) for _ in range(n)]
    start_time = time.time()
    activity_selection(activities)
    end_time = time.time()
    actual_times.append(end_time - start_time)

expected_times = [t * input_sizes[-1] / input_sizes[-1] * actual_times[-1] for t in input_sizes]

plt.plot(input_sizes, actual_times, color='teal', marker='o', label="Actual Time")
plt.plot(input_sizes, expected_times, 'r--', label="Expected O(n log n)")
plt.xlabel("Number of Activities")
plt.ylabel("Time (s)")
plt.title("Activity Selection Time Complexity")
plt.grid(True)
plt.legend()
plt.show()
