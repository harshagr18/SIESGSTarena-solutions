x = int(input())
for z in range(x):
    n,c = map(int, input().split(" "))
    l = [0 for i in range(n)]

    l[0] = 1
    flag = 0

    for i in range(c):
        x,y = map(int, input().split(" "))
        x = x-1
        y = y-1
        if l[x] == 1 and l[y] == 0:
            l[y] = 2
        elif l[y] == 1 and l[x] == 0:
            l[x] = 2
        elif l[x] == 2 and l[y] == 0:
            l[y] = 1
        elif l[y] == 2 and l[x] == 0:
            l[x] = 1
        elif l[x]==1 and l[y]==1:
            flag=1
        elif l[x]==2 and l[y]==2:
            flag=1

    if flag == 0:
        print("yes")
    else:
        print("no")