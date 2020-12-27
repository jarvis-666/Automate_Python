import logging

logging.basicConfig(filename='logging_log.txt', level=logging.CRITICAL, format=' %(asctime)s - %(levelname)s- %(message)s')
# logging.disable(logging.CRITICAL)
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))

logging.debug('End of program')

# using print functions in programs as a means of debugging is a form of logging.
    # logging lets you create custom messages

# basicConfig creates a LogRecord object that holds information about that event

# logging.debug() is used when we want to print log information

# don't get tempted to use print() statements for debugging purposes, as after debugging those need to be removed.

# log messages are meant for programmers and not for users, disable them after debugging

# users errors like invalid input or file not found, should be put in print() function calls and not logging

# logging is done in levels, DEBUG, INFO, WARNING, ERROR, CRITICAL

# at later stages of development, we can choose to only see errors and not debug meassages, so we change the level
    # in logging.basicConfig(level=logging.ERROR)

# passing logging level to logging.disable() will stop logging at that and lower levels