#Enter a color to find the complimentary color
color = input('Enter a primary or secondary color to find out its complimentary color ')

if color == 'red':
    print('The complimentary color to', color, 'is green.')
elif color == 'blue':
    print('The complimentary color to', color, 'is orange.')
elif color == 'yellow':
    print('The complimentary color to', color, 'is purple.')
elif color == 'green':
    print('The complimentary color to', color, 'is red.')
elif color == 'purple':
    print('The complimentary color to', color, 'is yellow.')
elif color == 'orange':
    print('The complimentary color to', color, 'is blue.')
else:
    print('Error message: Make sure you entered either a primary or secondary color')
