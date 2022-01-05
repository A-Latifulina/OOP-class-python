# finding commission 

monthly_sales = int(input('Enter the amount of your monthly sales: ')) # 1

print('Enter the amount of advanced pay,(less than $2000) or')
print ('Enter 0 if no advanced pay was give.')
advanced_pay = int(input('Enter amount here:'))  #2
while (advanced_pay > 2000):
     print('Enter the amount of advanced pay,(less than $2000) or')
     print ('Enter 0 if no advanced pay was give.')
     advanced_pay = float(input('Advanced pay:'))

if monthly_sales < 10000:
       rate = 0.06
elif monthly_sales >= 10000 and monthly_sales <= 14999.99:
        rate = 0.08
elif month_sales >= 15000 and monthly_sales <= 17999:  #3
        rate = 0.10
elif monthly_sales >=18000 and monthly_sales <=21999.99:
        rate = .12   #4
else:
        rate = .14   
  
pay = monthly_sales * rate - advanced_pay

print ('The pay is $ %.2f' % pay)

if pay <0:
    print('You must reimburse Hal the negative amount')   #5
