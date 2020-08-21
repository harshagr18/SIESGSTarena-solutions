x = int(input())
for i in range(x):
    n,r,l = list(map(int, input().split(" ")))
    distance = list(map(int,input().split()))
    for k in distance:
        if k > 150:
            r = r-1
        l = l-k
    if r<=0 or l<= 0:
        print("insufficient")
    else:
        print("sufficient")