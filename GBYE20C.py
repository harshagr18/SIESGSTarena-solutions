# Problem Link : http://arena.siesgst.ac.in/contest/GBYE20/problem/GBYE20C

u = int(input())
for _ in range(u):
    n = int(input())
    eff = list(map(int, input().split(" ")))
    rat = list(map(int,input().split()))
    k = int(input())
    d = int(input())

    final = []

    for i in range(n):
        curr = eff[i]
        ans = curr

        for j in range(d - 1):
            curr = curr - (curr/rat[i])
            ans = ans + curr
        
        final.append(ans)
    
    final.sort(reverse=True)
    ans = 0
    for i in range(k):
        ans = ans + final[i]
    print(int(ans))