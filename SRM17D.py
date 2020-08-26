# Problem Link : http://arena.siesgst.ac.in/contest/SRM17/problem/SRM17D

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    if n > 3 and n % 2 == 0:
        ans = "NO"
        for i in range((n//2) + 1):
            cp = arr[::]
            if cp[0] > cp[-1]:
                cp[0],cp[-1] = cp[-1], cp[0]
            for j in range(1,n-2,2):
                if cp[j] > cp[j+1]:
                    cp[j],cp[j+1] = cp[j+1],cp[j]
            check = True
            for j in range(n-1):
                if cp[j] > cp[j+1]:
                    check = False
                    break
            if check:
                ans = "YES"
                break
            else:
                arr = arr[-2:] + arr[:-2]
        print(ans)
    else:
        print("YES")