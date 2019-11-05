import sys
sys.path.append('E:\\工作\\软件\\app\\Gif_Project')
from appium import webdriver

def init_driver():
    desired_caps = {}
    #手机 系统信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.0'
    ##设备号
    desired_caps['deviceName'] = '192.168.163.103:5555'
    #包名
    desired_caps['appPackage'] = 'com.android.settings'
    #启动名
    desired_caps['appActivity'] = '.Settings'
    #允许输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True 
    #手机驱动对象
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
    return driver