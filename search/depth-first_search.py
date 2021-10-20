#!/usr/bin/env python

def search(G,s):
    N = len(G)
    seen = [False]*N
    todo = []
    seen[s] = True
    todo.append(s)
    while(todo!=[]):
        print(todo)
        v = todo[-1]
        todo = todo[:-1] 
        for x in G[v]:
            if (seen[x]):
                continue
            seen[x] = True
            print(x,"True")
            todo.append(x)
    return seen

G = [(1,4,2),(0,3,8),(0,5),(1,7,8),(0,8),(2,6,8),(5,7),(3,6),(1,3,4,5)]
print(search(G,0))


