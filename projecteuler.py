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
    """ Problem 1
    """
    
    logger.info('test inside function')
    logger.debug('does it work?')
    
    print("Problem 1")
    return

# ******************************************************************************
# Main
# ******************************************************************************

def main():
    
    # Problem Functions --------------------------------------------------------
    logger.info('Program Started')
    
    # Function for each problem calls
    problem1()

    logger.info('Program Completed')
    logger.info('--------------------------------------\n')
    
    return

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    main()


