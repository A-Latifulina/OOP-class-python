#Primary_Colors

primary_one = input('Enter a primary color ')
primary_two = input('Enter another primary color ')

if (primary_one == 'red' or primary_two == 'red') and (primary_one == 'blue' or primary_two == 'blue'):
    print('Your secondary color is purple.')
elif (primary_one == 'red' or primary_two == 'red') and (primary_one == 'yellow' or primary_two == 'yellow'):
    print('Your secondary color is orange.')
elif (primary_one == 'blue' or primary_two == 'blue') and (primary_one == 'yellow' or primary_two == 'yellow'):
    print('Your secondary color is green.')
else:
    print('Error message: Make sure you enter only either red, blue, and do not repeat the same color for both primary colors.')
