count_one = 0
count_two = 0
count_three = 0
count_four = 0

fee_one = 0
fee_two = 0
fee_three = 0
fee_four = 0

for i in range (10):
    name = str(input('What is your last name '))
    pinNumber = int(input('What is your four digit pin number '))
    print('There are four choices for code: \n under_grad_commuter \n under_grad_resident \n grad_commuter \n grad_resident')
    code = str(input('Enter one of the four choices for code '))
    hours = float(input('Enter credit hours studied '))
    
    if code == 'under_grad_commuter':
        fee = 500 * hours
        fee_one += fee
        count_one += 1
        
    elif code == 'under_grad_resident':
        fee = 550 * hours
        fee_two += fee
        count_two += 1
