from base.base_test import BaseTest
import pytest



class TestApiRunner:
    base_url = None  # Variable de clase para almacenar la base URL

    @pytest.fixture(scope='session', autouse=True)
    def set_base_url(self, request):
        # Obtener la URL base desde los argumentos de línea de comandos
        TestApiRunner.base_url = request.config.getoption("--base-url")

   
    def test_get_api_sumar(self, api_request_context):
        """ get sumar is 1 + 2 = 3"""

        base_url = f"{TestApiRunner.base_url}"
        print("URL:", base_url)  # Imprime la URL completa        
        response = BaseTest.requests_api_get(self, api_request_context, base_url+"/sumar/1/2")
        print(response)
        
        assert response.status == 200
        assert response.json()["resultado"] == 3

#  pytest src/test_suites/api --html=src/report/reportAPI.html --self-contained-html --numprocesses auto
# pytest src/test_suites/api --html=src/report/reportAPI.html --self-contained-html --numprocesses auto --base-url=https://jamesapisuma.jamesvalencia1.repl.co
