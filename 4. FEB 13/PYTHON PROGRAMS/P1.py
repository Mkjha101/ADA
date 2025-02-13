import time
import random
import matplotlib.pyplot as plt
import numpy as np

def generate_matrix(size):
    return [[random.randint(0, 9) for _ in range(size)] for _ in range(size)]

def recursive_multiply(A, B, C, sr1, er1, sc1, ec1, sr2, er2, sc2, ec2):
    if er1 - sr1 < 2 and ec2 - sc2 < 2:
        C[sr1][sc2] += A[sr1][sc1] * B[sr2][sc2] + A[sr1][sc1 + 1] * B[sr2 + 1][sc2]
        C[sr1][sc2 + 1] += A[sr1][sc1] * B[sr2][sc2 + 1] + A[sr1][sc1 + 1] * B[sr2 + 1][sc2 + 1]
        C[sr1 + 1][sc2] += A[sr1 + 1][sc1] * B[sr2][sc2] + A[sr1 + 1][sc1 + 1] * B[sr2 + 1][sc2]
        C[sr1 + 1][sc2 + 1] += A[sr1 + 1][sc1] * B[sr2][sc2 + 1] + A[sr1 + 1][sc1 + 1] * B[sr2 + 1][sc2 + 1]
        return

    mid1 = sr1 + (er1 - sr1) // 2
    mid2 = sc1 + (ec1 - sc1) // 2
    mid3 = sr2 + (er2 - sr2) // 2
    mid4 = sc2 + (ec2 - sc2) // 2

    recursive_multiply(A, B, C, sr1, mid1, sc1, mid2, sr2, mid3, sc2, mid4)
    recursive_multiply(A, B, C, sr1, mid1, mid2 + 1, ec1, mid3 + 1, er2, sc2, mid4)
    recursive_multiply(A, B, C, sr1, mid1, sc1, mid2, sr2, mid3, mid4 + 1, ec2)
    recursive_multiply(A, B, C, sr1, mid1, mid2 + 1, ec1, mid3 + 1, er2, mid4 + 1, ec2)
    recursive_multiply(A, B, C, mid1 + 1, er1, sc1, mid2, sr2, mid3, sc2, mid4)
    recursive_multiply(A, B, C, mid1 + 1, er1, mid2 + 1, ec1, mid3 + 1, er2, sc2, mid4)
    recursive_multiply(A, B, C, mid1 + 1, er1, sc1, mid2, sr2, mid3, mid4 + 1, ec2)
    recursive_multiply(A, B, C, mid1 + 1, er1, mid2 + 1, ec1, mid3 + 1, er2, mid4 + 1, ec2)

sizes = [2, 4, 8, 16, 32, 64]
actual_times = []
runs = 3

for size in sizes:
    total_time = 0
    for _ in range(runs):
        A = generate_matrix(size)
        B = generate_matrix(size)
        C = [[0] * size for _ in range(size)]

        start = time.time()
        recursive_multiply(A, B, C, 0, size - 1, 0, size - 1, 0, size - 1, 0, size - 1)
        end = time.time()
        total_time += end - start

    actual_times.append(total_time / runs)

# Expected TC: O(n^3)
expected = [s ** 3 for s in sizes]
coeffs = np.polyfit(expected, actual_times, 1)
fitted = np.poly1d(coeffs)(expected)

plt.figure(figsize=(4, 8))
plt.plot(sizes, actual_times, 'o-', color='teal', label="Actual Time (Recursive Mult.)")
plt.plot(sizes, fitted, 'r--', label="Expected O(n³) Time")

# Annotate sample points
for i in range(len(sizes)):
    plt.text(sizes[i], actual_times[i], f"{actual_times[i]:.4f}s", fontsize=8, color='teal')

plt.xlabel("Matrix Size (n x n)")
plt.ylabel("Average Time (s)")
plt.title("Time Complexity: Recursive Matrix Multiplication")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
