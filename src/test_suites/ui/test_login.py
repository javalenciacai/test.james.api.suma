import pytest
from playwright.sync_api import Page
import conftest
from data_test.data_login import DataLogin
from steps.login_steps import LoginSteps
from steps.general_steps import  GeneralSteps


class TestLogin:

    conftest.htmlImg = ''
    conftest.htmlVideo = ''
    
    
    @pytest.mark.parametrize("testdata", [(DataLogin.qa_colombia)])
    def test_login(self, page: Page, testdata) -> None:
        """Description of test: test login for ACME demo app"""
        i = 0
        print(testdata[i]["url"])
        print(testdata[i]["username"])
        GeneralSteps.start_navigate(page,testdata[i]["url"], testdata[i]["title"])    
        LoginSteps.login(page, testdata[i]["username"], "1111") 
        LoginSteps.validate_correct_environment(page, testdata[i]["ValidateENV"])
        LoginSteps.validate_company_name(page)
        GeneralSteps.screenshot(page)
     