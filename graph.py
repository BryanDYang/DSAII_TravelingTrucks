# Author:        Bryan Yang
# Student ID:    #001303738
# Major:         B.S. Computer Science. Started 10/1/22
# Email:         byang10@wgu.edu
# Date:          12/3/22

# Vertex class for addresses.
# Big-O Notation: O(n)
class Vertex:
    # Initialize address, visited, predecessor, minimum distance.
    def __init__(self, address):
        self.address = address
        self.visited = False
        self.prev_holder = None
        self.min_distance = float('inf')

    # Compare minimum distance to other minimum distance.
    def __cmp__(self, other):
        return self.cmp(self.min_distance, other.min_distance)

    # Compare priority based on minimum distance between addresses.
    def __lt__(self, other):
        self_priority = self.min_distance
        other_priority = other.min_distance
        return self_priority < other_priority


# Graph used nearest neighbor algorithm.
# Big-O: O(n)
class Graph:
    def __init__(self):
        # List of connected vertices of each vertex (adjacency list).
        self.adj_list = {}
        # Key dictionary for two vertices: edge weight
        self.edge_weight = {}

    # Add vertex if it is not in adjacency list.
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    # Add edge based on comparison vertices.
    def add_edge(self, vertexA, vertexB, weight):
        if weight != '':
            self.edge_weight[vertexA, vertexB] = weight
            self.edge_weight[(vertexB, vertexA)] = weight
            self.adj_list[vertexA].append(vertexB)

    # Edge weight between two vertices
    # Big-O Notation|Space-Time Complexity: O(n)
    def get_weight(self, vertexA, vertexB):
        if self.edge_weight[vertexA, vertexB]:
            weight = self.edge_weight[vertexA, vertexB]
            return weight
        elif self.edge_weight[vertexB, vertexA]:
            weight = self.edge_weight[vertexB, vertexA]
            return weight
