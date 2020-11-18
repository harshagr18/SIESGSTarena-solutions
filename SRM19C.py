# Problem Link : http://arena.siesgst.ac.in/contest/SRM19/problem/SRM19C

u = int(input())
for _ in range(u):
    a,b = list(map(int, input().split()))
    for i in range(b,a+1):
        if a % i == 0 and i % b == 0:
            print(i)
            break