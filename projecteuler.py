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
    fh = logging.FileHandler("logs/eulerLog.log",mode="w")
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

    if os.path.isfile("data/primes.dat"):
        logger.debug("Prime data file found")
        logger.debug("Reading in data from file")
        primeList = numpy.loadtxt("data/primes.dat",dtype="int")
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

        numpy.savetxt("data/primes.dat",primeList,fmt="%i")
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
    upperBound = 1e6
    p_new = 0
    circPrimeList = []

    if os.path.isfile("data/circularPrimes.dat"):
        logger.debug("Circular Prime Data file found")
        logger.debug("Reading in data from file")
        circPrimeList = numpy.loadtxt("data/circularPrimes.dat",dtype="int")
        numCircPrime = circPrimeList.size
  
    else:
        logger.debug("No data file found, calculations beginning")
        # Main loop
        for p in primeList:
            # Check stopping condition
            if p >= upperBound:
                break

            # Break up p into a 6 digit number, starting with the smallest
            p_tmp = p
            numDigits = len(str(p_tmp))
            num = [None]*numDigits
            for i in reversed(xrange(numDigits)):
                num[i] = p_tmp%10
                p_tmp /= 10

            # Now check all cyclic permutations of this number for primality
            circPrime = True  # default switch value
            for x in range(0,numDigits):
                for i in xrange(0,numDigits):
                    ii = (x-i) % numDigits  # modulate it across the digits 
                    p_new += num[i]*10**ii
            
                if p_new not in primeList:
                    p_new = 0
                    circPrime = False
                    break 

                p_new = 0
        
            if circPrime:
                circPrimeList.append(p)

        numCircPrime = len(circPrimeList)

        logger.debug("Saving circular primes to a file")
        numpy.savetxt("data/circularPrimes.dat",circPrimeList,fmt="%i")

    logger.info("Problem #35 Solution:")
    logger.info("There are %i circular primes under one million\n"%numCircPrime)

    return

def sqrtEst(x=20):
    """
    Calculating the square root of a number using bisection method
    """
    # Initialize
    n = 0
    a = 0.0
    b = float(x)
    TOL = 1e-8
    N = 1e4
    NaN = numpy.NaN
    fc = NaN

    if x <= 0:
        logger.error("Error: choose x > 0")
        return

    # Begin the bisection method
    while(1):

        fc_prev = fc
        n += 1
        c = (b+a) / 2.0

        fa = a*a - x
        fb = b*b - x
        fc = c*c - x

        tol = abs(fc-fc_prev)
        if tol < TOL or n >= N:
            break

        if fa*fc > 0:
            a = c
        else:
            b = c

    logger.info("After %i iterations:"%n)
    logger.info("The sqrt of %f is approx = %.8f\n"%(x,c))

    return

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
    logger.info("------------------------------\n")

    # Problem Functions --------------------------------------------------------

    problem1()
    problem2()
    problem10() 
    problem35()    
    sqrtEst()

    # use logging to printout notification that program has terminated
    logger.info("------------------------------")
    logger.info("  Program end")    
    logger.info("------------------------------")
    return

# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()


