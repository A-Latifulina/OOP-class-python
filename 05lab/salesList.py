num_days = int(input('Enter number of days '))

sales= [0] * num_days
print(sales)

i = 0
while  i < num_days:
    print ('Day #', i + 1, ':' )
    sales[i] = float(input('Enter sales: '))
    i = i + 1

print(sales)

list_num = int(input('Enter which list position to upgrade '))
new_value = float(input('Enter what value to upgrade '))
sales[list_num] = new_value

print(sales)

print('The sum is', sum(sales))

print('The average is', (sum(sales)/len(sales)))

print('The reversed list of sales is', list(reversed(sales)))
