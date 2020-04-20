def AdjacencyMatrix(pairwise_distance_matrix, epsilon):
    import numpy as np
    n = len(pairwise_distance_matrix)
    adjacency_matrix = np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            if i == j :
                adjacency_matrix[i, j] = 0
            elif pairwise_distance_matrix[i, j] < epsilon:
                adjacency_matrix[i, j] = 1
            else:
                adjacency_matrix[i, j] = 0
    
    return adjacency_matrix
                    