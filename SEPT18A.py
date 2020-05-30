x = int(input())
for i in range(x):
    ap = 0
    bp = 0
    a,b,c = list(map(int, input().split(" ")))
    while c != 1:
        if a % c == 0:
            ap = ap + 1
            a = a - 1
        elif b % c == 0:
            bp = bp + 1
            b = b - 1
        else:
            c = c - 1
    if (ap > bp ):
        print("A")
    elif (bp > ap):
        print("B")
    else:
        print("Draw")