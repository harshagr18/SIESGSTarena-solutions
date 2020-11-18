# Problem Link : http://arena.siesgst.ac.in/contest/SRM19/problem/SRM19B

u = int(input())
for _ in range(u):
    s = input()
    a = input()
    cost = 0
    for i in a:
        if i in s:
            s.replace(i,"")
        else:
            cost = cost+1
    print(cost)