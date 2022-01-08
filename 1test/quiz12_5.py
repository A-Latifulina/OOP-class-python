class Date:
     def __init__(self,month,day):
         self.day=day
         self.month=month #(1)
          
     def days_in_month(self):
         if self.month in (4,6,9, 11):
             return 30
         elif self.month in (2): #(2)
             return 28
         else:
             return 31
     def advance (self): # not concerned if it wraps to the next year
          self.day = self.day+ 1
          if self.day> self.days_in_month( ):
               self.month = self.month+ 1
               self.day = 1
              
     def set_day (self, day):
         self.day=day

     def set_month(self,month):
         self.month= month

     def get_month(self):
         return month #(3)

     def print_date( self):
          print (self.month, '/', self.day)

#main part of program
d1 = Date ( 9,19)
d2 = Date (12, 24)

print ('days in September:', d1.days_in_month() )
print ('Days in December:', d2.days_in_month( ) )
print (' d1 is ')
d1.print_date()  # print the date before advancing
d1.advance() #(4)  # we want to call a method
print (' d1 is advanced a day ')  #print he date after the advancing
d1.print_date()
birthday = Date(0,0)
birthday.set_month(2)
birthday.set_day ( 25)
print('My birthday is')
print(birthday)#(5)   # print the birthday 
