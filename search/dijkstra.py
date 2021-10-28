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
prev_nodes = [-1]*N

used = [False]*N
dist = [INF]*N
start = 0
dist[start] = 0
prev_nodes[start]=-1
for _ in range(N):
    min_dist = INF
    min_v = -1
    for v in range(N):
        if used[v]==False and dist[v] < min_dist:
            min_dist = dist[v]
            min_v = v

    if min_v==-1:
        break

    for edge in G[min_v]:
        if dist[edge.to] > dist[min_v]+edge.w:
            dist[edge.to] = dist[min_v]+edge.w
            prev_nodes[edge.to] = min_v
    
    used[min_v] = True

def get_optimal_path(v):
    prev_node = v
    path = []
    while prev_node!=-1:
        path.append(prev_node)
        prev_node = prev_nodes[prev_node]
    path.reverse()
    return path

for v in range(N):
    if dist[v] < INF:
        print(f"Shortest path for {start}->{v}")
        print(f"  length:{dist[v]}")
        print(f"  path:{get_optimal_path(v)}")
    else:
        print(f"Shortest path length {start}->{v}: not found")
