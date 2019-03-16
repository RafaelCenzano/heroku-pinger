# Imports
import requests
from configs import config
import logging
from time import sleep as delay

formatter = logging.Formatter(
    fmt="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# functions for pinging heroku

def keep_awake(url=config.HOME_URL,testing=False):
    try:
        r = requests.get(url)
    except Exception as e:
        logger.error(e)
        exit()
    status = r.status_code

    if status == 200:
        logger.info('Website ping successful')
        test_check = True
    else:
        logger.warn('Website ping unsuccessful - running tests on local program')
        test_check = False

    if testing == True:
        return test_check
# Main

def main():
    while True:
        keep_awake()
        delay(300)

# Tests

def check_test_result(result):
    if result == False:
        logger.error('Test failed - exiting')
        exit()
    else:
        logger.debug('Test passed')

def test_awake_function():

    test_check1 = keep_awake(url='https://www.google.com/', testing=True)
    check_test_result(test_check1)
    test_check2 = keep_awake(url='https://www.facebook.com/', testing=True)
    check_test_result(test_check2)
    test_check3 = keep_awake(url='https://github.com/', testing=True)
    check_test_result(test_check3)
    test_check4 = keep_awake(url='https://stackoverflow.com/', testing=True)
    check_test_result(test_check4)
    logger.info('Tests passed')

if __name__ == '__main__':
    main()
