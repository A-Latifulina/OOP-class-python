#multiplying integers
first = int (input('What is your first integer '))
second = int (input('What is your second integer '))
print ('State the product of ' , first , ' and ' , second)
product = int (input ())
print('you said the product is ' , product)
if  product== first * second:
    print('you are correct')
else:
    print('you are incorrect')
    print ( 'the product is ', first * second)
