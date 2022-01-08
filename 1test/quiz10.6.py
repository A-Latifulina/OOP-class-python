def find_largest (list):
    current_max = 0
    for i in list:
        if i > current_max:
            current_max = i
    return current_max

#main
greatest = find_largest(number_list)
print(greatest)
