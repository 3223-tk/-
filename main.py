import sys
import math
import heapq
def main():
    inpt=sys.stdin.readline
    n,m=map(int,inpt().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w=map(int,inpt().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    dist=[[math.inf,math.inf] for _ in range(n+1)]
    dist[1][0]=0
    queue=[(0,1,0)]
    while queue:
        cost,u,used=heapq.heappop(queue)
        if cost !=dist[u][used]:
            continue
        for v,w in graph[u]:
            new_cost=cost+w
            if new_cost<dist[v][used]:
                dist[v][used]=new_cost
                heapq.heappush(queue,(new_cost,v,used))
            if used==0 and cost<dist[v][1]:
                dist[v][1]=cost
                heapq.heappush(queue,(cost,v,1))
    answer=min(dist[n])
    print(-1 if answer ==math.inf else answer)

if __name__=="__main__":
    main()



