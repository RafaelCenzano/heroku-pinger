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

def keep_awake():
    try:
        r = requests.get(config.HOME_URL)
    except Exception as e:
        logger.warn(e)
        exit()
    status = r.status_code

    if status == 200:
        logger.info('Website ping successful')
    else:
        logger.warn('Website ping unsuccessful - running tests on local program')

def main():
    while True:
        keep_awake()
        delay(300)

if __name__ == '__main__':
    main()
