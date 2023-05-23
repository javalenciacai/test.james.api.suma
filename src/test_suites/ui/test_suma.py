import pytest
from playwright.sync_api import Page
import conftest
from data_test.data_suma import DataSuma
from steps.suma_steps import SumaSteps
from steps.general_steps import  GeneralSteps


class TestLogin:

    base_url = None  # Variable de clase para almacenar la base URL
    conftest.htmlImg = ''
    conftest.htmlVideo = ''

    @pytest.fixture(scope='session', autouse=True)
    def set_base_url(self, request):
        # Obtener la URL base desde los argumentos de línea de comandos
        TestLogin.base_url = request.config.getoption("--base-url")
    
    
    @pytest.mark.parametrize("testdata", [(DataSuma.qa_colombia)])
    def test_login(self, page: Page, testdata) -> None:
        """Description of test: test suma """
        i = 0
        base_url = f"{TestLogin.base_url}"
        print("URL:", base_url)  # Imprime la URL completa   
        print(testdata[i]["url"])
        GeneralSteps.start_navigate(page,base_url, testdata[i]["title"])    
        SumaSteps.suma(page, testdata[i]["Numero1"], "1") 
        SumaSteps.validate_result(page)
        SumaSteps.validate_correct_environment(page, testdata[i]["ValidateENV"])        
        GeneralSteps.screenshot(page)
     

#   pytest src/test_suites/ui --html=src/report/report.html --self-contained-html --numprocesses 4 -k "alguna palabra dentro del nombre del test"

# pytest src/test_suites/ui --html=src/report/report.html --self-contained-html --base-url=https://jamesfrontsuma.jamesvalencia1.repl.co/