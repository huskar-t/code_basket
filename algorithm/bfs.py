# encoding: utf-8
# 广度优先搜索

from queue import Queue


def bfs(adj, start):
    visited = set()
    q = Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        print(u)
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v)
                q.put(v)


if __name__ == '__main__':
    graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
    bfs(graph, 1)
