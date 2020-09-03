# Problem Link : http://arena.siesgst.ac.in/contest/BETA01/problem/BETA01A

u = int(input())
for _ in range(u):
    r,c,n = list(map(int, input().split()))
    if r*c >= n*n:
        print("1")
    else:
        print("0")