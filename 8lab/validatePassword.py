def valid_password(password):
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    is_valid = False 

    if len(password) >=7:
        correct_length = True
        for ch in password:  
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True
            if correct_length and has_uppercase and has_lowercase and has_digit:
                is_valid = True
            else:
                is_valid = False
    return is_valid

def test_password():
    password = input('Enter your password: ')
    print(password)
    bad_password = []
    while not valid_password(password):
        bad_password.append(password)
        print ('The password is not valid')
        password = input('Enter your password: ')
    print ('That is a valid password')
    print('The bad password list is', bad_password)

#main part of the program
test_password()
