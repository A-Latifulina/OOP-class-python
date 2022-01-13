annual_rainfall = {}

i = 1
for i in range(2):
    month = int(input('Enter month number '))
    rainfall = int(input('Enter monthly rainfall '))
    annual_rainfall[month] = rainfall
    i += 1

print(annual_rainfall)
