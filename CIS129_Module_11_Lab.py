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
# student grades until finished.
# - Include Exceptions handling to catch if the exam score is not an integer.
# - Was the exam score the SENTINEL?
#   Was the exam score less than 0 or greater than 100?

# The lab did not call for a report, but I decided to include one anyways.

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
    print('  First and Last name will be limited to 24 characters each.')
    print('  The exams are positive integer values from 0 to 100 only.')
    print('\nENTER -99 AT ANY TIME TO END INPUT\n')

    return


# While not part of the assignment, I felt it best to include a simple report.
def display_final_report():
    """This module is not required for the exercise but is included to make
    grading easier by opening the file created above and printing a simple
    report from it."""
    try:
        with open('student_grades.csv', mode='r', newline='') as students:
            reader = csv.reader(students)
            print(f'{'\nFIRST NAME':<25}{' LAST NAME':<25}{'EXAM 1':^10}{'EXAM 2':^10}{'EXAM 3':^10}')
            for record in reader:
                firstname, lastname, examgrade1, examgrade2, examgrade3 = record
                print(f'{firstname:<25}{lastname:25}{examgrade1:^10}{examgrade2:^10}{examgrade3:^10}')
    except FileNotFoundError:
        print('\n YOUR READ FILE DOES NOT EXIST')

    return


def get_name(which_name):
    """Prompt user for appropriate name."""
    name = input(f'{"Enter student's "}{which_name}{" name [-99 to quit]: "}')
    name = name[:23]  # Names are limited to a max of 25 characters (remember 0)
    return (name)


def receive_grade(which_exam):
    """This is the first step in validating the input grade:
    Did the user enter an integer value?"""
    try:
        exam_score = int(input(f'{"Enter student's "}{which_exam}{" exam score [-99 to exit]: "}'))
    except ValueError:
        print('Your entry must be an integer.  Please try again.')
    else:
        return exam_score



def get_exam_score(which_exam):
    """This module calls for the initial input of the grade, and then
    does the second round of validation:  Is the score either the 
    SENTINEL, less than zero or greater than 100?"""

    # Ask for a grade input.  which_exam includes the text
    # to create the correct input prompt.
    exam_score = receive_grade(which_exam)

    # Stay in the loop if the exam score is less than 0 or greater than 100.
    while exam_score < 0 or exam_score > 100:
        if exam_score == int(SENTINEL):  # If exam_score is less than zero, is it the SENTINEL?
            print('\nThank you for entering scores.')  # If the entry is the SENTINEL, print a thank you message
            raise SystemExit  # And exit the program.
        
        print('\n*** The score you enter should be from 0 to 100 ***\n')  # Print an error message
        exam_score = receive_grade(which_exam)  # And prompt the user for another entry
    
    return(exam_score)  # If everything is good, return the exam_score


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
            if lastname == SENTINEL:
                break

            examgrade1 = get_exam_score('first')
            examgrade2 = get_exam_score('second')
            examgrade3 = get_exam_score('third')

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
