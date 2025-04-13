# --Aim: 1D Peak

# Importing Libraries
import time
import random
import matplotlib.pyplot as mp

# Checking 1D Peak
def Peak(List):
    Num = len(List)
    Peaks = []
    for i in range(Num):
            if(i>0 and i<Num-1):
                if(List[i]>List[i-1] and List[i]>List[i+1]):
                    Peaks[i]=1
            if(i==0):
                if(List[i]>List[i+1]):
                    Peaks[i]=1
            if(i==Num-1):
                if(List[i]>List[i-1]):
                    Peaks[i]=1

# Basis of 1D Peak Program
def User():
    Num=int(input("Enter number of Elements in List:\t"))
    List=[]

    for i in range(Num):
        print("Enter element",i+1,end="")
        temp=int(input(": "))
        List.append(temp)
    st=time.time()
    Peaks=Peak(List)
    et=time.time()
    time=(et-st)
    # Printing Answer
    print("Peaks are at these positions:", Peaks, "\nTime Taken = ",time)

# Time Complexity for "1D Peak"
def TC():
    ""

# User Input
In = int(input("Enter 0 for Sample Program\tand\t1 for Time Complexity Graph for 1d Peak:\n"))
if(In==0):
    User()
else:
    ""