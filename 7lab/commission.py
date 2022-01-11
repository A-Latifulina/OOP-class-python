def get_sales():
    monthly_sales = float(input('Enter the monthly sales: '))
    return monthly_sales

def advanced_pay():
    advanced_pay = float(input('Advanced pay:'))
    while (advanced_pay >2000):
         print('Enter the amount of advanced pay,(less than $2000) or')
         print ('enter 0 if no advanced pay was give.')
    return advanced_pay

def determine_comm_rate():
    if monthly_sales < 10000:
        rate = 0.10
    elif monthly_sales>=10000 and monthly_sales <=14999.99:
        rate = 0.12
    elif monthly_sales >=15000 and monthly_sales <= 17999.99:
        rate =0.14
    elif monthly_sales >=18000 and monthly_sales <=21999.99:
        rate = 0.16
    else:
        rate = .18
    return rate

#main
name = input('Enter your name ')

i = 0
for i in range(3):
    get_sales()

advanced_pay()

determine_comm_rate()

pay = monthly_sales * rate - advanced_pay

print ('The pay is $ %.2f' % pay)

if pay <0:
    print('You must pay your employer', pay ) 
