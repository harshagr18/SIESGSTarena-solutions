# Problem Link : http://arena.siesgst.ac.in/contest/BETA01/problem/BETA01B

u = int(input())
for _ in range(u):
    balls = int(input())
    piyush = list(map(int,input().split()))
    gokul = list(map(int,input().split()))
    Psum = sum(piyush)
    Gsum = sum(gokul)
    if Psum>Gsum:
        print("Piyush")
    elif Gsum>Psum:
        print("Gokul")
    else:
        if piyush.count(0) > gokul.count(0):
            print("Gokul")
        elif gokul.count(0) > piyush.count(0):
            print("Piyush")
        else:
            print("Draw")