def min_steps(k):
    n = len(k)
    if n <= 1:
        return 0

    graph = {}
    for i in range(n):
        if k[i] in graph:
            graph[k[i]].append(i)
        else:
            graph[k[i]] = [i]

    current = [0]  
    visited = {0}
    steps = 0

    while current:
        next_nodes = []

        for node in current:
            # check if reached end
            if node == n - 1:
                return steps

            # check same value
            for child in graph[k[node]]:
                if child not in visited:
                    visited.add(child)
                    next_nodes.append(child)

            # clear the list to prevent redundant search
            graph[k[node]].clear()

            # check neighbors
            for child in [node - 1, node + 1]:
                if 0 <= child < len(k) and child not in visited:
                    visited.add(child)
                    next_nodes.append(child)

        current = next_nodes
        steps += 1

    return -1

# Driver code
k = [1, 2, 3, 4, 1, 3, 5, 3, 5]
print(min_steps(k))