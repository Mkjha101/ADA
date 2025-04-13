# --Aim: 1D Peak

# Importing Libraries
import time
import random
import matplotlib.pyplot as mp

# Defining Array of size 'n'
def array(size):
    a=[]
    for i in range (1,size):
        a.append(random.randint(1,size))
    a.append(size+100)
    return a

# Checking 1D Peak
def Peak(List):
    Num = len(List)
    Peaks = []
    for i in range(Num):
        Peaks.append(0)
    
    stime=time.perf_counter()
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
    etime=time.perf_counter()
    Time=(etime-stime)
    print("Peaks are at these positions:", Peaks)
    return Time

# Basis of 1D Peak Program
def User():
    Num=int(input("Enter number of Elements in List:\t"))
    List=[]

    for i in range(Num):
        print("Enter element",i+1,end="")
        temp=int(input(": "))
        List.append(temp)
    
    Time=Peak(List)
    # Printing Answer
    print("\nTime Taken = ",Time)

# Time Complexity for "1D Peak"
def TC():
    m=float(input("Enter Size multiplier:\t"))
    Table1=tuple()
    T=[]
    N=[]
    while(n<=10**6):
        Tdiff=0
        List=array(n)
        for i in range(100):
            Time=Peak(List)
            Tdiff+=Time
        Tdiff/=100
        T.append(Tdiff)
        N.append(n)
        n*=m
        n=int(n)
    Table1+=(T,N)
    return Table1

# User Input
In = int(input("Enter 0 for Sample Program\tand\t1 for Time Complexity Graph for 1d Peak:\n"))
if(In==0):
    User()
else:
    Table=TC()

# Plotting Time Complexity Graph
y=Table[0]
x=Table[1]
mp.title("Time Complexity for\nLinear Search using Iteration")
mp.plot(x,y)
mp.xlabel("Observations")
mp.ylabel("Time")
mp.show()