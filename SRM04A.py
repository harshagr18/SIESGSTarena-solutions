# http://arena.siesgst.ac.in/contest/SRM04/problem/SRM04A

x = int(input())
for i in range(x):
    sum = 0
    num = int(input())
    pts = list(map(int,input().split()))
    for i in pts:
        sum = sum + i
    if sum >= num:
        print("Harsh Wins")
    else:
        print(num - sum)