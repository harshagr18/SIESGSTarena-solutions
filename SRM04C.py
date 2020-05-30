x = int(input())
for i in range(x):
    sum = 0
    floors = int(input())
    stairs = list(map(int,input().split()))
    cums = stairs.copy()
    for j in range(len(cums)):
        cums[j] = sum + cums[j] + 1
        sum = cums[j]
    print(stairs,cums)        
    queries = int(input())
    for j in range(queries):
        query = int(input())
        for x in range(len(cums)):
            if query < cums[x]:
                floor = x
                print("Above floor "+str(floor))
                print(abs(query-cums[x-1]))
                print(abs(query-cums[x]))
                break