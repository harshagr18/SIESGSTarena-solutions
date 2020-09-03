# Problem Link : http://arena.siesgst.ac.in/contest/GBYE19/problem/GBYE19A

u = int(input())
for _ in range(u):
    no = int(input())
    if no%3 == 0:
        print("greyhound")
    else:
        print("untilone")