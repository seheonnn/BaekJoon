# BFS
import sys
from collections import deque

N = int(sys.stdin.readline()) # 컴퓨터 수
M = int(sys.stdin.readline()) # 연결되어 있는 컴퓨터 쌍의 수
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

def BFS(s): # 시작점인 s 포함하고 시작 -> 마지막에 cnt - 1
    queue = deque()
    queue.append(s)
    check = [0] * (N+1)
    check[s] = 1
    cnt = 0
    while queue:
        x = queue.popleft()
        cnt += 1
        for i in graph[x]:
            if check[i] == 0:
                queue.append(i)
                check[i] = 1
    return cnt

cnt = BFS(1) # 시작점이 1로 고정
print(cnt-1)