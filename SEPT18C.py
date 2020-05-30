x = int(input())
for i in range(x):
    flag = 0
    upper = 1
    lower = 1
    number = 1
    a = input()
    if ord(a[0])>=48 and ord(a[0])<=57:
        flag = 1
    if len(a) < 8 or len(a) > 20:
        flag = 1
    for k in a:
        if ord(k)>=48 and ord(k)<=57:
            number = 0
        if ord(k)>=65 and ord(k)<=90:
            upper = 0
        if ord(k)>=97 and ord(k)<=122:
            lower = 0
    if flag == 0 and number == 0 and upper == 0 and lower == 0:
        print("Valid")
    else:
        print("Invalid")