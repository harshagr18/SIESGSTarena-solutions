u = int(input())
for o in range(u):
    s = input()
    m = int(input())
    merit = 0
    for i in s:
        if i == "C":
            merit = merit+2000
        if i == "R":
            merit = merit-500
        if i == "F":
            merit = merit-200
    if merit >= m:
        print("yes")
    else:
        print("no")