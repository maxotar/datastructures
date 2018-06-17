from collections import defaultdict


class Graph():
    def __init__(self, connetions, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.addConnections(connetions)

    def addConnections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        self._graph[node1].add(node2)  # .add method of set
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        try:
            del self._graph[node]
        except KeyError:
            pass
        for _, values in self._graph.items():
            values.discard(node)

    def isConnected(self, node1, node2):
        return node1 in self._graph and node2 in self._graph[node1]

    def shortestPath(self, node1, node2, path=[]):
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph.keys():
            return None
        shortest = None
        for node in self._graph[node1]:
            if node not in path:
                newpath = self.shortestPath(node, node2, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

# https://www.python.org/doc/essays/graphs/
# https://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python
