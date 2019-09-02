# encoding: utf-8
from queue import Queue

num = 4
list_input = [
    [0, 3, 0, 0],
    [3, 0, 3, 0],
    [0, 3, 0, 0],
    [0, 0, 0, 0],
]

searched = {}


# 深度优先搜索
def dfs(obj, start):
    stack = [start]
    while stack:
        u = stack.pop()
        if searched.get(u):
            continue
        next_items = obj.get(u, [])
        next_items.reverse()
        stack.extend(next_items)
        searched[u] = True
        yield u


# 广度优先搜索
def bfs(obj, start):
    q = Queue()
    q.put(start)
    searched[start] = True
    while not q.empty():
        u = q.get()
        for v in obj.get(u, []):
            if searched.get(v):
                continue
            q.put(v)
            searched[v] = True
        yield u


if __name__ == '__main__':
    formatted_input = {}
    for i in range(num):
        for j in range(num):
            item = formatted_input.get(i, [])
            if list_input[i][j] >= 3:
                item.append(j)
            formatted_input[i] = item
    result = {}
    for key in formatted_input.keys():
        if not searched.get(key):
            # result[key] = list(dfs(formatted_input, key))
            result[key] = list(bfs(formatted_input, key))
    print(result)
