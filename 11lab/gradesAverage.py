student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
    }


average_list = [ ] 
name_list = list(student_grades.keys())  # We are saving the names for the dictionary in a separate list
print(name_list)
# the following creates an average for each student and places the average for each student in an average_list ( a parallel list to names) 
for i in range (5) :
    print (name_list[i], '   ', student_grades[name_list[i]] )
    average = sum(student_grades[name_list[i]])/len(student_grades[name_list[i]] )
    average_list.append(average)
    
print( 'The two parallel lists, name and average') 
for i in range(len(name_list)):
    print (name_list[i], '   ', average_list[i] )
                                                                         
# this figures out the  average for best student  , name and average 

maximum = max(average_list)
print ('The maximum average is ', maximum )
#But we need to go back and figure out which student has that average.  
for i in range (5):
    if average_list[i] == maximum:
        print ( name_list[i] , 'has the highest average of    ', average_list[i] ) 
    
print ('Figuring out the average for each test grade over all the students')     
# to figure out the average for each assignment you need to have the two-dimensional idea
average_assignment_grade = [ ]
grades= [ [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]
          ]


for row in range (5):
    
        grades[row] = student_grades[name_list[row]  ] 
        #print ('row is ', row)
        #print (grades[row])

print (grades) 

for column in range (5):
    sum = 0
    print('Grades for assignment ', column) 
    for row in range(5):
              
        print (grades [row] [column])
         
        sum = sum  +  grades[row] [column]      
    print( )
    average_assignment_grade.append (sum/5)

print ( 'The average assignment grades are ' )
for i in range (5):
    print( 'for assignment', i, 'the average is',  average_assignment_grade [i] ) 

