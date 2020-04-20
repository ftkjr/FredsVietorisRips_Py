def FredsDBSCAN(adjacency_matrix, minimum_connections):

    ##############
    # Initialize #
    ##############
    l = list()


    while len(untraversed_points) > 0:                                                  # While there are still points left to traverse
      l[i], untraversed_points =  get_cluster(adjacency_matrix, minimum_connections)    #   Get clusters, and update untraversed points
      i+=1                                                                              #   move to next cluster
    
    return l