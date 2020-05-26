x = int(input())
for i in range(x):
    a = input()
    s = a.count("s")
    c = a.count("c")
    o = a.count("o")
    b = a.count("b")
    y = a.count("y")
    if(s>=1 and c>=1 and o>=2 and b>=1 and y>=1):
        print("yes")
    else:
        print("no")