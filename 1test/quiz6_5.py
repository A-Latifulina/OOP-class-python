def print_total_feet(feet, inches): #(1)
    total_feet = (feet, inches)  #(2)
    print('The total number of feet is ', total_feet)

#main part of program
feet = float(input( "Enter the number of feet "))
inches = float(input('Enter the number of inches ')) #(3)
print_total_feet(feet, inches)  # calls the function
