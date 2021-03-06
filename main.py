# Imports
from time import sleep as delay
from configs import config
from logging import Formatter, getLogger, StreamHandler, INFO
from requests import get as ping


formatter = Formatter(
    fmt="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s")
logger = getLogger(__name__)
logger.setLevel(INFO)

console_handler = StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# functions for pinging heroku

def keep_awake(url=config.HOME_URL,testing=False):
    try:
        r = ping(url)
    except Exception as e:
        logger.error(e)
        exit()
    status = r.status_code

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

# Main

def main():

    # test code
    test_awake_function()

    while True:
        check = keep_awake()
        if check == 'test':
            test_awake_function()
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
