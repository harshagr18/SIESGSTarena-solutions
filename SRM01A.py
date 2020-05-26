x = int(input())
for i in range(x):
    a = list(map(int,input().split()))
    ones = a.count(1)
    zeroes = a.count(0)
    if ones > zeroes:
        print("1")
    elif ones < zeroes:
        print("0")
    else:
        print("-1")