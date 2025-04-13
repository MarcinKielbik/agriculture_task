# You are given a 2D binary matrix filled with 0s and 1s representing a rectangular field.
# Each 1 indicates a valid unit of land that can be cultivated.
# Your task is to find the largest square (with all sides equal)
# consisting only of 1s and return the area of that square.

def maximal_square(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])



    dp = [[0] * cols for _ in range(rows)]
    max_side = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    ) + 1
                max_side = max(max_side, dp[i][j])
    return max_side * max_side


matrix = [
    [1, 0, 1, 0],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]

print(maximal_square(matrix))

