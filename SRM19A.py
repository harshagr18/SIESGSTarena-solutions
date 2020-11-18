# Problem Link : http://arena.siesgst.ac.in/contest/SRM19/problem/SRM19A

u = int(input())
for _ in range(u):
    n = int(input())
    nums = list(map(int,input().split()))
    op = sum(nums)/2
    print("{:.1f}".format(op))