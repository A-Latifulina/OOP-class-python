def  count_times ( list  ) :

    count=0;
    for i in range (len(list )) :
        if list[i] == name :
            count = count + 1

    return count

#main part of the program

name = input('Enter name of teacher')
list = ['Dr.Hill', 'Dr.Courtney', 'Dr.Mosley', 'Dr.Scharff','Dr.Hill']
number = count_times(list)
print(number)
