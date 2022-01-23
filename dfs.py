class Node:
    def __init__(self,name) -> None:
        self.name =name
        self.children=[]

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

##################
##              A
#        B       C       D
#     E    F         G       H
#        I   J           K
#########################

graph = Node("A")
graph.addChild("B").addChild("C").addChild("D")
graph.children[0].addChild("E").addChild("F")
graph.children[2].addChild("G").addChild("H")
graph.children[0].children[1].addChild("I").addChild("J")
graph.children[2].children[0].addChild("K")

array=[]
print(graph.depthFirstSearch(array))