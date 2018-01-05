import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.queue import Queue
from datastructures.linkedlist import LinkedList


def exists_route_dfs(directed_graph, u, v):
    """Returns True if there exist a route between nodes u and v
    in directed_graph. Uses DFS.
    """
    def route_dfs(u, v):
        if u is v:
            return True
        u.discovered = True
        for neighbour in u.neighbours:
            if not neighbour.discovered:
                if route_dfs(neighbour, v):
                    return True
        return False

    for v in directed_graph:
        v.discovered = False

    return route_dfs(u, v)


def exists_route_bfs(directed_graph, u, v):
    """Returns True if there exist a route between nodes u and v
    in directed_graph. Uses BFS.
    """
    if u is v:
        return True
    for w in directed_graph:
        w.discovered = False
    q = Queue()
    q.enqueue(u)
    u.discovered = True
    while not q.queue_empty():
        u = q.dequeue()
        for neighbour in u.neighbours:
            if not neighbour.discovered:
                if neighbour is v:
                    return True
                q.enqueue(neighbour)
                neighbour.discovered = True
    return False


class DirectedGraph(object):
    def __init__(self):
        self.V = LinkedList()

    def __iter__(self):
        return self.V.__iter__()

    def add(self, vertex):
        self.V.insert(vertex)


class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.neighbours = LinkedList()
        self.discovered = False

if __name__ == "__main__":
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v1.neighbours.insert(v2)
    v2.neighbours.insert(v3)
    g = DirectedGraph()
    g.add(v1)
    g.add(v2)
    g.add(v3)
    print exists_route_dfs(g, v1, v3)
    print exists_route_bfs(g, v1, v3)
