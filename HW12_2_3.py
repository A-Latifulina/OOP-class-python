def shampoo_instructions(num_cycles):
    if (num_cycles < 1):
        print('Too few.')
    elif (num_cycles > 4):
        print('Too many.')
    else:
        N = 1
        while (N <= num_cycles):
            print(N, ': Lather and rinse.')
            N += 1
        print('Done.')

user_cycles = int(input())
shampoo_instructions(user_cycles)
