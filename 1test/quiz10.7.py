def  search (  key,list ):
    i = 0  #(1)
    found = False
    while not found and i < len (list):
           
        if key == list[i]: #(2)
            found =   True
        else:
            i = i + 1   
    return found;
     
file_name ='names.txt'
fhand = open(file_name)
employee_list = []  #(3)
count = 0
for line in fhand:
    line=line.rstrip( )
    employee_list.append(line) #(4)                                                                                               #employee list
    count = count + 1
for i in range (count ):
    print (employee_list[i])   #(5)   // print the employee list one by one

name = input('For which name do you wish to search')
if (search ( name, employee_list) == True):
     
    print (name, 'is on the list of full time employees')
else:
    print ( name, ' is not on the list of full time employees' )  #(6)
