#string formats pt 2
cookie_amount = int(input('Enter the amount of cookies you want to bake '))

sugar_cup = cookie_amount * 1.5/48
butter_cup = cookie_amount * 1/48
flour_cup = cookie_amount * 2.75/48

print('This will require:')
print("{:.2f}".format(sugar_cup), 'cup(s) of sugar.')
print("{:.2f}".format(butter_cup), 'cup(s) of butter.')
print("{:.2f}".format(flour_cup), 'cup(s) of flour.')
