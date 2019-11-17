from time import sleep
from appium import webdriver
class TestXueqiu:
    def setup(self):
        caps={}
        #todo：这些设置是在这里
        #todo：https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md
        caps["platformName"]="android"
        caps["deviceName"]="myHonor"
        caps["appPackage"]="com.xueqiu.android"
        caps["appActivity"]=".view.WelcomeActivityAlias"
        caps["autoGrandPermission"]=True

        self.driver=webdriver.Remote("http://localhost:4723/wd/hub",caps)
        self.driver.implicitly_wait(20)

    def test_guanzhu(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/quick_action").click()



