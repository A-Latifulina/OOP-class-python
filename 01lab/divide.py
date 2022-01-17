#dividing integers
first = int (input('What is your first integer '))
second = int ( ('What is your second integer '))

quotient = int (input ('State the quotient of ' + str(first) + ' divided by ' + str( second)  ))
print(you said the quotient  is  , quotient)
if  quotient == first / second:
    print('you are correct')
else:
    print('you are incorrect')
    print ( 'the quotient is ', first / second)
