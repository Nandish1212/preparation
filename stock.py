def max_profit(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    return max_profit

prices = [10,180,260,320,40,535,695]
print(max_profit(prices))