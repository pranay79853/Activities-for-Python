# Profit loss

actual_cost = int(input(" Please Enter the Actual Product Price: "))

sale_amount = int(input(" Please Enter the Sales Amount: "))

if(sale_amount > actual_cost) :
    profit = sale_amount - actual_cost
    print("You have generated a profit of", profit)

elif(sale_amount < actual_cost) :
    loss = actual_cost - sale_amount
    print("You have a loss of", loss)

else :
    print("You have nor profit nor loss")
    