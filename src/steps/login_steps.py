from base.base_test import BaseTest
from repository.repository_login import RepositoryLogin
from playwright.sync_api import expect
import re


class LoginSteps:

    def login(self, username, password):
        '''you are login on app'''

        # create a locator
        txt_user_name = BaseTest.get_locator(self, RepositoryLogin.txt_user_name)
        txt_password = BaseTest.get_locator(self, RepositoryLogin.txt_password)
        btn_login = BaseTest.get_locator(self, RepositoryLogin.btn_login)

        # Expect an attribute "to be strictly equal" to the value.
        BaseTest.expect_if_be_visible(self, btn_login)

        # Input username
        txt_user_name.fill(username)

        # Input password
        txt_password.fill(password)        

        # Click the get started link.
        btn_login.click()


    def validate_correct_environment(self, environment):
        '''Expect the URL to contains intro'''
        BaseTest.expect_of_url(self, re.compile(".*" + environment + ""))

    def validate_company_name(self):
        '''Validate #HeaderCompanyName'''
        locator_company_name = BaseTest.get_locator(self, RepositoryLogin.header_company_name)
        BaseTest.expect_if_be_visible(self, locator_company_name)
        