count = 0
my_string = input ('Enter a sentence ')
print('The original sentence is ', my_string) 

your_string = ''

i = 0
for i in range (len(my_string)):
      ch = my_string[i]

      if ch =='T' or ch =='t':
            ch = '_'
            i = i + 1
          
      your_string = your_string + ch
      print(your_string)
    
print('The sentence with "T" or "t" replaced with "_" is', your_string)
