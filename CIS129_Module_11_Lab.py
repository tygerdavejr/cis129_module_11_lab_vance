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
#   Is the length of either name greater than 25?
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

SENTINEL = -99  # Provide the user with a method to escape processing

def main():
    """This module calls all the sub-functions."""
    
    # Display opening instructions
    display_instructions()
    
    return


# Display Opening Instructions
def display_instructions():
    """This module displays basic instructions for the program."""

    print('\nINSTRUCTIONS')
    print('\n  Use this module to enter three exam scores for your students.')
    print('  First and Last name are limited to 25 characters.')
    print('  The exams are positive integer values only.')
    print('\nENTER -99 AT ANY TIME TO END INPUT\n')

    return





# MAIN PROCESSING
# Initiate the main() module

if __name__ == '__main__':
    main()



# TERMINATE PROCESSING
# Display final report

