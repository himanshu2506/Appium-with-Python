from appium import webdriver
from main_package.commonLib import XML_Lib


class Launch:
    cap = XML_Lib.XML_Lib()

    desired_cap = {
        "platformName": cap.reader('platformName', 'capability'),
        "deviceName": cap.reader('deviceName', 'capability'),
        "platformVersion": cap.reader('platformVersion', 'capability'),
        "appActivity": cap.reader('appActivity', 'capability'),
        "appPackage": cap.reader('appPackage', 'capability'),
        "path": cap.reader('path', 'capability')
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    driver.implicitly_wait(1)
