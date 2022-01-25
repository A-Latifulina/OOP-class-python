birthdays= { }

def search():
    name = input('Enter a name ')
    print(birthdays.get(name, 'not found'))

def add():
    name = input('Enter a name ')
    bday = input ('Enter a birthday ')
    if name not in birthdays:
        birthdays[name] = bday
    else:
        print ('That entry already exists')

def update():
    name = input('Enter a name ')
    if name in birthdays:
        bday = input ('Enter the new birthday ')
        birthdays[name] = bday
    else:
        print('That name is not found')

def delete():
    name= input('Enter a name ')
    if name in birthdays:
        del birthdays[name]
    else :
        print('That name is not found')

#main
print('The menu of choices for the birthday book is')
print('1 for searching a name')
print('2 for adding a new name and birthday')
print('3 for changing a birthday of an existing name')
print('4 for deleting a name and birthday')
print('5 to print the book')

choice = 0
while choice != 10:
    choice = int ( input('Enter choice'))
    if choice == 1:
        search()
    elif choice == 2:
        add()
    elif choice == 3:
        update()
    elif choice == 4:
        delete()
    elif choice == 5:
        print (birthdays)             
