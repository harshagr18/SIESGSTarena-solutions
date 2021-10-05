# Problem Link : http://arena.siesgst.ac.in/contest/GBYE20/problem/GBYE20A

u = int(input())
for _ in range(u):
    startTime, endTime = list(map(int,input().strip().split()))
    n = int(input())
    affected = 0
    for i in range(n):
        personStartTime, personEndTime = list(map(int,input().strip().split()))
        if not(personEndTime < startTime or personStartTime > endTime):
            affected += 1
    if affected == 0:
        print("Safe")
    else:
        print("Isolate",end=" ")
        print(affected)




# Python Program to calculate the square root

# Note: change this value for a different result
num = 8 

# To take the input from the user
#num = float(input('Enter a number: '))

num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))