t=int(input())
s=0
for i in range(t):
    n=int(input())
    a = list(map(int, input().split()))
    d=len(a)-len(set(a))
    if d == 0:
        print(d)
    s=s+d
print(s)