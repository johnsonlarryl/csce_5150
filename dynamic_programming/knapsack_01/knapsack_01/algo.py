from typing import List, Tuple

def knapsack(weights: int, profits: List[int], capacity: int) -> Tuple[int, int]:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Print initial row
    print("Initial DP table:")
    print(dp[0])

    # Build DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]

            else:
                dp[i][w] = max(
                    dp[i-1][w],
                    profits[i-1] + dp[i-1][w - weights[i-1]]
                )

        # Print row after each item is processed
        print(
            f"\nItem {i} "
            f"(weight={weights[i-1]}, profit={profits[i-1]}):"
        )
        print(dp[i])

    # ------------------------------------
    # Print complete DP matrix
    # ------------------------------------

    print("\n\nFinal DP Matrix:")
    print("\n       Capacity")

    print("       ", end="")
    for w in range(capacity + 1):
        print(f"{w:5}", end="")
    print()

    print("       " + "-" * (5 * (capacity + 1)))

    for i in range(n + 1):
        print(f"{i:<7}", end="")

        for value in dp[i]:
            print(f"{value:5}", end="")

        print()

    # ------------------------------------
    # Find selected items
    # ------------------------------------

    w = capacity
    selected_items = []

    for i in range(n, 0, -1):

        # Value changed, so item i was selected
        if dp[i][w] != dp[i-1][w]:

            selected_items.append(i-1)

            # Reduce remaining capacity
            w -= weights[i-1]

    selected_items.reverse()

    # ------------------------------------
    # Print selected items
    # ------------------------------------

    print("\nSelected Items:")

    total_weight = 0
    total_profit = 0

    for index in selected_items:

        item_number = index + 1
        weight = weights[index]
        profit = profits[index]

        print(
            f"Item {item_number}: "
            f"Weight = {weight}, "
            f"Profit = {profit}"
        )

        total_weight += weight
        total_profit += profit

    print(f"\nTotal Weight: {total_weight}")
    print(f"Maximum Profit: {total_profit}")

    return selected_items, total_profit