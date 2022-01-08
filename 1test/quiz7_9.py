#Write a program with one function and a main part that calls
#this function.  The function accepts two arguments: a list, and an
#integer x.  Assume that the list contains integers. You must write the
#code for the function. The function should display all of the numbers in
#the list that are less than x.

#The main part of the program should assign the list of  8 integers(you
#can specify and be specific)  and ask the user for the value of  x  .
#Then the main part of the program should call the above function. You
#must write the code for the main part of the program.

def function(list, intx):
    newlist = 0
    for i in range (len(list)):
        if list[i] < intx:
            newlist = newlist + newlist[i]
    return newlist

#main
list = [0, 1, 2, 3, 4, 5, 6, 7]
intx = input('Enter integer x: ')
function(list, intx)
print('The integers in the list smaller than your input are:', newlist)
