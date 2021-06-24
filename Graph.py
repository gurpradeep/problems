from LinkedList import LinkedList

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []

        for i in range(vertices):
            self.array.append(LinkedList())

    def add_edge(self,source, destination):
        if (source < self.vertices and destination<self.vertices ):
            self.array[source].insert_at_head(destination)

    def print_graph(self):
        for vertex in range(self.vertices):
            print("|",vertex,end="| =>")
            temp = self.array[vertex].get_head()
            while temp is not None:
                print("[",temp.data,end="]->")
                temp = temp.next_element
            print("None")




