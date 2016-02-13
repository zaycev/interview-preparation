import sys


class Graph(object):
    """ Minimalistic class for directed graph with the following properties:
        * loops and self-loops are allowed.
        * parallel edges are not allowed.
    """

    class BaseNode(object):

        def __init__(self, id, data):
            self.id = id
            self.data = data

        def __repr__(self):
            return "<Node(%d, %r)>" % (self.id, self.data)
 
    def __init__(self):
        self.__nodes = {}         # Maps node id to node.
        self.__adjacent = {}      # Maps node id to a set of adjacent nodes.
        self.__edges = set()      # Set of pairs representing edges.
        self.__node_counter = 0   # Used for generating IDs for new nodes.

    def iternodes(self):
        return self.__nodes.itervalues()

    def iteredges(self):
        for node_1_id, node_2_id in self.__edges:
            yield self.__nodes[node_1_id], self.__nodes[node_2_id]

    def iterdfs(self, node):
        dfs_list = []
        self.__dfs(node, lambda n: dfs_list.append(n), set())
        return dfs_list.__iter__()

    def is_dag(self):
        raise NotImplemented()

    def itertopological(self):

        # Take all edges and find nodes with incoming degree
        # equal to 0 (origins). Connect them with "Super Origin".
        origins = set(self.__nodes.keys())
        for node_1_id, node_2_id in self.__edges:
            if node_2_id in origins:
                origins.remove(node_2_id)

        s_origin = self.create_node("S")
        for origin_id in origins:
            origin = self.__nodes[origin_id]
            self.create_edge(s_origin, origin)

        # Start DFS from super origin and populate visited list
        # every time we exit from a node.
        topological_list = []
        visited = set()
        self.__topological_dfs(s_origin.id, visited, topological_list)

        # Assert that super origin is in the end of 
        # the topological list.
        assert topological_list[-1] == s_origin.id

        # Remove super origin from the graph.
        for origin_id in origins:
            self.__edges.remove((s_origin.id, origin_id))
        del self.__adjacent[s_origin.id]
        del self.__nodes[s_origin.id]

        # Return topological list in a reversed order
        # without the first element.
        topological_list_iter = reversed(topological_list)
        next(topological_list_iter)
        for node_id in topological_list_iter:
            yield self.__nodes[node_id]

    def create_node(self, data):
        node = self.BaseNode(self.__node_counter, data)
        self.__node_counter += 1
        self.__nodes[node.id] = node
        self.__adjacent[node.id] = set()
        return node

    def create_edge(self, node_1, node_2):
        if node_1.id in self.__nodes and node_2.id in self.__nodes:
            if (node_1.id, node_2.id) not in self.__edges:
                self.__edges.add((node_1.id, node_2.id))
                self.__adjacent[node_1.id].add(node_2.id)

    def remove_edge(self, node_1, node_2):
        pass

    def __dfs(self, node, apply_func, visited):
        if node.id in visited:
            return
        apply_func(node)
        visited.add(node.id)
        for adj_node_id in self.__adjacent[node.id]:
            adj_node = self.__nodes[adj_node_id]
            self.__dfs(adj_node, apply_func, visited)

    def __topological_dfs(self, node_id, visited, topological_list):
        """
        Slightly modified DSF for topological sort.
        """
        if node_id in visited:
            return
        visited.add(node_id)
        for adj_node_id in self.__adjacent[node_id]:
            self.__topological_dfs(adj_node_id, visited, topological_list)
        topological_list.append(node_id)


def test():

    g = TopologicalGraph()

    a = g.create_node("a")
    b = g.create_node("b")
    c = g.create_node("c")
    d = g.create_node("d")
    e = g.create_node("e")

    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(a, d)
    g.add_edge(a, e)

    g.add_edge(b, d)
    g.add_edge(c, d)
    g.add_edge(c, e)
    g.add_edge(d, e)

    g.topological(lambda node: sys.stdout.write(node.data+"\n"))

    return 0


if __name__ == "__main__":
    sys.exit(test())
