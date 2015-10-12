#!/usr/bin/env python

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
from math import *
import argparse
import numpy
import os.path

# ******************************************************************************
# Globals
# ******************************************************************************

primeList = []  # Modified in problem10()

# ******************************************************************************
# Functions
# ******************************************************************************

def get_arguments():
    """
    Get args from command line and return the important info to main
    """
    global logger

    parser = argparse.ArgumentParser()
    parser.add_argument("-v","--verbose",action="store_true",help="Switches on "
                       "verbose logging functionality")
    __args = parser.parse_args()

    # Logger set up
    logger = logging.getLogger("eulerLog")
    fh = logging.FileHandler("eulerLog.log",mode="w")
    ch = logging.StreamHandler()

    logFileFormat = logging.Formatter(
        "%(asctime)s [ %(funcName)s:%(lineno)d ] %(levelname)s: %(message)s"
        )
    consLogFormat = logging.Formatter(
        "[ %(funcName)s:%(lineno)d ] %(levelname)s: %(message)s"
        )

    fh.setFormatter(logFileFormat)
    ch.setFormatter(consLogFormat)

    logger.addHandler(fh)
    logger.addHandler(ch)

    if __args.verbose:
    # Set logging level to DEBUG
        logger.setLevel(logging.DEBUG)
        logger.info("Level set to DEBUG")
 
    else:
    # Set logging level to INFO
        logger.setLevel(logging.INFO)
        logger.info("Logging level set to INFO")
 
    return __args


def problem1():
    """ 
    Problem 1: Find the sum of all natural numbers below 1000 which are 
        multiples of 3 and 5
    """
    runningSum = 0

    logger.debug("Problem #1 iterations started")

    for x in range (1,1000):
        if x%3 == 0 and x%5 == 0:
            runningSum += x

    logger.debug("Iterations complete")

    answer = ("Sum of numbers on (0,1000) divisible by 3,5 "
	      "is %i\n" %runningSum )

    logger.info("Problem #1 Solution:")
    logger.info(answer)
    
    return


def problem2():
    """
    Problem #2: Find the sum of even valued terms < 4e6 of the 
    Fibonacci sequence
    """    
    # Initialization
    maxVal = 4e6
    a = 0
    b = 1
    c = a + b
    runningSum = 0

    logger.debug("Variables initiated, begging loop")

    while(1):

        if c > maxVal:
            break

        if c%2 == 0:
            runningSum += c

        # Iterate
        c = a + b
        a = b
        b = c

    logger.debug("Loop terminated at value c=%i"%c)
    logger.debug("Last used value was c=%i"%a)
    logger.info("Problem #2 Solution:")
    logger.info("Sum of even Finonacci terms less than 4e6 = %i\n"%runningSum)
    return

def problem10():
    """
    Problem 10: Find the sum of all primes below 2e6
    """
    global primeList

    # Initialize
    N = 2e6      # Problem's upper bound
                 #   I need to later integrate it into primes.data

    if os.path.isfile("primes.dat"):
        logger.debug("Prime data file found")
        logger.debug("Reading in data from file")
        primeList = numpy.loadtxt("primes.dat",dtype="int")
        primeCount = primeList.size

    else:
        logger.debug("No file found. Calculations beginning")
        N = 2e6
        primeCount = 2  # Accounting for 1 and 2 already
        n = 3
        primeList.append(1)
        primeList.append(2)
        
        logger.debug("Brute Force 'isPrime' loop start")

        # Brute force it
        while n <= N:
            bound = int( ceil( sqrt(n)+1 ) )  # All you need to check
            for ii in range(2,bound+1):

    	        if n%ii == 0:
                # Then it is not prime
                    break
 
            if ii == bound:
                primeList.append(n)
                primeCount += 1

            if n % (N/10.) == 0:
            # Status Update
                percentComplete = n/float(N) * 100
                logger.debug("%i%% complete, %i primes found"
                             %(percentComplete,primeCount)
                            )
            n += 1

        numpy.savetxt("primes.dat",primeList,fmt="%i")
        logger.debug("Loop completed")

    # Now calculate the sum of the primes
    primesSum = sum(primeList)

    logger.debug("%i primes found"%primeCount)
    logger.info("Problem #10 Solution:")
    logger.info("The sum of primes <= %i is %i\n"%(N,primesSum))

    return
  
def problem35():
    """
    Problem #35: How many circular primes are there below 1e6?
    """

    # Initialize
    global primeList
    num = [None]* 6  # Since it's < 1e6 we know there are 5 digits max
    upperBound = 100
   
    # Main loop
    for p in primeList:
        # Check stopping condition
        if p >= upperBound:
            break

        # Break up p into a 6 digit number, starting with the smallest
        for i in reversed(xrange(6)):
            num[i] = p%10
            p /= 10
    x1 = 7 in primeList
    x2 = 4 in primeList
    print x1
    print x2


# ******************************************************************************
# Main
# ******************************************************************************

def main():
    """
    Main will run all problem functions and sequentially returning each problem
    solution to stdout as well as "projecteuler.log"
    """
    __args = get_arguments()
    
    # use logging to printout notification that program has started

    logger.info("------------------------------")
    logger.info("  Program start")
    logger.info("------------------------------")

    # Problem Functions --------------------------------------------------------

#    problem1()
#    problem2()
    problem10() 
    problem35()    
  
    # use logging to printout notification that program has terminated
    logger.info("------------------------------")
    logger.info("  Program end")    
    logger.info("------------------------------")
    return

# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()


