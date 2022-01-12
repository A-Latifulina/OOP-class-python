#the most common words
import string
fname='romeo-full.txt'
try:  
    fhand=open(fname)
except:
    print('File cannot be opened:' ,fname )
    exit()	 

#print(fname)

counts = dict()
for line in fhand:
    line=line.rstrip( )
    line=line.translate(string.punctuation)#  removes any extra string punctuation
    line=line.lower()
    words=line.split()
    
    for word in words:
        
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] = counts.get(word, 0) + 1

#print the dictionary that was created
print(counts)            

# the following code creates a list and stores in the list the tuples from the above dictionary
lst = list()
for key,val in counts.items():
    lst.append((val,key))

#call the method that will sort the lst, where reverse is True	
lst.sort(reverse = True)

# print the 20 most common words in the lst

for key, val in lst[0:20]:
    print (val,key) 
