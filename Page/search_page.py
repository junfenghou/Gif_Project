import sys
sys.path.append('E:\\工作\\软件\\app\\Gif_Project')
from Basic.Base import Base
import Page

class Search_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
        
    def input_search_text(self,text):
        self.click(Page.search_button)
        self.input(Page.search_text,text)
        self.click(Page.search_return_button)
        
    def wifi_click(self):
        self.click(Page.wifi_button)

