from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)


def topologicalSort(myGraph):

    visited=[False for _ in range(myGraph.vertices)]

    for k,v in myGraph.graph.items():
        for i in range(len(myGraph.graph[k])):
            if not visited[v[i]]:
                visited[v[i]]=True

    
    for i in range(len(visited)):
        if visited[i]==False:
            return i

    

        



myGraph = Graph(5)
myGraph.addEdge(0,1)
myGraph.addEdge(0,3)
myGraph.addEdge(1,2)
myGraph.addEdge(2,3)
myGraph.addEdge(2,4)
myGraph.addEdge(3,4)
print(topologicalSort(myGraph))
