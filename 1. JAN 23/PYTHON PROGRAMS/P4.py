import time
import matplotlib.pyplot as mp
import math

# Function to compute a^b using Divide and Conquer
def power(a, b):
    if b == 0:
        return 1
    half = power(a, b // 2)
    if b % 2 == 0:
        return half * half
    else:
        return a * half * half

# Graph & Timing Logic
def run_and_plot():
    a = 2  # fixed base
    exponents = list(range(1000, 100001, 5000))  # Increasing b values
    repeats = 100  # Repeat to amplify measurable time
    times = []
    for b in exponents:
        start = time.time()
        for _ in range(repeats):
            power(a, b)
        end = time.time()
        avg_time = (end - start) / repeats
        times.append(avg_time * 1000)  # in ms

    # Theoretical log b curve (scaled for visual comparison)
    log_curve = [math.log2(b) * 0.01 for b in exponents]

    # Plotting both curves
    mp.plot(exponents, times, marker='o', label='Actual Time', color='purple')
    mp.plot(exponents, log_curve, linestyle='--', label='~ log₂(b)', color='red')

    mp.title("Time Complexity Graph: a^b using Divide and Conquer")
    mp.xlabel("Exponent b")
    mp.ylabel("Execution Time (ms)")
    mp.legend()
    mp.grid(True)
    mp.show()

# Main execution
if __name__ == "__main__":
    a = int(input("Enter base (a): "))
    b = int(input("Enter exponent (b): "))
    
    start = time.time()
    result = power(a, b)
    end = time.time()

    print(f"{a}^{b} = {result}")
    print(f"Execution Time: {(end - start) * 1000:.5f} ms")

    # Plot time complexity graph
    run_and_plot()
