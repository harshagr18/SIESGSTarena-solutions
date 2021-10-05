y = int(input())
avengers = {
    "light"    : "ironman",
    "magic"    : "doctor strange",
    "strength" : "thor",
    "stealth"  : "black widow",
    "earth"    : "captain america" 
}
for i in range(y):
    rings = []
    for k in range(4):
        a = input()
        rings.append(a)
    for k in range(4):
        print(avengers[rings[k]])