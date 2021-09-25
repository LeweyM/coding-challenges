def rotate_matrix(matrix):
    layer = 0
    n = len(matrix)
    while layer < n / 2:
        first = layer
        last = n - 1 - layer
        i = first
        while i < last:
            offset = i - first
            matrix[first][i], matrix[last-offset][first], matrix[last][last-offset], matrix[i][last] = \
                matrix[last-offset][first], matrix[last][last-offset], matrix[i][last], matrix[first][i]
            i += 1
        layer += 1
    return matrix
