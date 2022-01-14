def get_login_name (first, last, idnumber):
   set1 = first[0:3]
   set2 = last[0:3]
   set3 = idnumber[-3:]

   login_name = set1 + set2 + set3
   return login_name

def getInfo():
   first = input('Enter your first name ')
   last = input('enter your last name ')
   idnumber = input ('Enter your student ID number ')
   print ('Your system log in name is ')
   print (get_login_name(first, last, idnumber))

# main
getInfo()
