x = int(input())
for i in range(x):
    ticketlist = []
    ticketno = int(input())
    for j in range(ticketno):
        ticket,calc = list(map(str, input().split(" ")))
        num1,calc = list(map(str, calc.split("x")))
        num2,num3 = list(map(str, calc.split("=")))
        num1=int(num1)
        num2=int(num2)
        num3=int(num3)
        if (num1 * num2 != num3):
            ticketlist.append(ticket)
    print(len(ticketlist))
    for j in ticketlist:
        print(j)