t = int(input())
for tt in range(1,t+1):
    classes, teachers = list(map(int,input().strip().split()))
    teacherArray = []
    for i in range(teachers):
        teacherArray.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    check = True
    for i in range(classes):
        s,p = list(map(int,input().strip().split()))
        S = list(map(int,input().strip().split()))
        P = list(map(int,input().strip().split()))
        
        days = []
        days.append(list(map(str,input().strip().split())))
        days.append(list(map(str,input().strip().split())))
        days.append(list(map(str,input().strip().split())))
        days.append(list(map(str,input().strip().split())))
        days.append(list(map(str,input().strip().split())))
        
        if check:
            for j in range(5):
                day = days[j]
                k = j*7
                for pd in day:
                    if pd[0] == 's':
                        ind = int(pd[1:])
                        if teacherArray[S[ind]-1][k] == 0:
                            teacherArray[S[ind]-1][k] = 1
                        else:
                            check = False
                            break
                        k += 1
                    else:
                        ind = int(pd[1:])
                        if teacherArray[P[ind]-1][k] == 0 and teacherArray[P[ind]-1][k+1] == 0:
                            teacherArray[P[ind]-1][k] = 1
                            teacherArray[P[ind]-1][k+1] = 1
                        else:
                            check = False
                            break
                        k += 2
                if check == False:
                    break
    if check:
        print(tt)