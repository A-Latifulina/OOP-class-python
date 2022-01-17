#string formats
food_charge = int(input('Enter charge for the food '))
food_tip = food_charge * .18
food_sales_tax = food_charge * .07
food_total = food_charge + food_tip + food_sales_tax

print('The entered food charge is', food_charge)
print('The tip (18%) is', "{:.2f}".format(food_tip))
print('The sales tax (7%) is', "{:.2f}".format(food_sales_tax))
print('The total is', food_total)
