from base.base_test import BaseTest

class GeneralSteps:


    def start_navigate(self, url, page_title):
        '''start recording video and navigating in the application'''     
        BaseTest.get_video(self)            
        BaseTest.get_navigate(self, url, page_title)
    
    def screenshot(self):
        '''takes evidence of the end of the test if it passes'''
        BaseTest.get_screenshot(self)
    