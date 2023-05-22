from base.base_test import BaseTest
from repository.repository_suma import RepositorySuma
from playwright.sync_api import expect
import re


class SumaSteps:

    def suma(self, numero1, numero2):
        '''you are login on app'''

        # create a locator
        txt_numero1 = BaseTest.get_locator(self, RepositorySuma.txt_numero1)
        txt_numero2 = BaseTest.get_locator(self, RepositorySuma.txt_numero2)
        btn_sumar = BaseTest.get_locator(self, RepositorySuma.btn_sumar)

        # Expect an attribute "to be strictly equal" to the value.
        BaseTest.expect_if_be_visible(self, btn_sumar)

        # Input username
        txt_numero1.fill(numero1)

        # Input password
        txt_numero2.fill(numero2)        

        # Click the get started link.
        btn_sumar.click()


    def validate_correct_environment(self, environment):
        '''Expect the URL to contains intro'''
        BaseTest.expect_of_url(self, re.compile(".*" + environment + ""))

    def validate_result(self):
        '''Validate #HeaderCompanyName'''
        lbl_resultado = BaseTest.get_locator(self, RepositorySuma.resultado)
        BaseTest.expect_if_be_visible(self, lbl_resultado)
        