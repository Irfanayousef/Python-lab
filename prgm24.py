def disp_pyramidal(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i * j,end=" ")
        print()
n=int(input("enter the number of step:"))
if n <1:
    print("Please enter a positive integer")
else:
    disp_pyramidal(n)
