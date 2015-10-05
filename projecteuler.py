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
import math
import argparse

# ******************************************************************************
# Globals
# ******************************************************************************


# ******************************************************************************
# Functions
# ******************************************************************************

def get_arguments():
    """
    Get args from command line and return the important info to main
    """
    __args = ""    
    return __args


def problem1():
    """ 
    Problem 1: Find all natural numbers below 1000 which are 
        multiples of 3 and 5
    """
    return


# ******************************************************************************
# Main
# ******************************************************************************

def main():
    """
    Main will run all problem functions and sequentially returning each problem
    solution to stdout as well as 'projecteuler.log'
    """
    __args = get_arguments()
    
    # use logging to printout notification that program has started

    # Problem Functions --------------------------------------------------------
    problem1()
    
    # use logging to printout notification that program has terminated
    
    return

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    main()


