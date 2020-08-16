# params
from .chromedriver_init import main as chromedriver_init


# params
_initfunc_d = {
    'chromedriver': chromedriver_init
}


# main class
class webdriver():
    def __init__(self, drivertype):
        '''
        drivertype (str): driver type
        '''
        self.driver = _initfunc_d[drivertype]

    def get_html(self, url):
        return self.driver.get(url)




# testing
if __name__ == '__main__':
    main()
