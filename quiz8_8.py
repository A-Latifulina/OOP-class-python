#Assume a file containing a series of integers is named numbers.txt  and
#exists in your working folder.

#This  program calls two functions , one to read in the numbers from the
#data file into a  list ( one number on a line ) and one function to
#print out the list.  I am writing the main part of the program.  You are
#responsible for writing the code for  two functions. Notice which
#function needs a return statement.

def read_list():
    numberfile = open('numbers.txt')
    contents = numberfile.read()
    return contents
def print_list():
    print(contents)

#main part of the program
my_list = read_list()
my_list.print_list()






