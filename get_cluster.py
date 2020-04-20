def get_cluster(adjacency_matrix, min_connections):

    ##############
    # Initialize #
    ##############

    n = len(adjacency_matrix)                  # n by n matrix
    cluster = []                               # List to store clustered points
    sub_cluster =[]                            # List to store points connected to clustered points,  but aren't in clusters themselves 
    untraversed_points = [p for p in range(n)] # Where haven't we been?


    ########################
    # Find the first point #
    ########################
    # Start cluster with first point that meets cluster requirements
    starting_point = find_starting_point(adjacency_matrix, min_connections)
    cluster.append(starting_point)   
   

    ###############################################
    # Begin the search for points in this cluster #
    ###############################################

    for point in cluster:                                                     # For points in our cluster list
        for other_point in untraversed_points:                                #   Search through the points we haven't hit
            if adjacency_matrix[point, other_point] == 1:                     #       if they are adjacent
                untraversed_points.remove(other_point)                        #           remove them from the places we haven't hit
                if sum(adjacency_matrix[other_point]) >= min_connections:     #           if they meet min connection requirement
                    cluster.append(other_point)                               #               add it to cluster list
                else:                                                         #           else our adjacent point doesn't meet req
                    sub_cluster.append(other_point)                           #               so it's a subcluster point

    ##########
    # Return #
    ##########

    return cluster, untraversed_points
    # The end