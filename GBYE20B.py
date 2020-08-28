# Problem Link : http://arena.siesgst.ac.in/contest/GBYE20/problem/GBYE20B

import bisect
u = int(input())
for _ in range(u):
    n,q = list(map(int, input().split()))
    artists = list(map(str,input().split()))
    songs = list(map(int, input().split()))
    cumulative = [songs[0]]
    for i in range(1,n):
        cumulative.append(cumulative[i-1] + songs[i])
    
    end = cumulative[-1]

    for i in range(q):
        query = int(input())
        if query % end == 0:
            query = end
        else:
            query = query % end
        index = bisect.bisect_left(cumulative,query)
        print(artists[index])