birthdays= { }
choice = 0
print('Your choices are 1 for searching a name, 2 for adding a new name and birthday')
print('3  for changing a birthday of an existing name', '4 for deleting a name and birthday')
print ('5 for printing out the dictionary')

while choice != 10:
    user_val = int(input('Enter choice # '))
    if choice == 1:
        name = input('Enter a name: ')
        print(birthdays.get(name, 'not found'))
    elif choice == 2:
        name = input('Enter a name: ')
        bday = input ('Enter a birthday: ')
        if name not in birthdays:
            birthdays[name] = bday
        else:
            print('That entry already exists')
    elif choice == 3:
        name = input('Enter a name: ')
        if name in birthdays:
            bday = input ('Enter the new birthday: ')
            birthdays[name] = bday
        else:
            print('That name is not found')
    elif choice == 4:
         name= input('Enter a name: ')
         if name in birthdays:
             del birthdays[name]
         else :
             print('That name is not found.')
    
    elif choice == 5:
          print(birthdays)       
