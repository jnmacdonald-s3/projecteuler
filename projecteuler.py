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
import random

# ******************************************************************************
# Globals
# ******************************************************************************

primeList = []

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

    # Logger initialization
    logger = logging.getLogger("eulerLog")
    fh = logging.FileHandler("logs/eulerLog.log",mode="w")  # File log
    ch = logging.StreamHandler()  # Console log

    # Logger formats
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

        global primeList
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
                logger.debug("%i%% of range checked, %i primes found"
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


def problem499():
    """
    Problem #499: St. Petersburg Lottery
    """

    # Initialize
    N = 10000  # number of simulations
    m = 2  # cost per game (pounds)
    s0 = 10  # initial fortune (pounds), must be larger than m
    safeZone = 10 * s0 # arbitrary number, if s reaches it, it's a "win"?
    wins = 0
    losses = 0

    for n in xrange(1,N+1):
    
        s = s0
     
        while(1):

            # pay to play the game
            s -= m
            pot = 1   

            while(1):
            
                # Go through coin flip procedure
                coinFlip = random.randrange(0,2)
 
                if coinFlip == 1:
                    pot *= 2

                else:
                    s += pot
                    break
         
            if (s > safeZone):
                wins += 1
                break
  
            if (s < m):
                losses += 1
                break


    winProb = wins/float(N)

    logger.info("Problem #499 Solution:")
    logger.info("AFTER %i SIMULATIONS:"%N)
    logger.info("For m = %i, s = %i"%(m,s0))
    logger.info("The probabilty of never running out of money is %.7f\n"%winProb)

    return


def problem436():
    """
    Problem #436: An unfair bet?
    """

    # Initialization
    N = 1000000  # Number of simulations to run
    xWins = 0
    yWins = 0
    ties = 0

    for n in xrange(1,N+1):
 
        # Set up
        x = 0
        y = 0
        S = 0

        # Player x's turn
        while( S <= 1):
            x = random.uniform(0,1)
            S += x

        # Player y's turn
        while( S <= 2):
            y = random.uniform(0,1)
            S += y

        # Determine winner
        if (x > y):
            xWins += 1

        elif (x < y):
            yWins += 1

        else:
            ties += 0

     
    xWinPrcnt = xWins / float(N) * 100
    yWinPrcnt = yWins / float(N) * 100
    
    logger.info("Problem #436 Solution:")
    logger.info("After %i Simulations"%N)
    logger.info("Player x won %f%% of the time"%xWinPrcnt)
    logger.info("Player y won %f%% of the time\n"%yWinPrcnt)


    return


def problem205():
    """
    Problem #205: Die vs Die
    """    

    # Initialize
    N = 100000
    peterWins_1 = 0
    colinWins_1 = 0
    peterWins_2 = 0
    colinWins_2 = 0


    for n in xrange(1,N):
        
        # First Roll
        peterRoll = random.randrange(1,5)  # 4 sided die
        colinRoll = random.randrange(1,7)  # 6 sided die

        if peterRoll > colinRoll:
            peterWins_1 += 1
      
        elif colinRoll > peterRoll:
            colinWins_1 += 1

        # Second Roll
        peterRoll += random.randrange(1,5)  # 4 sided die
        colinRoll += random.randrange(1,7)  # 6 sided die

        if peterRoll > colinRoll:
            peterWins_2+= 1
      
        elif colinRoll > peterRoll:
            colinWins_2 += 1


    peterWinPrcnt_1 = peterWins_1 / float(N) * 100
    colinWinPrcnt_1 = colinWins_1 / float(N) * 100

    peterWinPrcnt_2 = peterWins_2 / float(N) * 100
    colinWinPrcnt_2 = colinWins_2 / float(N) * 100

    logger.info("Problem #205 Solution")  
    logger.info ("After %i Simulation:"%N)
    logger.info("Peter (1 - 4 sided die) wins %f%% of the time"%peterWinPrcnt_1)
    logger.info ("Colin (1 - 6 sided die) wins %f%% of the time"%colinWinPrcnt_1)
    logger.info ("Peter (2 x 4 sided die) wins %f%% of the time"%peterWinPrcnt_2)
    logger.info("Colin (2 x 6 sided die) wins %f%% of the time\n"%colinWinPrcnt_2)


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
    problem499()
    problem436()
    problem205() 

    # use logging to printout notification that program has terminated
    logger.info("------------------------------")
    logger.info("  Program end")    
    logger.info("------------------------------")
    return

# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()


