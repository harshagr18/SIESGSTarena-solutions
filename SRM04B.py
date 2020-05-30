# http://arena.siesgst.ac.in/contest/SRM04/problem/SRM04B

def TextToNumber(mynum):
    if mynum == "zero": return 0
    elif mynum == "one": return 1
    elif mynum == "two": return 2
    elif mynum == "three": return 3
    elif mynum == "four": return 4
    elif mynum == "five": return 5
    elif mynum == "six": return 6
    elif mynum == "seven": return 7
    elif mynum == "eight": return 8
    else: return 9

x = int(input())
for i in range(x):
    final = []
    sorting = []
    order = []
    nos = list(map(str, input().split(", ")))
    nos[-1] = nos[-1].replace('.', '')
    for j in nos:
        first,second,third = map(str, j.split(" "))
        first = int(TextToNumber(first))
        second = int(TextToNumber(second))
        third = int(TextToNumber(third))
        number = (first * 100) + (second * 10) + third
        final.append(number)
        sorting.append(number)
    sorting.sort(reverse=True)
    for k in sorting:
        for j in range(len(final)):
            if k == final[j]:
                order.append(str(j+1))
    print(' '.join(order))