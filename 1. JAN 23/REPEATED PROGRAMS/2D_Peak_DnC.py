import time
import matplotlib.pyplot as mp
import random
import math

# Function to find the index of the maximum element in a column
def find_max_in_column(matrix, mid_col, rows):
    max_row = 0
    for i in range(1, rows):
        if matrix[i][mid_col] > matrix[max_row][mid_col]:
            max_row = i
    return max_row

# Recursive 2D peak finder using Divide and Conquer
def find_peak_2d(matrix, rows, cols, mid_col):
    max_row = find_max_in_column(matrix, mid_col, rows)

    # Check if the current element is a 2D peak
    if (mid_col == 0 or matrix[max_row][mid_col] >= matrix[max_row][mid_col - 1]) and \
       (mid_col == cols - 1 or matrix[max_row][mid_col] >= matrix[max_row][mid_col + 1]):
        return (max_row, mid_col)

    # Move left
    elif mid_col > 0 and matrix[max_row][mid_col - 1] > matrix[max_row][mid_col]:
        return find_peak_2d(matrix, rows, cols, mid_col - cols // 4)

    # Move right
    else:
        return find_peak_2d(matrix, rows, cols, mid_col + cols // 4)

# Plot time complexity graph
def run_and_plot():
    sizes = list(range(100, 1001, 100))  # Matrix sizes: 100x100 to 1000x1000
    times = []

    for size in sizes:
        matrix = [[random.randint(1, 100000) for _ in range(size)] for _ in range(size)]
        start = time.time()
        find_peak_2d(matrix, size, size, size // 2)
        end = time.time()
        times.append((end - start) * 1000)  # in milliseconds

    # Reference curve: O(n log n), scaled
    ref_curve = [n * math.log2(n) * 0.0001 for n in sizes]

    # Plotting
    mp.plot(sizes, times, marker='o', label="Actual Time", color='darkred')
    mp.plot(sizes, ref_curve, linestyle='--', label="~ n·log₂(n)", color='green')

    mp.title("Time Complexity: 2D Peak Finding (Divide and Conquer)")
    mp.xlabel("Matrix Dimension (n x n)")
    mp.ylabel("Execution Time (ms)")
    mp.legend()
    mp.grid(True)
    mp.show()

# Main Execution
if __name__ == "__main__":
    matrix = [
        [10, 8, 10, 10],
        [14, 13, 12, 11],
        [15, 9, 11, 21],
        [16, 17, 19, 20]
    ]
    rows, cols = len(matrix), len(matrix[0])
    
    start = time.time()
    peak_pos = find_peak_2d(matrix, rows, cols, cols // 2)
    end = time.time()
    print(f"Peak element is {matrix[peak_pos[0]][peak_pos[1]]} at position {peak_pos}")
    print(f"Execution Time: {(end - start) * 1000:.5f} ms")

    run_and_plot()
