import sys
sys.path.append('E:\\app\\git_program\\Gif_Project')
from selenium.webdriver.support.wait import WebDriverWait

class Base(object):
    def __init__(self,driver):
        self.driver = driver
        
    def find_element(self,loc,timeout=10):
        return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element(*loc))
    
    def click(self,loc):
        self.find_element(loc).click()
        
    def input(self,loc,text):
        self.fm = self.find_element(loc)
        self.fm.clear()
        self.fm.send_keys(text)