cost_price = int(input("Enter the cost price:"))
selling_price = int(input("Enter the selling price:"))

# if sp is more than cp --> profit
if selling_price > cost_price:
    profit = selling_price - cost_price
    print("We have made profit of:", profit)

# if sp is less than cp --> loss
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("We have incurred loss of:", loss)

# if sp is equal to cp --> no profit no loss
else:
    print("We have made no profit and no loss")