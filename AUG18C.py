x = int(input())
l=['r','a','h','u','l']
for i in range(x):
    s = input()
    new = ""
    for j in range(len(s)):
        if(s[j] not in l):
            new = new+s[j]
    print(new)