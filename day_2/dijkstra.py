import sys
import heapq

from graph import Graph


class DijkstraSolver(object):


    def __init__(self, d_graph):
        self.d_graph = d_graph

    def shortest_paths(self, source):
        dist = {node:sys.maxint for node, attrs in self.d_graph.iternodes()}
        pred = {node:None for node, attrs in self.d_graph.iternodes()}
        dist[source] = 0.0
        p_queue = [(d, node) for node, d in dist.iteritems()]
        heapq.heapify(p_queue)
        while len(p_queue) > 0:
            cur_d, cur_node = heapq.heappop(p_queue)
            for next_node in self.d_graph.get_adjacent(cur_node):
                edge_weight = self.d_graph.get_edge_weight(cur_node, next_node)
                new_next_dist = dist[cur_node] + edge_weight
                if new_next_dist < dist[next_node]:
                    dist[next_node] = new_next_dist
                    pred[next_node] = cur_node
                    for i, (d, p_qeueu_node) in enumerate(p_queue):
                        if p_qeueu_node == next_node:
                            p_queue[i] = (new_next_dist, next_node)
                            heapq.heapify(p_queue)
                            break
        return dist.iteritems()



def test():

    g = Graph()

    for node in ["u", "y", "v", "x", "w", "y", "z"]:
        g.add_node(node)

    g.add_bi_edge("u", "v", 2)
    g.add_bi_edge("u", "x", 1)
    g.add_bi_edge("u", "w", 5)

    g.add_bi_edge("v", "x", 2)
    g.add_bi_edge("v", "w", 3)

    g.add_bi_edge("x", "w", 3)
    g.add_bi_edge("x", "y", 1)

    g.add_bi_edge("w", "z", 5)
    g.add_bi_edge("w", "y", 1)
    g.add_bi_edge("y", "z", 1)

    print list(g.iternodes())
    print list(g.iteredges())

    solver = DijkstraSolver(g)

    for node, dist in solver.shortest_paths("u"):
        print node, dist

    return 0


if __name__ == '__main__':
    sys.exit(test())
