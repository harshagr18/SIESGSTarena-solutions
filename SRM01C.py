x = int(input())
for i in range(x):
    num = int(input())
    seq = list(map(int,input().split()))
    qnum = int(input())
    seq.sort()
    for j in range(qnum):
        g,s = list(map(int, input().split(" ")))
        small = seq[(s-1)]
        great = seq[-g]
        print(great - small)