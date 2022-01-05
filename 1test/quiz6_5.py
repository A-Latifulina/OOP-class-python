#Fill in the blank lines for this problem that reads in the number of
#feet and number of inches for the length of a house and calls a function
#that prints out the total number of feet.  It could be  a decimal for
#the number of feet.

def print_total_feet(feet, inches): #(1)

    total_feet = (feet, inches)  #(2)

    print('The total number of feet is ', total_feet)

#main part of program

feet = float(input( "Enter the number of feet "))

inches = float(input('Enter the number of inches ')) #(3)

print_total_feet(feet, inches)  # calls the function
