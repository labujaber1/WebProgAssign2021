from django.http import response
from django.test import TestCase
from django.test.client import Client
from .models import Product
from .form import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from django.urls import reverse
# Create your tests here.

#Used for unit tests
class FunctionTestCase(TestCase):
    #start test and browser
    def setUp(self):
        self.browser=webdriver.Firefox()
        

    #passed
    #test home page returns response code 200
    # def testHomeResponse(self):
    #     response = self.client.get('/')
    #     self.assertEquals(response.status_code, 200)


    #passed test home page for string hello
    #expected result
    # def test_homepage_start(self):
    #     self.browser.get("http://localhost:8000")
    #     self.assertIn('Hello,',self.browser.page_source)

    ## test forms saved for 
    # book fitting contain Single
    #failed which is true - expected result for Book,
    #passed - expected result for Book
    # def testBookingFitting(self):
    #     self.browser.get("http://localhost:8000/BookFitting")
    #     self.assertIn('Book ',self.browser.page_source)

    
    #passed - all products not in ProductList.html
    # def testOrderRequest(self):
    #     response = self.client.get('/ProductList/')
    #     self.assertNotContains(response, 'All products')

    #passed
    # def testUrlsList(self):
    #     client= Client()
    #     response = client.get(reverse('ProductList'))
    #     response.status_code
    #     self.assertEquals(response.status_code, 200)

    #passed
    # def testURLAccess(self):
    #     client = Client()
    #     response = client.get(reverse('ProductListAccess'))
    #     response.status_code
    #     self.assertEquals(response.status_code, 200)

    #passed
    # def testURLClub(self):
    #     client = Client()
    #     response = client.get(reverse('ProductListClub'))
    #     response.status_code
    #     self.assertEquals(response.status_code, 200)

    #passed
    # def testURLClubset(self):
    #     client = Client()
    #     response = client.get(reverse('ProductListSet'))
    #     response.status_code
    #     self.assertEquals(response.status_code, 200)

    #expect to fail to test date format, also 32 for day - failed as expected
    #failed unexpected using '/' instead of '-'. Change datefield to auto in order request 
    #form and date widget for this form
    # def testFitting(self):
    #     client = Client()
    #     fitting = BookFitting(name='Jo',description='Something',fitting_date='25/12/2021',contact_details='jo@jo.com')
    #     fitting.save()
    #     response = client.get(fitting.get_absolute_url())
    #     response.status_code
    #     self.assertEquals(response.status_code, 200)

    #save data check response
    def testFitting(self):
        client = Client()
        fitting = BookFitting(name='Jo',description='Something',fitting_date='2021-12-25',contact_details='jo@jo.com')
        fitting.save()
        self.assertEquals(fitting.status_code, 200)


    #add text to search and submit, check if response 200 to redirect to other page
    ##failed cannot find id_name - in navbar, uses include to add to page
    # def testSearchProductName(self):
    #     self.browser.get("http://127.0.0.1:8000")
        
    #     #wait as its in (navbar) other frame in secs
    #     driver = webdriver.Firefox()
    #     driver.implicitly_wait(4) 
    #     #enter something in search
    #     text = self.browser.find_element_by_id('id_name')
        
    #     text.send_keys('Mx20')
    #     #click button
    #     self.browser.find_element_by_name('submit').click()
    #     #check response is expected 200
    #     self.assertRedirects(response,'/SearchResults',status_code=302,target_status_code=200)

    


    #close browser
    def tearDown(self):
        self.browser.quit()
      