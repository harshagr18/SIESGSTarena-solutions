# Problem Link : http://arena.siesgst.ac.in/contest/BETA01/problem/BETA01A

u = int(input())
for _ in range(u):
    r,c,n = list(map(int, input().split()))
    if r*c >= n*n:
        print("1")
    else:
        print("0")


# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))