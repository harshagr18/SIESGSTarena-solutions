# Problem Link : http://arena.siesgst.ac.in/contest/GBYE20/problem/GBYE20D

from collections import defaultdict

u = int(input())
for _ in range(u):
    overs = int(input())
    bowlers = list(map(int, input().split()))
    mydict = defaultdict(int)
    for i in bowlers:
        mydict[i] += 1
    ans = "successful"
    for i in mydict.keys():
        if mydict[i] % 2 != 0:
            ans = "unsuccessful"
            break
    print(ans)