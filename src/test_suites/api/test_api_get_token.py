from base.base_test import BaseTest



# base https://rapidapi.com/BraveNewCoin/api/bravenewcoin/

class TestApiRunner:
     

    base_url = 'https://bravenewcoin.p.rapidapi.com/'
    request_body = {

            "audience": "https://api.bravenewcoin.com",
            "client_id": "oCdQoZoI96ERE9HY3sQ7JmbACfBf55RY",
            "grant_type": "client_credentials"
        }

    header = {
            "Content-Type":"application/json",
            "x-rapidapi-host": "bravenewcoin.p.rapidapi.com",
            "x-rapidapi-key":"d9eb65d125msh597cb72df1a399ap10f1a2jsn5cd1769942d4",
            "Content-Length":"<calculated when request is sent>"
        }


    def test_get_api_token(self, api_request_context):
        """ get token bravenewcoin"""

        response = BaseTest.requests_api_post(self, api_request_context, self.base_url+"oauth/token",self.request_body, self.header)
        print(response.json()["access_token"])
        
        assert response.status == 200
