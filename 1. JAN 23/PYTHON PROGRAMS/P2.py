# --Aim: 2D Peak

# Importing Library
import time
import random
import matplotlib.pyplot as mp

# Creating Array of size 'm x n'
def array(rows, cols):
    a=[]
    for i in range (1,rows+1):
        Temp=[]
        for j in range(1,cols+1):
            Temp.append(random.randint(1,rows*cols+1))
        a.append(Temp)
    return a

# Checking 2D Peak
def Peak(cols, rows, Lst1):
    Peaks=[]
    for i in range(rows):
        temp=[]
        for j in range(cols):
            # For the First Array
            if(i==0):
                if(j==0 and i+1<len(Lst1) and j+1<len(Lst1[i])):
                    if(Lst1[i][j]>Lst1[i][j+1] and Lst1[i][j]>Lst1[i+1][j]):
                        temp.append(1)
                    else:
                        temp.append(0)
                elif(j==(cols-1) and i+1<len(Lst1) and j+1<len(Lst1[i])):
                    if(Lst1[i][j]>Lst1[i][j-1] and Lst1[i][j]>Lst1[i+1][j]):
                        temp.append(1)
                    else:
                        temp.append(0)
                else:
                    if(i+1<len(Lst1) and Lst1[i][j]>Lst1[i+1][j] and Lst1[i][j]>Lst1[i][j-1] and Lst1[i][j]>Lst1[i][j+1]):
                        temp.append(1)
                    else:
                        temp.append(0)
            
            # For the Last Array
            elif(i==rows-1):
                if(j==0 and i-1>0):
                    if(Lst1[i][j]>Lst1[i-1][j] and Lst1[i][j]>Lst1[i][j+1]):
                        temp.append(1)
                    else:
                        temp.append(0)
                elif(j==(cols-1) and i-1<len(Lst1)):
                    if(Lst1[i][j]>Lst1[i][j-1] and Lst1[i][j]>Lst1[i-1][j]):
                        temp.append(1)
                    else:
                        temp.append(0)
                else:
                    if(i-1<len(Lst1) and Lst1[i][j]>Lst1[i-1][j] and Lst1[i][j]>Lst1[i][j-1] and Lst1[i][j]>Lst1[i][j+1]):
                        temp.append(1)
                    else:
                        temp.append(0)
            
            # For other Arrays
            else:
                if(j==0):
                    if(j<cols-1 and Lst1[i][j]>Lst1[i-1][j] and Lst1[i][j]>Lst1[i][j+1] and Lst1[i][j]>Lst1[i+1][j]):
                        temp.append(1)
                    else:
                        temp.append(0)
                elif(j==(cols-1) and j-1>0):
                    if(Lst1[i][j]>Lst1[i][j-1] and Lst1[i][j]>Lst1[i-1][j] and Lst1[i][j]>Lst1[i+1][j]):
                        temp.append(1)
                    else:
                        temp.append(0)
                else:
                    if(i-1<len(Lst1) and Lst1[i][j]>Lst1[i+1][j] and Lst1[i][j]>Lst1[i-1][j] and Lst1[i][j]>Lst1[i][j-1] and Lst1[i][j]>Lst1[i][j+1]):
                        temp.append(1)
                    else:
                        temp.append(0)
        Peaks.append(temp)
    return Peaks
Rows=int(input("Enter number of Rows in Matrix:\t"))
Cols=int(input("Enter number of Columns in Matrix:  "))
m=float(input("Enter Size multiplier:\t"))
T=[]
N=[]
while(Rows<=10**3 and Cols<=10**3):
    Tdiff=0
    List=array(Rows, Cols)
    for i in range(100):
        stime=time.perf_counter()
        Peaks=Peak(Cols, Rows, List)
        if(i==0):
            print(Peaks)
        etime=time.perf_counter()
        Tdiff+=(etime-stime)
    Tdiff/=100
    T.append(Tdiff)
    N.append(Rows*Cols)
    Rows*=m; Cols*=m
    Rows=int(Rows); Cols=int(Cols)

# Plotting Time Complexity Graph
print("Obs:", N, "\nTime:", T)

# Style Edits using ChatGPT
mp.style.use('bmh')
mp.figure(figsize=(10, 6))

mp.title("Time Complexity for\n\'2-D Peak\'")
mp.plot(N,T, marker='o', linewidth=2, color='teal')  # Convert to milliseconds
mp.xlabel("Observations")
mp.ylabel("Time")

# Using ChatGPT
mp.grid(True, linestyle='--', alpha=0.6)
mp.tight_layout()
mp.xticks(fontsize=10)
mp.yticks(fontsize=10)

mp.show() #block=false

'''
# --Aim: 2D Peak

import time
import random
import matplotlib.pyplot as mp

# Generate random 2D array of size rows × cols
def generate_array(rows, cols):
    return [[random.randint(1, rows * cols + 1) for _ in range(cols)] for _ in range(rows)]

# Check for 2D Peaks
def find_2d_peaks(matrix, rows, cols):
    peaks = []
    for i in range(rows):
        row_peaks = []
        for j in range(cols):
            current = matrix[i][j]
            top = matrix[i-1][j] if i > 0 else float('-inf')
            bottom = matrix[i+1][j] if i < rows - 1 else float('-inf')
            left = matrix[i][j-1] if j > 0 else float('-inf')
            right = matrix[i][j+1] if j < cols - 1 else float('-inf')

            if current > top and current > bottom and current > left and current > right:
                row_peaks.append(1)
            else:
                row_peaks.append(0)
        peaks.append(row_peaks)
    return peaks

# Main logic
def main():
    random.seed(0)  # For reproducibility

    rows = int(input("Enter number of Rows in Matrix:\t"))
    cols = int(input("Enter number of Columns in Matrix:\t"))
    multiplier = float(input("Enter Size multiplier:\t"))

    N = []  # Problem size (rows × cols)
    T = []  # Execution time

    while rows <= 10**3 and cols <= 10**3:
        total_time = 0
        matrix = generate_array(rows, cols)

        for i in range(100):
            start = time.perf_counter()
            peaks = find_2d_peaks(matrix, rows, cols)
            end = time.perf_counter()
            total_time += (end - start)
            
            if i == 0:
                print("Peak Matrix:")
                for r in peaks:
                    print(r)
                peak_count = sum(sum(row) for row in peaks)
                print(f"Total Peaks Found: {peak_count}")
            

        avg_time = total_time / 100
        T.append(avg_time)
        N.append(rows * cols)

        rows = int(rows * multiplier)
        cols = int(cols * multiplier)

    # Plotting Time Complexity
    print("Observations (n):", N)
    print("Time (s):", T)

    mp.style.use('bmh')
    mp.figure(figsize=(10, 6))
    mp.title("Time Complexity for '2-D Peak'")
    mp.plot(N, T, marker='o', linewidth=2, color='teal')
    mp.xlabel("Matrix Size (rows × cols)")
    mp.ylabel("Avg Execution Time (seconds)")
    mp.grid(True, linestyle='--', alpha=0.6)
    mp.tight_layout()
    mp.xticks(fontsize=10)
    mp.yticks(fontsize=10)
    mp.show()

if __name__ == "__main__":
    main()
'''