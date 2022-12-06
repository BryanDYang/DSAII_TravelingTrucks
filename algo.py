# Author:        Bryan Yang
# Student ID:    #001303738
# Major:         B.S. Computer Science. Started 10/1/22
# Email:         byang10@wgu.edu
# Date:          12/3/22


# Greedy Algorithm to get nearest or shortest path from starting vertex to other vertices in the graph.
# Algorithm: Given a starting vertex (Distance: 0) and a graph, distance of the starting vertex determines
# each edge weight to its adjacent vertices.
# Big-O Notation: O(E log V)
class Greedy:

    def __init__(self, graph, start_vertex):
        not_visited = []
        # Add all vertices to not visited list
        for current_vertex in graph.adj_list:
            not_visited.append(current_vertex)

        # Start vertex distance is 0 since it's comparing itself.
        start_vertex.min_distance = 0

        # Remove a vertex per iteration of the loop until not_visited list is empty.
        while len(not_visited) > 0:

            # visit each vertex with minimum distance.
            min_index = 0
            for i in range(1, len(not_visited)):
                if not_visited[i].min_distance < not_visited[min_index].min_distance:
                    min_index = i
            current_vertex = not_visited.pop(min_index)
            current_vertex.visited = True

            # Compare path lengths between current vertex to all the neighbors
            for adj_vertex in graph.adj_list[current_vertex]:
                edge_weight = graph.edge_weight[(current_vertex, adj_vertex)]
                alt_path_distance = current_vertex.min_distance + edge_weight

                # If shorter path is found when comparing start_vertex to adj_vertex, update adj_vertex distance and
                if alt_path_distance < adj_vertex.min_distance:
                    adj_vertex.min_distance = alt_path_distance
                    adj_vertex.pre_holder = current_vertex

    # Find shortest or nearest path to a vertex.
    # Return target vertex with assigned distance.
    # Big-O Notation: O(n)
    @staticmethod
    def get_greedy(target_vertex):
        vertex = target_vertex

        while vertex is not None:
            vertex = vertex.prev_holder

        return target_vertex
