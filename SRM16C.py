# Problem Link : http://arena.siesgst.ac.in/contest/SRM16/problem/SRM16C

import math
def power(x, y, p) : 
    res = 1
    x = x % p  
    if (x == 0) : 
        return 0
    while (y > 0) : 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
        y = y >> 1      # y = y/2 
        x = (x * x) % p 
          
    return res
t = int(input())
for _ in range(t):
    N,S = input().strip().split()
    N = int(N)
    sizeS = len(S)
    if N <= sizeS:
        print("0")
    else:
        a = (power(26,N-sizeS,1000000007) * ((sizeS+1)%1000000007))%1000000007
        b = (power(26,N-sizeS-1,1000000007) * (sizeS%1000000007))%1000000007
        ans = (a-b)%1000000007
        print(int(ans))