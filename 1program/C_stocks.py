acme_shares = int(input('Enter the amount of Acme shares bought '))
initial_investment = acme_shares * 40
stockbroker_commission_buy = initial_investment * .03

stocks_sold = int(input('Enter the amount of Acme shares sold '))
sale_returns = stocks_sold * 42.75
stockbroker_commission_sell = sale_returns * .03

stockbroker_combined_commissions = stockbroker_commission_sell + stockbroker_commission_buy

print('The amount of money paid for the stock is $', initial_investment)
print('The amount of commission paid to stockbroker for stock purchase was $', "{:.2f}".format(stockbroker_commission_buy))
print('The amount of money made from sale is $', sale_returns)
print('The amount of commission paid to stockbroker for stock sale was $', "{:.2f}".format(stockbroker_commission_sell))
print("The sum of stockbroker's commission for buying and selling is $", "{:.2f}".format(stockbroker_combined_commissions))
print('Amount of funds available after selling stock and after paying stockbroker commission for buying and selling stock is $', "{:.2f}".format(sale_returns - stockbroker_combined_commissions))

