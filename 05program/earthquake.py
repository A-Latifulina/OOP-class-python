earthquake_file = open('earthquake_log.txt')

magnitude = []
location = []

for line in earthquake_file:
    values = line.split()
    magnitude.append(values[0])
    location.append(values[6])

print('The magnitude list is ', magnitude)\n
print('The location list is ', location)

def average_magnitude():
    sum = 0
    for i in range (len(magnitude)):
        sum = sum + float(magnitude[i])
        average = sum / len(magnitude)
    print('The average magnitude is', average)

#main
average_magnitude()

print ('The max magnitude was', max(magnitude))
print ('The list of sorted locations is ', sorted(location))
