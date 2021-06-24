from Graph import Graph
from Stack import MyStack


def dfs(g,vertex):
    num_of_vertices=g.vertices
    vertices_reached =0

    visited = [False for _ in range(num_of_vertices) ]
    visited[vertex]=True
    stack = MyStack()
    stack.push(vertex)
    while not stack.is_empty():
        current_node = stack.pop()
        temp = g.array[current_node].head_node
        while temp is not None:
            if not visited[temp.data]:
                stack.push(temp.data)
                visited[temp.data]=True
                vertices_reached+=1
            temp = temp.next_element
    
    return vertices_reached+1

def find_mother_vertex(g):

    for vertex in range(g.vertices):
        num_of_vertices_reached = dfs(g, vertex)
        if num_of_vertices_reached==g.vertices:
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