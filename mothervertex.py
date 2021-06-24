from Stack import MyStack


def dfs(g,vertex):
    num_of_vertices=g.num_of_vertices
    vertices_reached =0

    visited = [False for _ in g.num_of_vertices]
    visited[vertex]=True
    stack = MyStack()
    stack.push(vertex)
    while not stack.is_empty():
        temp_vertex = stack.pop()
        


    return vertices_reached




def find_mother_vertex(g):

    num_of_vertices = g.num_of_vertices
    for vertex in range(num_of_vertices):
        num_of_vertices_reached = dfs(g, vertex)
        if num_of_vertices_reached==num_of_vertices:
            return vertex
    return -1



if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 0)
    g.add_edge(3, 1)
    print(find_mother_vertex(g))
    pass