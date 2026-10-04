def knapsack(weights, values, capacity):

    n = len(weights)

    # DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Build the table
    for i in range(1, n + 1):

        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:

                # Include or exclude the item
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )

            else:
                # Cannot include the item
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Input
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

# Calculate maximum value
result = knapsack(weights, values, capacity)

print("Maximum value:", result)