import sys
sys.path.append('E:\\工作\\软件\\app\\Gif_Project')
from Page.search_page import Search_Page
from Basic.Init_Driver import init_driver
import time,allure,pytest

class Test_Base:
    #def __init__(self):
    def setup(self):
        self.driver = init_driver()
    '''
    def test_2(self):
        sp = Search_Page(self.driver)
        sp.input_search_text(123)
        #self.driver.quit()
    '''
    @pytest.mark.parametrize('a',[1,2,3])
    #@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step(title="测试步骤001")
    def test_1(self,a):
        allure.attach('描述','我是测试步骤001的描述')
        assert a != 2
    
    def test_2(self):
        sp2 = Search_Page(self.driver)
        sp2.wifi_click()
        #self.driver.quit()
    def teardown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    Test_Base().test()