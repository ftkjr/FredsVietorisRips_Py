def PairwiseDistanceMatrix(x, y):
    import numpy as np
    n = len(x)
    
    distance_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            distance_matrix[i, j] = Euclideandist(x[i], y[i], x[j], y[j])

    return distance_matrix
