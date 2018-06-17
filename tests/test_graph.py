from datastructures.graph import Graph


connections = [('A', 'B'), ('B', 'C'), ('B', 'D'),
               ('C', 'D'), ('E', 'F'), ('F', 'C')]


def test_directed():
    g = Graph(connections, True)
    assert g._graph == {'A': {'B'},
                        'B': {'D', 'C'},
                        'C': {'D'},
                        'E': {'F'},
                        'F': {'C'}}


def test_undirected():
    g = Graph(connections)
    assert g._graph == {'A': {'B'},
                        'B': {'D', 'A', 'C'},
                        'C': {'D', 'F', 'B'},
                        'D': {'C', 'B'},
                        'E': {'F'},
                        'F': {'E', 'C'}}
    g.add('E', 'D')
    assert g._graph == {'A': {'B'},
                        'B': {'D', 'A', 'C'},
                        'C': {'D', 'F', 'B'},
                        'D': {'C', 'E', 'B'},
                        'E': {'D', 'F'},
                        'F': {'E', 'C'}}
    g.remove('A')
    assert g._graph == {'B': {'D', 'C'},
                        'C': {'D', 'F', 'B'},
                        'D': {'C', 'E', 'B'},
                        'E': {'D', 'F'},
                        'F': {'E', 'C'}}
    g.add('G', 'B')
    assert g.shortestPath('G', 'E') == ['G', 'B', 'D', 'E']
