# Imports
from time import sleep as delay
from configs import config
from logging import Formatter, getLogger, StreamHandler, INFO
from requests import get as ping
from threading import Thread

# Logger setup
formatter = Formatter(
    fmt="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s")
logger = getLogger(__name__)
logger.setLevel(INFO)
# Logger setup for logging to console
console_handler = StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# functions for pinging heroku

def keep_awake(url=config.HOME_URL,testing=False):
    # Try requesting url
    try:
        r = ping(url)
    except Exception as e:
        logger.error(e)
        exit()
    status = r.status_code

    # checking status code
    if status == 200:
        logger.info('Website ping successful')
        if testing == True:
            return True
    else:
        logger.warn('Website ping unsuccessful - running tests on local program')
        if testing == True:
            return False
        else:
            return 'test'

    return 'clear'

# Function that restarts to thread to allow program to keep running

def restarter(count=0):
    if count != 10:
        check = keep_awake()
        if check == 'test':
            test_awake_function()
        delay(60*2)
        newcount = count + 1
        restarter(count=newcount)
    else:
        pass

# Tests

def check_test_result(result):
    # Check if test was successful
    if result == False:
        logger.error('Test failed - exiting')
        exit()
    else:
        logger.debug('Test passed')

def test_awake_function():

    # ping 4 websites that have high uptime
    test_check1 = keep_awake(url='https://www.google.com/', testing=True)
    check_test_result(test_check1)
    test_check2 = keep_awake(url='https://www.facebook.com/', testing=True)
    check_test_result(test_check2)
    test_check3 = keep_awake(url='https://github.com/', testing=True)
    check_test_result(test_check3)
    test_check4 = keep_awake(url='https://stackoverflow.com/', testing=True)
    check_test_result(test_check4)
    logger.info('Tests passed')


# Main

def main(count=0):

    # escape if tests don't work
    test_awake_function()
    restarter()

    # Loop main function 5 times

    if count == 5:
        exit()

    current_count = count + 1
    main(current_count)

if __name__ == '__main__':
    main()
