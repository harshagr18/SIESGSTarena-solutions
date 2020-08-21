x = int(input())
for i in range(x):
    flag = 0
    a = input()
    if a.count(".") == 3 and ":" not in a:
        nos = a.split(".")
        for k in nos:
            try:    
                if int(k) > 255 or int(k) < 0:
                    flag = 1
            except ValueError:
                flag = 1
            if len(nos) != 4:
                flag = 1
            if k.startswith("0") and len(k) is not 1:
                flag = 1
        if flag == 1:
            print("invalid")
        else:
            print("ipv4")
        

    elif a.count(":") == 7 and "." not in a:
        nos = a.split(":")
        for k in nos:
            if any(letter.isupper() for letter in k):
                flag = 1
            if len(nos) != 8:
                flag = 1
            if k.startswith("0") and len(k) is not 1:
                flag = 1
            try:
                if not bool(int(k,16)):
                    flag = 1
            except ValueError:
                flag = 1

        if flag == 1:
            print("invalid")
        else:
            print("ipv6")


    else:
        print("invalid")