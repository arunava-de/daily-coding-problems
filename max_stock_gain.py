def max_gain(stocks):
    min_price = 10**6
    profit = 0
    max_profit = -10**6

    if stocks==[]:
        print("Empty stocks list")
        return
    elif len(stocks)==1:
        print("Not enough stocks to buy and sell")
        return

    for i in range(len(stocks)):
        if stocks[i]<min_price:
            min_price = stocks[i]

        profit = stocks[i] - min_price

        if profit>max_profit:
            max_profit = profit

    return max_profit
    
print(max_gain( [9, 11, 8, 5, 7, 10]))