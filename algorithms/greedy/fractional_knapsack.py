# A naive recursive implementation
# of 0-1 Knapsack Problem
D = []
W = 50
profit = [60, 100, 120]
weight = [10, 20, 30]
n = len(profit)





# Driver Code
if __name__ == '__main__':
    # Initialize the memoization table with None
    D = [[None for _ in range(W + 1)] for _ in range(n + 1)]
    print(memknapSack(n,W))

# This code is contributed by Nikhil Kumar Singh