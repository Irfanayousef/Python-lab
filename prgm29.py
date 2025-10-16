def findFactors(number):
    factors=[]
    for i in range(1,number+1):
        if number % i==0:
            factors.append(i)
    return factors
num=int(input("enter the no of rows:"))
result=findFactors(num)
print(f"the factors of {num} are :{result}")
