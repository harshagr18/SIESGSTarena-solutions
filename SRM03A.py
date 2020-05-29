x = int(input())
for i in range(x):
    ans = 0
    a,b,c = list(map(int, input().split(" ")))
    max1 = a+b+c
    max2 = a+b*c
    max3 = a*b+c
    max4 = a*b*c
    print(max(max1,max2,max3,max4))