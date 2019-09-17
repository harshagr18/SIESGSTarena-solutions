x = int(input())
for i in range(x):
	n,hp = list(map(int,input().strip().split()))
	dmg = list(map(int,input().strip().split()))
	sum = 0
	for j in dmg:
		if j>0:
			sum = sum + j
	if sum > hp:
		print("unsuccessful")
	else:
		print("successful")