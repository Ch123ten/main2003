class Graph:
    def __init__(self):
        self.adjList = {}
    
    def addEdge(self, src, dest):
        if src not in self.adjList:
            self.adjList[src] = []
        if dest not in self.adjList:
            self.adjList[dest] = []
        self.adjList[src].append(dest)
        self.adjList[dest].append(src)

    def dfs(self, v, visited = None):
        if not visited:
            visited = set()
        visited.add(v)
        print(v, end=' ')
        for i in self.adjList[v]:
            if i not in visited:
                self.dfs(i, visited)

    def bfs(self, queue, visited = None):
        if not queue:
            return
        v = queue.pop(0)
        if not visited:
            visited = set()
        if v not in visited:
            print(v, end=' ')
        visited.add(v)
        for i in self.adjList[v]:
            if i not in visited:
                queue.append(i)
        self.bfs(queue, visited)
    
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,4)
g.addEdge(3,4)
g.bfs([0])
print("\n")
g.dfs(0)