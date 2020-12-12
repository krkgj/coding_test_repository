# 음료수 얼려 먹기 p149 - BFS로 구현
from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

print(graph[2][2])


def bfs(x, y):
    queue = deque()
    # 주어진 범위 내에서 검사하도록 조건 설정
    if graph[x][y] == 0:
        graph[x][y] = 1
        queue.append([x, y])
    elif x < 0 or x >= n or y < 0 or y >= m or graph[x][y] == 1:
        return False

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # BFS로 구현
    while queue:
        x2, y2 = queue.popleft()
        # 현재 x,y 좌표를 기준으로 direction 상하좌우를 살펴 0인 노드를 1로 만들고 큐에 푸쉬한다.
        for w in range(4):
            nx = x2 + dx[w]
            ny = y2 + dy[w]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append([nx, ny])
    return True


result = 0
for i in range(n):  # 0, 1, 2.. n-1
    for j in range(m):  # 0, 1, 2.. m-1
        if bfs(i, j):
            result += 1


print(result)












# # BFS 구현 소스코드 예제 p147
# def bfs(graph, start, visited):
#     queue = deque()
#     queue.append(start)
#     visited[start] = True
#
#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')
#
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# # DFS 구현 소스코드 예제 p142
# def dfs(graph, v, visited):
#     # 현재 노드를 방문 처리
#     visited[v] = True
#     print(v, end=' ')
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#
#
# # 노드 번호가 1부터 시작됨으로 헷갈릴 수 있기에 index 0은 사용하지 않는다.
# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]
#
# # 각 노드가 방문된 정보를 표현 => 1차원 리스트로
# visited = [False for i in range(9)]
#
# bfs(graph, 1, visited)
# dfs(graph, 1, visited)
















# # 인접 리스트 방식 예제 p136
# graph = [[] for _ in range(3)]
#
# graph[0].append((1, 7))
# graph[0].append((2, 5))
#
# graph[1].append((0, 7))
#
# graph[2].append((0, 5))
#
# print(graph)













# # 재귀함수 - 유클리드 호제법(최대공약수 계산)
# def gcd(a, b):
#     if a % b == 0:
#         return b
#
#     return gcd(b, a % b)
#
#
# print(gcd(192, 216))


















# # 재귀함수 - 팩토리얼 예제
# def factorial(n):
#     if n == 1:
#         return 1
#     print(n, "값을 리턴합니다.")
#     return n * factorial(n - 1)
#
#
# print(factorial(12))