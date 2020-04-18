x = int(input())
for i in range(x):
	artist,query = list(map(int, input().split(" ")))
	listart = list(map(str, input().split(" ")))
	listno = list(map(int, input().split(" ")))
	for k in range((len(listno)-1)):
		listno[k+1]=listno[k+1]+listno[k]
	for k in range(query):
		check = int(input())
		while check > listno[(len(listno)-1)]:
			check = check - listno[(len(listno)-1)]
		for j in range(len(listno)):
			if check<=listno[j]:
				print(listart[j])
				break