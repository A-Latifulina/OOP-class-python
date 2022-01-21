def calc_average():
    test_scores = []
    print('Enter test scores: ')
    for i in range(0, 5):
        score = int(input())
        test_scores.append(score)
    average = sum(test_scores)/5
    return average

def determine_letter_grade(average):
    if average >= 90:
        print('The average letter grade is A')
    elif average >= 80:
        print('The average letter grade is B')
    elif average >= 70:
        print('The average letter grade is C')
    elif average >= 60:
        print('The average letter grade is D')
    else:
        print('The average letter grade is F')

#main
for i in range(0, 3):
    name = input('Enter name ')
    determine_letter_grade(calc_average())
