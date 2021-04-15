def is_split_possible(graph):
    color = {}
    def dfs(pos):
        for i in graph[pos]:
            if i in color:
                if color[i] == color[pos]:
                    return False
            else:
                color[i] = 1 - color[pos]
                if not dfs(i):
                    return False
        return True
    for i in range(len(graph)):
        if i not in color:
            color[i] = 0
            if not dfs(i):
                return False
    return True

# Driver code
graph = [[3], [2, 4], [1], [0, 4], [1, 3]]
print(is_split_possible(graph))