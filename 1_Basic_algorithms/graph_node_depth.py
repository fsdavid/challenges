
def get_depth(graph, parent, node):
    """
    Returns a depth of the given node inside the directed acyclic graph .
    (E. g. if the graph is designed as "A--B--C" where A is
     the parent node and we need to find depth of C, 2 should 
     be returned as a shortest number of the edges from A to C.)

    Parameters
    ----------
    graph : Adjacency matrix of the graph
    parent : Index of the parent node
    node : Index of the desired node to find the depth
    """
    
    length = 0

    def find_parent(nodeIndex, l):
        i = 0
        while i < len(graph):
            if graph[i][nodeIndex] > 0 and i != node:
                if i == parent:
                    nonlocal length
                    length = l if length == 0 or l < length else length
                    break
                else: 
                    find_parent(i, l + 1)
            i += 1

    find_parent(node, 1)
    return length if length > 0 else -1