# Program for 1D Peak
Num=int(input("Enter number of Elements in List:\t"))
List=[]; Peaks=[]

for i in range(Num):
    print("Enter element",i+1,end="")
    temp=int(input(": "))
    List.append(temp)
    Peaks.append(0)

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

# Printing Answer
print("Peaks are at these positions:", Peaks)