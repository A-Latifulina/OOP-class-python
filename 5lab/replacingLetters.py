# working with strings
#This program attempts to replace every T with a '_'

count = 0
my_string = input ('Enter a sentence ')
print('The original sentence is ', my_string) 

your_string = '' #(1)

i = 0
for i in range (len(my_string)):
      ch = my_string[i]

      if ch =='T' or ch =='t':
            ch = '_'#(2)
            i = i + 1
          
      your_string = your_string + ch #(3)
      print(your_string) #Task 9
    

print('The sentence with "T" or "t" replaced with "_" is', your_string)
       
