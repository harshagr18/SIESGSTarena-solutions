x = int(input())
for i in range(x):
    n,k = list(map(int, input().split(" ")))
    rakhis = list(map(int,input().split()))
    num = rakhis[k-1]
    rakhis.sort()
    for i in range(n):
        if rakhis[i] == num:
            print(i)
