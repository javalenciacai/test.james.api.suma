from base.base_test import BaseTest



class TestApiRunner:
     

    base_url = 'https://jamesapisuma.jamesvalencia1.repl.co'
    request_body = {

            
        }

    header = {
            "Content-Type":"application/json",
            "Accept": "*/*",
            "Content-Length":"<calculated when request is sent>"
        }


    def test_get_api_sumar(self, api_request_context):
        """ get sumar is 1 + 2 = 3"""

        response = BaseTest.requests_api_get(self, api_request_context, self.base_url+"/sumar/1/2")
        print(response)
        
        assert response.status == 200
        assert response.json()["resultado"] == 3
#  pytest src/test_suites/api --html=src/report/reportAPI.html --self-contained-html --numprocesses auto