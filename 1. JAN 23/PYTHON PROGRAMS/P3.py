import time
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Polynomial

def generate_magic_square(n):
    magic_square = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    i, j = 0, n // 2
    while num <= n * n:
        magic_square[i][j] = num
        num += 1
        new_i = (i - 1 + n) % n
        new_j = (j + 1) % n
        if magic_square[new_i][new_j] != 0:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j
    return magic_square

# Parameters
min_n = 3
max_n = 201
step = 10

Obs = []
T = []

# Measure time for different sizes of magic square
for n in range(min_n, max_n + 1, step):
    if n % 2 == 0:
        continue
    repetitions = 100 if n < 50 else 10
    total_time = 0
    for _ in range(repetitions):
        start = time.time()
        generate_magic_square(n)
        end = time.time()
        total_time += (end - start)
    avg_time = total_time / repetitions
    Obs.append(n)
    T.append(avg_time)

# Convert to numpy arrays
x = np.array(Obs)
y = np.array(T)

# Fit a polynomial (e.g., degree 2) to simulate time complexity
p = Polynomial.fit(x, y, 2)
y_fit = p(x)

# Plotting
plt.style.use('bmh')
plt.figure(figsize=(10, 6))
plt.title("Time Complexity of Magic Square Generation")
plt.plot(x, y, 'o-', label="Actual Execution Time", color='teal')
plt.plot(x, y_fit, 'r--', label="Quadratic Fit (O(n^2))")
plt.xlabel("Matrix Size (n × n)")
plt.ylabel("Avg Execution Time (seconds)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

'''
import time
import matplotlib.pyplot as mp

def generate_magic_square(n):
    magic_square = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    i, j = 0, n // 2
    while num <= n * n:
        magic_square[i][j] = num
        num += 1
        new_i = (i - 1 + n) % n
        new_j = (j + 1) % n
        if magic_square[new_i][new_j] != 0:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j
    return magic_square

# Lists to store observations
Obs = []
T = []

# Use a more detailed and regular range of odd numbers
min_n = 3
max_n = 201  # Set upper limit
step = 10    # Step size

print("Running timing test...")

for n in range(min_n, max_n + 1, step):
    if n % 2 == 0:
        continue  # Only odd numbers

    repetitions = 100 if n < 50 else 10  # Fewer reps for large n
    total_time = 0

    print(f"Testing for n = {n} (repetitions: {repetitions})")
    for _ in range(repetitions):
        stime = time.time()
        generate_magic_square(n)
        etime = time.time()
        total_time += (etime - stime)

    avg_time = total_time / repetitions
    Obs.append(n)
    T.append(avg_time)

# Output data
print("Observations (n):", Obs)
print("Avg Time (s):", T)

# Plotting
mp.style.use('bmh')
mp.figure(figsize=(10, 6))
mp.title("Time Complexity of Magic Square Generation")
mp.plot(Obs, T, marker='o', linewidth=2, color='teal')
mp.xlabel("Matrix Size (n × n)")
mp.ylabel("Avg Execution Time (seconds)")
mp.grid(True, linestyle='--', alpha=0.6)
mp.tight_layout()
mp.xticks(fontsize=10)
mp.yticks(fontsize=10)
mp.show()
'''