#! /usr/bin/env python
""" 
Project Euler - An interactive project with the purposes of learning:
    - Python
    - Following software requirements
    - Following coding guidelines
    - Using important standard Python libraries
    - Producing inline documentation
    - Introduction to Git and Github
    - Collaborative development with Git
"""
# ******************************************************************************
# Imports
# ******************************************************************************

import logging

# ******************************************************************************
# Globals
# ******************************************************************************

# Logging Configuration
global logger
logger = logging.getLogger('projecteuler')
logger.setLevel(logging.DEBUG)

# create file handler & console handler setting them to appropiate levels
file_h = logging.FileHandler('projecteuler.log')
file_h.setLevel(logging.DEBUG)

console_h = logging.StreamHandler()
console_h.setLevel(logging.INFO)

# create formatters for each handler
con_format = logging.Formatter(
    '[ %(funcName)s:%(lineno)d ] %(levelname)s  %(message)s'
    )
log_format = logging.Formatter(
    '%(asctime)s [ %(funcName)s:%(lineno)d ] %(levelname)s  %(message)s'
    )

# set formatters to appropriate
file_h.setFormatter(log_format)
console_h.setFormatter(con_format)

# add handlers to logger
logger.addHandler(file_h)
logger.addHandler(console_h)
    

# ******************************************************************************
# Functions
# ******************************************************************************

def problem1():
    """ 
    Problem 1: Find all natural numbers below 1000 which are 
        multiples of 3 and 5
    """
     # Variable Declaration
    max_val = 1000
    multiple1 = 3
    multiple2 = 5
    num_list = []
    total = 0
    logger.debug('variables declared for problem 1')
    
    # Loop through all values from 0 to but not including max_val and storing 
    # multiples
    for i in range(max_val):
        if i % multiple1 == 0:
            num_list.append(i)
        elif i % multiple2 == 0:
            num_list.append(i)
    logger.debug('list of values have been stored')
    
    # Summation of values in num_list
    for value in num_list:
        total = total + value
    logger.debug('summation complete')
    
    logger.info("Problem 1 Solution: ")
    logger.info("The sum of terms under %d which are multiples of %d and %d is %d \n" 
          % (max_val, multiple1, multiple2, total))
    
    return

# ******************************************************************************
# Main
# ******************************************************************************

def main():
    """
    Main will run all problem functions and sequentially returning each problem
    solution to stdout as well as 'projecteuler.log'
    """
    
    logger.info('Program Started')

    # Problem Functions --------------------------------------------------------
    problem1()

    
    logger.info('Program Completed')
    logger.info('--------------------------------------\n')
    
    return

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    main()


