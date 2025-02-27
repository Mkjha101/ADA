import time
import matplotlib.pyplot as mp
import random
import math

def add_matrix(A, B, multiplier=1):
    size = len(A)
    return [[A[i][j] + multiplier * B[i][j] for j in range(size)] for i in range(size)]

def strassen_multiply(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2
    # Divide matrices
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Compute 7 products
    P1 = strassen_multiply(A11, add_matrix(B12, B22, -1))
    P2 = strassen_multiply(add_matrix(A11, A12), B22)
    P3 = strassen_multiply(add_matrix(A21, A22), B11)
    P4 = strassen_multiply(A22, add_matrix(B21, B11, -1))
    P5 = strassen_multiply(add_matrix(A11, A22), add_matrix(B11, B22))
    P6 = strassen_multiply(add_matrix(A12, A22, -1), add_matrix(B21, B22))
    P7 = strassen_multiply(add_matrix(A11, A21, -1), add_matrix(B11, B12))

    # Combine submatrices
    C11 = add_matrix(add_matrix(add_matrix(P5, P4), P6, -1), P2)
    C12 = add_matrix(P1, P2)
    C21 = add_matrix(P3, P4)
    C22 = add_matrix(add_matrix(add_matrix(P5, P1), P3, -1), P7, -1)

    new_matrix = []
    for i in range(mid):
        new_matrix.append(C11[i] + C12[i])
    for i in range(mid):
        new_matrix.append(C21[i] + C22[i])
    return new_matrix

def generate_matrix(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

def run_and_plot():
    sizes = [2**i for i in range(1, 8)]  # from 2 to 128
    times = []

    for n in sizes:
        A = generate_matrix(n)
        B = generate_matrix(n)
        start = time.perf_counter()
        strassen_multiply(A, B)
        end = time.perf_counter()
        times.append((end - start) * 1000)

    scale_factor = times[0] / (sizes[0] ** 2.81)
    theoretical = [(n ** 2.81) * scale_factor for n in sizes]

    mp.plot(sizes, times, marker='o', label="Actual Time", color='teal')
    mp.plot(sizes, theoretical, linestyle='--', label="~ n^2.81", color='crimson')

    mp.title("Time Complexity: Matrix Multiplication (Strassen’s Algorithm)")
    mp.xlabel("Matrix Size (n x n)")
    mp.ylabel("Execution Time (ms)")
    mp.legend()
    mp.grid(True)
    mp.tight_layout()
    mp.show()

run_and_plot()
