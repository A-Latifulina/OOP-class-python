disney_world_fee_total = 0
jersey_shore_fee_total = 0   #1
for i in range (10):
    name =input('What is the family name ')
    number = int (input ('How many in your family '))
    vacation_choice = input('type Jersey or Disney ' )
    if vacation_choice == 'Jersey':
        fee = 700 * number #2
        jersey_shore_fee_total = jersey_shore_fee_total + fee
    elif vacation_choice == 'Disney':   #3
        fee = 1500 * number
        disney_world_fee_total = disney_world_fee_total + fee  #4
    else :
        print ( 'Not an available choice')

    print ('family name is ', name)
    print (' Your fee is ', fee)
    print ('Your choice is ', vacation_choice )

print('The total fees for Jersey shore is', jersey_shore_fee_total)  #5
print ('The total fees for Disney world is ', disney_world_fee_total)
