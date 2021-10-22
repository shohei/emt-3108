#!/usr/bin/env python
class Edge():
    def __init__(self, to, w):
        self.to = to
        self.w = w

G = [[Edge(1,3),Edge(2,5)],
     [Edge(2,3),Edge(3,12)],
     [Edge(3,9),Edge(4,4)],
     [Edge(5,2)],
     [Edge(3,7),Edge(5,8)],
     []]

INF = 9999
N = len(G)

def chmin(a,b):
    if a<=b:
        return a 
    else:
        return b 

used = [False]*N
dist = [INF]*N
s = 0
dist[s] = 0
for i in range(N):
    min_dist = INF
    min_v = -1
    for v in range(N):
        if used[v]==False and dist[v] < min_dist:
            min_dist = dist[v]
            min_v = v

    if min_v==-1:
        break

    for edge in G[min_v]:
        dist[edge.to] = chmin(dist[edge.to], dist[min_v]+edge.w)
    
    used[min_v] = True

for v in range(N):
    if dist[v] < INF:
        print(dist[v])
    else:
        print("INF")


