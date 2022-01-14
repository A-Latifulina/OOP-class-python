#working with strings
#This program counts the number of times
#the letter T  or t   appears in a string


my_string = input('Enter a sentence ')

count = 0

for ch in my_string:
      if ch == 'T' or ch == 't':
            count += 1

print ('The letter T or t  appears', count)
       
