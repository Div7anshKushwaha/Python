# Read matrix size
m, n = map(int, input().strip().split())

# Read matrix rows
matrix = []
for _ in range(m):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

# Rotating the matrix 90° clockwise:
# Step 1: Reverse the rows
# Step 2: Take the transpose

# Reverse the row order
matrix.reverse()

# Transpose: convert (m x n) → (n x m)
rotated = []
for col in range(n):
    new_row = []
    for row in range(m):
        new_row.append(matrix[row][col])
    rotated.append(new_row)

# Print rotated matrix
for row in rotated:
    print(*row)
