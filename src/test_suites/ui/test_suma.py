import pytest
from playwright.sync_api import Page
import conftest
from data_test.data_suma import DataSuma
from steps.suma_steps import SumaSteps
from steps.general_steps import  GeneralSteps


class TestLogin:

    conftest.htmlImg = ''
    conftest.htmlVideo = ''
    
    
    @pytest.mark.parametrize("testdata", [(DataSuma.qa_colombia)])
    def test_login(self, page: Page, testdata) -> None:
        """Description of test: test suma """
        i = 0
        print(testdata[i]["url"])
        GeneralSteps.start_navigate(page,testdata[i]["url"], testdata[i]["title"])    
        SumaSteps.suma(page, testdata[i]["Numero1"], "1") 
        SumaSteps.validate_result(page)
        SumaSteps.validate_correct_environment(page, testdata[i]["ValidateENV"])        
        GeneralSteps.screenshot(page)
     

#   pytest src/test_suites/ui --html=src/report/report.html --self-contained-html --numprocesses 4 -k "alguna palabra dentro del nombre del test"