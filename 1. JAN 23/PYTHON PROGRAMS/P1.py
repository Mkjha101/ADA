# --Aim: 1D Peak

# Importing Libraries
import time
import random
import matplotlib.pyplot as mp

# Defining Array of size 'n'
def array(size):
    a=[]
    for i in range (1,size+1):
        a.append(random.randint(1,size))
    return a

# Checking 1D Peak
def Peak(List):
    Num = len(List)
    Peaks = []
    for i in range(Num):
        Peaks.append(0)
    
    stime=time.perf_counter()
    if(len(List)>1):
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
    elif(len(List)==1):
        Peaks[0]=1
    else:
        Peaks=[]
    etime=time.perf_counter()
    Time=(etime-stime)
    PnT=[Peaks,Time]
    '''
    if(Num<=100):
        print("Peaks are at these positions:", Peaks)
    '''
    return PnT

# Basis of 1D Peak Program
def User():
    Num=int(input("Enter number of Elements in List:\t"))
    List=array(Num)
    Ans=Peak(List)
    Peaks=Ans[0]
    Time=Ans[1]
    # Printing Answer
    print("List: ", List, "\nPeaks are: ", Peaks, "\nTime Taken = ", Time)

# Time Complexity for "1D Peak"
def TC():
    m=float(input("Enter Size multiplier:\t"))
    Table1=tuple()
    T=[]
    N=[]
    n=100
    while(n<=10**4):
        Tdiff=0
        List=array(n)
        for i in range(100):
            Ans=Peak(List)
            Time=Ans[1]
            Tdiff+=Time
        Tdiff/=100
        T.append(Tdiff)
        N.append(n)
        n*=m
        n=int(n)
    Table1+=(T,N)
    return Table1

# User Input
In = int(input("\n1. For Sample Program: Enter 0\n2. For Time Complexity Graph: Enter 1\nOption: "))
if(In==0):
    User()
elif(In==1):
    Table=TC()

    # Plotting Time Complexity Graph
    y=Table[0]
    x=Table[1]
    print("Obs:", x, "\nTime:", y)
    
    # Style Edits using ChatGPT
    mp.style.use('bmh')
    mp.figure(figsize=(10, 6))
    
    mp.title("Time Complexity for\n\'1-D Peak\'")
    mp.plot(x,y, marker='o', linewidth=2, color='teal')  # Convert to milliseconds
    mp.xlabel("Observations")
    mp.ylabel("Time")

    # Using ChatGPT
    mp.grid(True, linestyle='--', alpha=0.6)
    mp.tight_layout()
    mp.xticks(fontsize=10)
    mp.yticks(fontsize=10)

    mp.show() #block=false
    #mp.pause(40)
    #mp.close()
else:
    print("\nInvalid Input!")