class graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]

    def add_edge(self,vertex1,vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_Vertex(vertex2)
        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)

        if vertex1 not in self.graph[vertex2]:
            self.graph[vertex2].append(vertex1)

    def view_graph(self):
        return self.graph


g=graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_edge('A',"B")
g.add_edge('B',"B")
g.add_edge('A',"B")
print(g.view_graph())