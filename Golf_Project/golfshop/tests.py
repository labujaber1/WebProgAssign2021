from django.http import response
from django.test import TestCase

from .form import *
from selenium import webdriver

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

    def testSearchProductName(self):
        
        self.client.get("http://localhost:8000", follow=True)
        #enter something in search
        text = self.browser.find_element_by_name('name_name')
        text.send_keys('Mx20')
        
        #click button
        self.browser.find_element_by_name('submit').click()
        #check response is expected 200
        
        self.assertRedirects(response,'/SearchResults',status_code=302,target_status_code=200)

    


    #close browser
    def tearDown(self):
        self.browser.quit()
      