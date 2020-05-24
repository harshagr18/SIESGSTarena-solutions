x = int(input())
avengers = {
    "light"    : "ironman",
    "magic"    : "doctor strange",
    "strength" : "thor",
    "stealth"  : "black widow",
    "earth"    : "captain america" 
}
for i in range(x):
    rings = []
    for k in range(5):
        a = input()
        rings.append(a)
    for k in range(5):
        print(avengers[rings[k]])