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
    global logger
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", help="Enables Verbose Logging")
    __args = parser.parse_args()
    if __args.verbose:
        print("Setting Log Level to DEBUG")
        logger = logging.getLogger('projecteuler')
        logger.setLevel(logging.DEBUG)
        # create file handler & console handler setting them to appropiate levels
        file_h = logging.FileHandler('projecteuler.log', mode='w')
        file_h.setLevel(logging.DEBUG)

        console_h = logging.StreamHandler()
        console_h.setLevel(logging.DEBUG)

    else:
        print("Setting Log Level to INFO")
        logger = logging.getLogger('projecteuler')
        logger.setLevel(logging.DEBUG)
        # create file handler & console handler setting them to appropiate levels
        file_h = logging.FileHandler('projecteuler.log', mode='w')
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
    
    return __args


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

def problem2():
    """ 
    Problem 2: Find the sum of the even-valued terms in the Fibonacci
        sequence whose values do not exceed four million
    """
    #Variable Declaration
    max_val = 4000000
    total = 2   # set to 2 to account for the first even term of sequence
    num1 = 1    # first term of sequence
    num2 = 2    # second term of sequence
    temp = 0
    
    # Loop until the stored value is greater than the specified max_val
    while num2 < max_val:
        temp = num1 + num2
        # check to see if the following value is even
        if temp % 2 == 0:
            total = temp + total
        num1 = num2
        num2 = temp
    
    logger.info("Problem 2 Solution: ")
    logger.info("The sum of even-valued terms in Fibonacci sequence is %d\n" % total)
    
    return

def problem5():
    """
    Problem 5: Find the smallest number divisible by all values from 1 to 20
    """
    # all values < 10 are inclusive multiples in values 11 to 20
    values = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    smallestPrimeNum = 0
    
    # find smallest prime number of the list
    for number in values:
        n = 2
        temp = int(math.ceil(math.sqrt(11)))
        __isprime = True
        while n <= temp:
            if number % n == 0:
                #not prime
                __isprime = False
            n += 1
        if __isprime:
            smallestPrimeNum = number
            break
    
    # increment smallest prime number until number is divisble by all values
    __doneFlag = False
    myNum = 0
    while not __doneFlag:
        myNum += smallestPrimeNum
        __doneFlag = True
        # check if divisible by all values
        for number in values:
            if myNum % number == 0:
                continue
            else:
                __doneFlag = False
                break
                
    logger.info("Problem 5 Solution: ")
    logger.info("The smallest number divisible by values 1 to 20 is %d\n"
                % myNum)
    
    return

def problem7():
    """
    Problem 7: Find the 10,001st prime number
    """
    __doneFlag = False
    counter = 6 # start from 13 which is the 6th prime number
    testnum = 14 # next value after 13
    
    while not __doneFlag:
        temp = int(math.ceil(math.sqrt(testnum)))
        for value in range(2, temp+1):
            __isPrime = True
            if testnum % value == 0:
                #not prime
                __isPrime = False
                break
        if __isPrime:
            counter += 1      
        if counter == 10001:
            __doneFlag = True
        if __doneFlag == False:
            testnum += 1
            
    logger.info("Problem 7 Solution:")
    logger.info("The 10,001st prime number is %d\n" % testnum)
    
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
    logger.info('Program Started\n')

    # Problem Functions --------------------------------------------------------
    problem1()
    problem2()
    problem5()
    problem7()
    
    logger.info('Program Completed')
    logger.info('--------------------------------------\n')
    
    return

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    main()


