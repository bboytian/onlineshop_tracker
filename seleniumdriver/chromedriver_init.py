# imports
import os
import os.path as osp

import selenium.common.exceptions as sncmer
import selenium.webdriver as snwd

from ..global_imports import *

# params
_driver_dir = osp.dirname(osp.abspath(__file__)) + 'webdrivers'


# main func
@verbose
@announcer
def main():
    '''
    Future
        - There is a block commented out that seems to be a bug
          fix for an outdated raspberry chrome driver. This is
          left here in case we need it in the future

    Return
        driver (snwd.Chrome)
        None, if no driver is found, a notification should be sent
    '''
    webdrivername_l = FINDFILESFN(_driver_dir + '/*')
    for webdrivername in webdrivername_l:
        driver_dir = DIRCONFN(_driver_dir, webdrivername)

        chrome_options = snwd.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        # ## for bug in selenium/rasp
        # if webdriver_str == 'chromedriver_rasp32_74':
        #     chrome_options.add_argument(
        #         '--disable-features=VizDisplayCompositor')

        try:                # driver OS is correct
            driver = snwd.Chrome(driver_dir,
                                 options=chrome_options)
            return driver

        except (OSError, sncmer.SessionNotCreatedException) as e:
        # wrong OS or wrong version, trying the next one in lst
            continue


# testing
if __name__ == '__main__':
    main()
