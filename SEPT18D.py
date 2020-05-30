x = int(input())
for i in range(x):
    temp = []
    maxstring = []
    costs = list(map(int,input().split()))
    costs.append(1)
    for i in costs:
        if i % 2 == 0:
            temp.append(i)
        else:
            if len(temp)>0:
                maxstring.append(max(temp))
                temp.clear()
    if len(maxstring) == 0:
        print("-1")
    else:
        print(min(maxstring))