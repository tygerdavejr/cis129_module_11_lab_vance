# cis129_module_11_lab_vance
Module 11 Lab

This is a weird lab in that it asks for two scripts to run in iPython and then what looks like full-fledged software.

Exercise 9.1:
with open('grades.txt', mode='w') as grades:
    student_number = input('\nEnter Student Number [Q to quit]: ')
    while student_number != 'Q':
        student_name = input('Enter Student Name: ')
        student_grade = input('Enter Grade: ')
        student_record = student_number + ' ' + student_name + ' ' + student_grade + '\n'
        grades.write(student_record)
        student_number = input('\nEnter Student Number [Q to quit]: ')


Exercise 9.2: 
with open('grades.txt', mode='r') as grades:
    print(f'{'Student No.':<15}{'Student Name':<15}{'Grade':>10}')
    count = 0
    total_score = 0.00
    for student in grades:
        count += 1
        student_number, student_name, grade = student.split()
        print(f'{student_number:<15}{student_name:<15}{grade:>10}')
        grade_score = float(grade)
        total_score += grade_score
    avg_score = total_score / count
    print(f'{'Total of Grades':<15}{'No. of Students':<15}{'Avg Grade':>10}')
    print(f'{total_score:<15.2f}{count:<15}{avg_score:>10.2f}')
    
