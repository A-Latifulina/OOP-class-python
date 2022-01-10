##sales_list.py  We are gathering dales data for  5 days
num_days = int(input('Enter number of days ')) #Task 11

sales= [0] * num_days #Task 11
print(sales)

i = 0
while  i < num_days:
    print ('Day #', i + 1, ':' )
    sales[i] = float(input('Enter sales: '))
    i = i + 1

print(sales)

list_num = int(input('Enter which list position to upgrade ')) #Task 12
new_value = float(input('Enter what value to upgrade ')) #Task 12
sales[list_num] = new_value #Task 12

print(sales) #Task 12

print('The sum is', sum(sales)) #Task 13

print('The average is', (sum(sales)/len(sales))) #Task 13

print('The reversed list of sales is', list(reversed(sales))) #Task 14
