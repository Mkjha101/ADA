Rows=int(input("Enter number of Rows in Matrix:\t"))
Cols=int(input("Enter number of Columns in Matrix:  "))
Matrix=[]; Peaks=[]

for i in range(Rows):
    Matrix.append([])
    Peaks.append([])
    for j in range(Cols):
        print("Enter element",i+j+1,end="")
        temp=int(input(": "))
        Matrix[i].append(temp)
        Peaks[i].append(0)

print(Matrix, Peaks, sep="\n")

for i in range(Rows):
    for j in range(Cols):
        ;