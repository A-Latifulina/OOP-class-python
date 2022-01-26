def search (key,list):
    found = False;
    i = 0;
    while (found== False and i <len(list)):
        if key == list[i]: #(1) 
            found = True
        else:
            i += 1 #(2)
    return i

def swap (first_list, second_list, first, second):

    temp = first_list[first]
    first_list[first] = first_list[second]
    first_list[second] = temp

    temp = second_list[first]    
    second_list[first] = second_list[second]
    second_list[second] = temp                                      

def sort(first_list, second_list):
    for i in range(len(first_list)-1):
        minSubscript = i  #(3)
        for j in range (i+1, len(first_list) ):
            if first_list[j] < first_list[minSubscript]:
                minSubscript = j #(4)
                
        swap(first_list,second_list,i,minSubscript )
                
inventory_file = open('inventory.txt')
book_list = []
quantity_list = [] 
for line in inventory_file:
       values = line.split() #(5)
       book_list.append(values[0])
       quantity_list.append(values[1]) #(6)

print('the original list')
for i in range(len(book_list)):
    print(book_list[i]+ '   ' ,   quantity_list[i] )#(7)

print()
sort(book_list, quantity_list) #(8)
print('after the sort' ) 

for i in range(len(book_list)):
    print(book_list[i]+ '   ' ,  ( quantity_list[i]) )
    
print ( )
print('For the search') 
subscript = search ('Python', book_list)
print ( "Python has ", quantity_list[subscript], ' books' )

title = input('Enter a book title to search ') 
subscript = search (title, book_list)
print (title, 'has ', quantity_list[subscript], ' books' )
    
