#Part A, B, & extra credit

baseball_data = open('baseball_finals.txt')

series_year = {}
team_name = {}

for line in baseball_data:
    value = line.split()
    series_year[value[0]] = [value[1], value[2], value[3], value[4], value[5]]
    if value[2] in team_name:
        team_name[value[2]] += 1
    else:
        team_name[value[2]] = 1
    
year = input('Enter a year between 1905 and 2018 ')
print('The city of the winning team is', series_year[year][0])
print('The name of the losing team is', series_year[year][3])
print('The city of the losing team', series_year[year][2])
print('The score was', series_year[year][4])
