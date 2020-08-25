u = int(input())
for o in range(u):
    count = 0
    comboList = []
    a = int(input())
    intercept = [0 for i in range(a)]

    for i in range(a):  # comboList containing both left and right
        comboList.append(list(map(int,input().split())))

    # Sorting comboList wrt right
    comboList.sort(key=lambda x:x[1])

    for i in range(a): # Main Algo
        if intercept[i] == 0:
            j = i+1
            while j < a:
                if comboList[j][0] <= comboList[i][1]:
                    intercept[j] = 1
                j = j+1
            intercept[i] = 1
            count = count+1
    print(count)
