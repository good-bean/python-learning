# Graphs are data structures representing relations between pairs of
# elements. These elements, called nodes, can be real-life objects,
# entities, points in space or others. The connections between the
# nodes are called the edges.

# Each node is a list of tuples, where the first element is the connected
# node, and the second element is the distance.
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

# Defining a function to calculate the shortest path between each
# node in the graph
def shortest_path(graph, start, target = ''):
    # Keeping track of visited nodes in a list to be removed once visited
    unvisited = list(graph)
    # Get currently known shortest distances between start-[other nodes]
    distances = {
        # starts from '0' -> distance from node-self == 0
        node: 0 if node == start
        # set all others to infinite
        else float('inf')
        for node in graph
    }
    paths = {
        # generate lists for nodes and their paths
        node: [] for node in graph
    }
    # add node to its own list as starting point
    paths[start].append(start)
   
    while unvisited:
        # comparison depends on value rather than key
        current = min(unvisited, key=distances.get)
        # iterate over tuples in graph[current]
        for node, distance in graph[current]:
            # compare next node's distance + current distance
            # with the current known distance for the next node
            # if true, a shorter path has been found
            if distance + distances[current] < distances[node]:
                # update node distance
                distances[node] = distance + distances[current]
                # if node path not empty and is last node is the next node
                if paths[node] and paths[node][-1] == node:
                    # assign copy of current path to the node path
                    paths[node] = paths[current][:]
                # add current node path to the next node
                else:
                    paths[node].extend(paths[current])
                # append next node to its path
                paths[node].append(node)
        # remove current node from unvisited list
        unvisited.remove(current)
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            # omit starting node from target list
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')

    return distances, paths

shortest_path(my_graph, 'A', 'F')
