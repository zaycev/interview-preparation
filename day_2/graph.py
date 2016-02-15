import sys
import collections

class Graph(object):


    def __init__(self):
        self.__nodes = {}
        self.__edges = {}
        self.__adjacent = {}

    def __len__(self):
        return len(self.__nodes)

    def get_adjacent(self, node):
        if node not in self.__nodes:
            raise ValueError("Node is not belong this graph.")
        return self.__adjacent[node]

    def get_edge_weight(self, node_1, node_2):
        if (node_1, node_2) in self.__edges:
            return self.__edges[(node_1, node_2)]
        else:
            raise ValueError("Nodes are not belong this graph.")

    def add_node(self, node, **kwargs):
        if node not in self.__nodes:
            self.__nodes[node] = kwargs
            self.__adjacent[node] = set()
        else:
            self.__nodes[node] = kwargs

    def add_edge(self, node_1, node_2, weight=1.0):
        if node_1 in self.__nodes and node_2 in self.__nodes:
            if (node_1, node_2) not in self.__edges:
                self.__adjacent[node_1].add(node_2)
                self.__edges[(node_1, node_2)] = weight
            else:
                self.__edges[(node_1, node_2)] = weight
        else:
            raise ValueError("Nodes are not belong this graph.")

    def add_bi_edge(self, node_1, node_2, weight=1.0):
        self.add_edge(node_1, node_2, weight)
        self.add_edge(node_2, node_1, weight)

    def iternodes(self):
        return self.__nodes.iteritems()

    def iteredges(self):
        return self.__edges.iteritems()

    def iterdfs(self, node):
        dfs_list = []
        self.__dfs_util(node, lambda n: dfs_list.append(n), set())
        return dfs_list.__iter__()

    def iterbfs(self, node):
        bfs_list = []
        self.__bfs_util(node, lambda n: bfs_list.append(n))
        return bfs_list.__iter__()

    def __dfs_util(self, node, apply_func, visited):
        if node in visited:
            return
        apply_func(node)
        visited.add(node)
        for adj_node in self.__adjacent[node]:
            self.__dfs_util(adj_node, apply_func, visited)

    def __bfs_util(self, node, apply_func):
        visited = {node}
        queue = collections.deque([node])
        while len(queue) > 0:
            cur_node = queue.popleft()
            apply_func(cur_node)
            for adj_node in self.__adjacent[cur_node]:
                if adj_node not in visited:
                    queue.append(adj_node)
                    visited.add(adj_node)

def test():


    g = Graph()

    nodes = [1,2,3,4,5,6]
    for node in nodes:
        g.add_node(node)

    for node in g.iterdfs(1):
        print node
    print

    for node in g.iterbfs(1):
        print node
    print

    for node in g.iternodes():
        print node
    print

    g.add_edge(1, 2, 1.0)
    g.add_edge(2, 3, 1.0)
    g.add_edge(3, 4, 1.0)
    g.add_edge(4, 5, 1.0)
    g.add_edge(2, 6, 1.0)

    print "DFS traversal:"
    for node in g.iterdfs(1):
        print node
    print

    print "BFS traversal:"
    for node in g.iterbfs(1):
        print node
    print

    print "Edges:"
    for e, w in g.iteredges():
        print e, w
    print

    return 0



if __name__ == "__main__":
    sys.exit(test())
