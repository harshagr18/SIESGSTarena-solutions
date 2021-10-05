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
        print("SAFEST")
    else:
        print("AKELA CHOD",end=" ")
        print(affected)