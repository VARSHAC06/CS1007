class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, v, w):
        if v not in self.adj_list:
            self.adj_list[v] = []
        if w not in self.adj_list:
            self.adj_list[w] = []

        self.adj_list[v].append(w)
        self.adj_list[w].append(v)

    def display(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")

#Example Usage:

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

g.display()
 
