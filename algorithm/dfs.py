# encoding: utf-8
# 深度优先搜索

# 相当于先序遍历
# 构造栈
# 存储[当前节点v,下一个要遍历节点在graph[v]的index]


def dfs(adj, start):
    visited = set()
    stack = [[start, 0]]
    print(start)
    visited.add(start)
    while stack:
        (v, next_child_idx) = stack[-1]
        if (v not in adj) or (next_child_idx >= len(adj[v])):
            stack.pop()
            continue
        next_child = adj[v][next_child_idx]
        stack[-1][1] += 1
        if next_child in visited:
            continue
        print(next_child)
        visited.add(next_child)
        stack.append([next_child, 0])


def iter_dfs(G, s):
    S, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        S.add(u)
        item = G.get(u, [])
        # 为了符合先序遍历将数组翻转
        item.reverse()
        Q.extend(item)
        yield u


if __name__ == "__main__":
    # a, b, c, d, e, f, g, h, i = range(9)
    # G = {0: [b, c, d, e, f],  # a
    #      1: [c, e],  # b
    #      2: [d],  # c
    #      3: [e],  # d
    #      4: [f],  # e
    #      5: [c, g, h],  # f
    #      6: [f, h],  # g
    #      7: [f, g],  # h
    #      }
    # print(list(iter_dfs(G, a)))  # [0, 5, 7, 6, 2, 3, 4, 1]

    graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5], 5: [6]}
    dfs(graph, 1)  # 1 4 5 2 3
    print(list(iter_dfs(graph, 1)))  # [1, 2, 4, 5, 3]
