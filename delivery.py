# Author:        Bryan Yang
# Student ID:    #001303738
# Major:         B.S. Computer Science. Started 10/1/22
# Email:         byang10@wgu.edu
# Date:          12/3/22

import csv
from algo import *
from graph import *

# Load trucks per project constraints.
# Truck load <= 16 packages
# Truck 1: No Constraints other 10:30 delivery deadlines for some packages.
# Truck 2: Packages arriving at 9:05 + can only be delivered by Truck 2.
# Truck 3: Can only be shipped together - 13, 15, 19 and 10:30 delivery deadlines for some packages.
tk1_load = [1, 2, 7, 8, 9, 10, 22, 25, 26, 27, 29, 33]
tk2_load = [3, 5, 6, 12, 17, 18, 28, 30, 31, 32, 36, 37, 38]
tk3_load = [4, 11, 13, 14, 15, 16, 19, 20, 21, 23, 24, 34, 35, 39, 40]
total_distance = 0
status_list = []
delivered = []


# Read distance data from dataframe (csv).
# Return dataframe into a list.
# Big-O Notation: O(n)
def get_dist_data():
    dist_data = []
    with open('WGUPS Distance Table.csv') as csv_dist:
        read_csv_dist = csv.reader(csv_dist, delimiter=',')
        for col in read_csv_dist:
            dist_data.append(col)
    return dist_data


# Add edges using returned csv dataframe from get_dist_data.
# Add weights to edges list.
def get_graph(graph):
    edges = []
    global vertex1
    global vertex2
    df = get_dist_data()
    for col in df:
        graph.add_vertex(Vertex(col[1]))
        # Add vertex addresses to adjacency list in graph object.

    for col in df:
        for i in range(3, len(col)):
            # Starting in column 3 to obtain distances only.
            if col[i] != '':
                edges.append((col[1], df[i - 3][1], float(col[i - 1])))
                # df[i-3][1] get each pair of connect address.

    # Compare vertex 1 and vertex 2 address distance to add proper edges.
    for j in edges:
        for i in graph.adj_list:
            if i.address == j[0]:
                vertex1 = i
            if i.address == j[1]:
                vertex2 = i
        graph.add_edge(vertex1, vertex2, j[2])
        graph.add_edge(vertex2, vertex1, j[2])

    return graph


# Search/Find vertex in adjacency list.
# Big-O Notation: O(n)
def find_vertex(graph, address):
    for i in graph.adj_list:
        if i.address == address:
            return i


# Set starting vertex to hub.
# Start deliver packages.
# Big-O Notation: O(n^3)
def delivery(truck, time):
    not_delivered = []
    start_vertex = (None, '4001 South 700 East')
    _min = None
    _cost = 0
    _pk = None

    # Loops through truck lists and loads trucks.
    if truck.tk_id == 1:
        for i in tk1_load:
            truck.get_package(i)

    if truck.tk_id == 2:
        for i in tk2_load:
            truck.get_package(i)

    if truck.tk_id == 3:
        for i in tk3_load:
            truck.get_package(i)

    # Loops through truck's hash table.
    # Append packages to not delivered list.
    for i in truck.pk_list.hashMap:
        for j in i:
            not_delivered.append((j, j.address))
    not_delivered.append(start_vertex)

    # Algorithm continues unless the list is empty.
    while len(not_delivered) != 0:
        # Remove next start_vertex:
        not_delivered.remove(start_vertex)

        # Get new graph after each interation.
        g = get_graph(Graph())

        # Find matching vertex with matching pacakge address.
        c = find_vertex(g, start_vertex[1])

        # Nearest and shortest path's algorithm object construct to new vertex and graph.
        algo = Greedy(g, c)

        for i in not_delivered:
            # Pacakge address iterates the algorithm on each loop run.
            # Iterates until minimum pacakge is determined.
            al = algo.get_greedy(find_vertex(g, i[1]))

            # If minimum not determined, it is assigned as minimum along within its package group.
            # First process after pacakge delivery.
            if _min is None:
                _min = al
                _cost = _min.min_distance
                _pk = i[0]

            # If new vertex < _min, new vertex is now min and within its pacakge group.
            elif al.min_distance < _min.min_distance and al.address != _min.address:
                _min = al
                _cost = _min.min_distance
                _pk = i[0]

            # If current vertex is match for package 9 And time user input >= 10:20,
            # vertex is removed from not delivered list and package is modified.
            # Add correct vertex to not delivered list.
            elif i[0].pk_id == 9 and al.address == '300 State St' and i[0].hr_to_mn(time) >= 620:
                print('At 10:20AM address for package', i[0].pk_id, 'was corrected from:', al.address)
                not_delivered.remove((i[0], al.address))
                _pk = i[0]
                _pk.address = '410 S State St'
                _min = find_vertex(g, '410 S State St')
                print('To correct Address: ', _min.address)
                not_delivered.append((_pk, _min.address))

        # After pacakge deliveries are complete, find the shortest distance to home hub from last vertex.
        # Compute final distance via adding miles from each edge from trucks to total miles.
        if len(not_delivered) == 0:
            hub = algo.get_greedy(find_vertex(g, '4001 South 700 East'))
            truck.total_cost += hub.min_distance
            global total_distance
            total_distance += truck.total_cost
            return

        # After minimum is determined, add distance traveled to total.
        # Update pacakge delivery timestamps.
        # Set pacakge status to 'delivered.'
        # Add pacakge to delivered list.
        # Assign new start vertex
        # Set minimum weight to none.
        truck.total_cost += _cost
        truck.set_travel_time(truck.total_cost)
        _pk.set_timestamp(truck.total_cost)
        delivered.append(_pk)
        _pk.set_delivered()
        start_vertex = (_pk, _min.address)
        _min = None


