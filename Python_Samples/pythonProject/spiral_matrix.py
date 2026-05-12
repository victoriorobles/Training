def spiral_matrix(size):
    matrix = []
    rows = size
    cols = size
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(i+j)
        matrix.append(row)
    return matrix

print(spiral_matrix(5))