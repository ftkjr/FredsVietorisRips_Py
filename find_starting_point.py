def find_starting_point(adjacency_matrix, untraversed_points, minimum_connections):
    starting_point = 0  
    while sum(adjacency_matrix[starting_point]) < minimum_connections:
        starting_point += 1
        if starting_point == len(adjacency_matrix):
            raise Exception('No point of the {} given met the minimum connection requirement. Consider reducing your minimum connections and try again.'.format(len(adjacency_matrix)))

    untraversed_points.remove(starting_point)
    return starting_point, untraversed_points
