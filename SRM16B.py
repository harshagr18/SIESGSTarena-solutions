# Problem Link : http://arena.siesgst.ac.in/contest/SRM16/problem/SRM16B

import math

u = int(input())
for _ in range(u):
    keys = list(map(str, input().split("-")))
    flag = True

    converted = []
    for i in range(len(keys)):
        converted.append(int(keys[i],16))
    
    for i in range(len(keys)):
        for j in range(2,math.ceil(math.sqrt(converted[i]))):
            if converted[i] % j == 0:
                flag = False
                break

    if flag:
        print("YES")
    else:
        print("NO")