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
