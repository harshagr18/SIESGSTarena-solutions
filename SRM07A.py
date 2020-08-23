u = int(input())
for o in range(u):
    total = []
    num = int(input())
    x1 = list(map(int,input().split()))
    x2 = list(map(int,input().split()))
    x3 = list(map(int,input().split()))
    x4 = list(map(int,input().split()))
    
    for i in range(num):
        total.append(x1[i]+x2[i]+x3[i]+x4[i])
    print(total)
    
    first = total.index(max(total))
    total[first] = 0

    second = total.index(max(total))
    total[second] = 0

    third = total.index(max(total))
    print(first+1,second+1,third+1)