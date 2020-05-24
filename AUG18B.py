from math import ceil

x = int(input())
for i in range(x):
    n,p,a = list(map(int, input().split(" ")))	
    per = 0.75 * n
    need = per - p
    if need > 0:
        if(per + a) > n:
            print("-1")
        else:
            print(ceil(need))
    else:
        print("0")