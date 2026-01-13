# A naive recursive implementation
# of 0-1 Knapsack Problem
D = []
W = 50
profit = [60, 100, 120]
weight = [10, 20, 30]
n = len(profit)


def memknapSack(i,j):

    # Base Case
    if i == 0 or j == 0:
        return 0
    
    if(D[i][j] is not None): 
        return D[i][j]

    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (weight[i - 1] > j):
        D[i][j] = memknapSack(i-1,j)
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        D[i][j] = max(memknapSack(i-1, j), memknapSack(i - 1, j - weight[i - 1]) + profit[i - 1])
        
    return D[i][j]


# Driver Code
if __name__ == '__main__':
    # Initialize the memoization table with None
    D = [[None for _ in range(W + 1)] for _ in range(n + 1)]
    print(memknapSack(n,W))

# This code is contributed by Nikhil Kumar Singh