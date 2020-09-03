# Problem Link : http://arena.siesgst.ac.in/contest/BETA01/problem/BETA01C

u = int(input())
for _ in range(u):
    string = input()
    string = string.replace("a","n")
    string = string.replace("s","i")
    string = string.replace("h","n")
    string = string.replace("o","a")
    string = string.replace("k","d")
    print(string)