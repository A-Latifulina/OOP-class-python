#Write a function called get_average that matches up with this code.  The
#function accepts the list of integers and returns the average.  You may
#NOT use short cuts such as using the sum( )  function.  You are only
#responsible for writing the code for the function.  I wrote the code for
#the main part of the program.


def get_average(mylist):
    sum = 0
    for i in range (len(mylist)):
        sum = sum + mylist[i]

    average = sum / (len(mylist))
    return average


#main part of the program

mylist=[2,7,4,5,89,43,65,78,35,54,97]    #  assume that there are more numbers

average=get_average(mylist)

print('The average is ', average)  
