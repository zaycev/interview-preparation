import heapq
import sys

from graph import Graph





class AStarSolver(object):

    def __init__(self, d_graph, h_func):
        self.d_graph = d_graph
        self.h_func = h_func

    def find_path(self, source, goal):

        if source == goal:
            return 0, [], 0

        goal_node_attr = self.d_graph.get(goal)
        dist = {source:0.0}
        pred = {node:None for node, attrs in self.d_graph.iternodes()}
        p_queue = [(0, source)]
        steps = 0

        while len(p_queue) > 0:

            _, cur_node = heapq.heappop(p_queue)

            # Used for debugging.
            steps += 1

            if cur_node == goal:
                ""
                break

            for next_node in self.d_graph.get_adjacent(cur_node):
                
                edge_weight = self.d_graph.get_edge_weight(cur_node, next_node)
                distance = dist[cur_node] + edge_weight

                # Priority is equal to the cost to the next node + estimation to
                # the goal node. In Dijkstra, estimation = 0.
                next_node_attr = self.d_graph.get(next_node)
                priority = distance + self.h_func(next_node_attr, goal_node_attr)

                if next_node not in dist or distance < dist[next_node]:

                    # Add or update priority of the next node with new estimation.
                    if next_node not in dist:
                        heapq.heappush(p_queue, (priority, next_node))
                    else:
                        # O(n) search. This might be optimized.
                        for i, (_, node) in enumerate(p_queue):
                            if node == next_node:
                                p_queue[i] = (priority, next_node)
                                heapq.heapify(p_queue)
                                break


                    # Update Dijkstra's dist to the current node.
                    dist[next_node] = distance
                    pred[next_node] = cur_node

        # Decode shortest path.
        cost = dist[goal]
        prev = pred[goal]
        path = [goal]
        while prev is not None:
            path.append(prev)
            prev = pred[prev]

        return cost, list(reversed(path)), steps



def test():
    

    g = Graph()

    for y in xrange(0, 4):
        for x in xrange(1, 5):
            node = y * 4 + x
            print node, {"x": x, "y": y+1}
            g.add_node(node, x=x, y=y+1)

    # 1
    g.add_bi_edge(1,2)
    g.add_bi_edge(1,5)

    # 2
    g.add_bi_edge(2,6)
    g.add_bi_edge(2,3)

    # 3
    g.add_bi_edge(3,7)
    g.add_bi_edge(3,4)

    # 4
    g.add_bi_edge(4,8)

    # 5
    g.add_bi_edge(5,9)
    g.add_bi_edge(5,6)

    # 6
    g.add_bi_edge(6,10)

    # 7
     
    # 8
    g.add_bi_edge(8, 12)

    # 9
    g.add_bi_edge(9, 13)

    # 10
    g.add_bi_edge(10, 14)
    g.add_bi_edge(10, 11)

    # 11

    # 12
    g.add_bi_edge(12, 16)

    # 13
    g.add_bi_edge(13, 14)

    # 14
    g.add_bi_edge(14, 15)

    # 15

    # 16
    

    def greedy_h(n1, n2):
        return abs(n1["x"] - n2["x"]) + abs(n1["y"] - n2["y"])

    astar_solver = AStarSolver(g, greedy_h)

    print
    print astar_solver.find_path(1, 16)
    print astar_solver.find_path(8, 16)
    print

if __name__ == "__main__":
    sys.exit(test())
