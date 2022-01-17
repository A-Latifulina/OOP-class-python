start_time = int(input("What is the starting time of your phone call? "))
length_min = int(input("What is the length of your phone call in minutes? "))

regular_price = .4

if (start_time >= 1800) or (start_time <= 800):
    discounted_price = (regular_price * .5) * length_min
    print('The price after discounting starting time is $ %0.2f'%(discounted_price))
else:
    discounted_price = regular_price * length_min
    print('The regular price with no discount is $ %0.2f'%(discounted_price))

if length_min > 60:
    discounted_price = discounted_price * .85
    print('The discounted price for a call over 60 minutes is $ %0.2f'%(discounted_price))

tax = (discounted_price * .065)
final_price = (discounted_price + tax)

print('Your final price with tax is $ %0.2f'%(final_price))
