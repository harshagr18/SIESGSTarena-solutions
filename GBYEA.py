x = int(input())
i = 0
temp = 0
for i in range(x):
	count = 0
	a,b = list(map(int, input().split(" ")))
	ppl = int(input())
	for k in range(ppl):
		c,d = list(map(int, input().split(" ")))
		if c<a and d<a:
			temp = 0
		elif c>b and d>b:
			temp = 0
		else:
			count = count + 1
	if count>0:
		print("Isolate "+ str(count))
	else:
		print("Safe")