# MODULE 11 LAB: STUDENT GRADES FILE WRITER
#
# David Vance
# Professor Kevin Chang
# CIS129 - Programming and Problemsolving I
# 18 October 2024
"""This module allows an instructor to enter the grades of a student and 
write that file in CSV format.  The required record structure is
firstname, lastname, examgrade1, examgrade2, examgrade3
where firstname and lastname are string text, and the three examgrades
are integers."""

# Additional notes:  
# - Include a SENTINEL loop so that the instructor can continue to enter
# student grades.
# - Include Exceptions handling to catch errors in first, last name entry:
#   Is the entry the SENTINEL?
# - Include Exceptions handling to catch errors in exam score entry:
#   Was the value not an integer?
#   Was the value the SENTINEL?
#   Was the value a negative entry?
# - The program doesn't include an output requirement, but include a 
#   file reader.

# INITIATIONS
# Import modules, build Classes, define CONSTANTS, variables and dictionaries,
# and build defined functions.

import csv  # Import CSV for writing and reading CSV files

SENTINEL = '-99'  # Provide the user with a method to escape processing


# Display Opening Instructions
def display_instructions():
    """This module displays basic instructions for the program."""

    print('\nINSTRUCTIONS')
    print('\n  Use this module to enter three exam scores for your students.')
    print('  First and Last name are limited to 25 characters.')
    print('  The exams are positive integer values only.')
    print('\nENTER -99 AT ANY TIME TO END INPUT\n')

    return

def input_information():
    return

def write_file(student_record):
    return


# While not part of the assignment, I felt it best to include a simple report.
def display_final_report():
    """This module is not required for the exercise but is included to make
    grading easier by opening the file created above and printing a simple
    report from it."""
    try:
        with open('student_grades.csv', mode='r', newline='') as students:
            reader = csv.reader(students)
            print(f'{'\nFIRST NAME':<25}{'LAST NAME':<25}{'EXAM 1':^10}{'EXAM 2':^10}{'EXAM 3':^10}')
            for record in reader:
                firstname, lastname, examgrade1, examgrade2, examgrade3 = record
                print(f'{firstname:<25}{lastname:25}{examgrade1:^10}{examgrade2:^10}{examgrade3:^10}')
    except FileNotFoundError:
        print('\n YOUR READ FILE DOES NOT EXIST')
    return


def get_name(which_name):
    """Prompt user for appropriate name."""
    name = input(f'{"Enter student's "}{which_name}{" name [-99 to quit]: "}')
    return (name)


def get_grade(which_exam):
    try:
        exam_score = int(input(f'{"Enter student's "}{which_exam}{" exam score: "}'))
    except ValueError:
        print('Your entry must be an integer.  Please try again.')
    else:
        return(exam_score)


# MAIN MODULE
# This module calls all other modules
def main():
    """This module calls all the sub-functions."""
    
    # Display opening instructions
    display_instructions()
    
    # Open file with CVS mode for writing
    with open('student_grades.csv', mode='w', newline='') as students:
        writer = csv.writer(students)

        firstname = get_name('first')

        while firstname != SENTINEL:
            lastname = get_name('last')
            examgrade1 = get_grade('first')
            examgrade2 = get_grade('second')
            examgrade3 = get_grade('third')

 #       student_record = [firstname, lastname, examgrade1, examgrade2, examgrade3]
            writer.writerow([firstname, lastname, examgrade1, examgrade2, examgrade3])

            firstname = get_name('first')  
    
    
    # Display final report
    display_final_report()
    return


# MAIN PROCESSING
# Initiate the main() module

if __name__ == '__main__':
    main()
