#The function accepts the list of integers and returns the average.  You may
#not use short cuts such as using the sum( ) function.

def get_average(mylist):
    sum = 0
    for i in range (len(mylist)):
        sum = sum + mylist[i]

    average = sum / (len(mylist))
    return average

#main part of the program
mylist=[2,7,4,5,89,43,65,78,35,54,97] s
average=get_average(mylist)
print('The average is ', average)  
