import heapq

def make_adjList(graph,u,v,w):
    graph[u].append([w,v])
    graph[v].append([w,u])

def bfs(start,graph,visited):
    queue=[]
    # heapq.heappush(queue,start)
    cost=0
    visited[start]=True
    for element in graph[start]:
        v=element[1]
        w=element[0]
        heapq.heappush(queue,[w,v])
    # print(queue)
    while queue:
        w,u=heapq.heappop(queue)
        print(u,w)
        # print(u,w)
        if visited[u]==False:
            cost+=w
            visited[u]=True
            # print(u)
            for element in graph[u]:
                w=element[0]
                v=element[1]
                heapq.heappush(queue,[w,v])

    return cost



if __name__ == "__main__":
    N=int(input())
    M=int(input())

    graph=[[] for _ in range(N+1)]
    visited=[False for _ in range(N+1)]
    
    for _ in range(M):
        u,v,w=list(map(int,input().split()))
        make_adjList(graph,u,v,w)
    
    print(bfs(1,graph,visited))
    


