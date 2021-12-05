from django.test import TestCase
from django.core import mail
from .form import *
from selenium import webdriver
driver = webdriver.Chrome(executable_path="./WebDriver/chromedriver")
    
# Create your tests here.
#Used for unit tests
class FunctionTestCase(TestCase):
    #start test and browser
    def setUp(self):
        #self.browser=webdriver.Chrome()
        self.browser=driver
    
    #passed
  #def test_homepage_start(self):
        #self.browser.get("http://localhost:8000")
        #self.assertIn('Hello,',self.browser.page_source)

    ## test forms saved for 
    # book fitting
    #def test_booking_fitting(self):
        #self.browser.get("http://localhost:8000")
        #form = generalEnquiriesForm(data={'name':'mary'})
        #self.assertTrue(form.is_valid())

    # registercustomer and 
    # enquiry
    #def test_enquiry(self):
        #form = generalEnquiriesForm(data={'name':'joey'})
        #self.assertTrue(form.is_valid())

    ## test loaded items contain all fields in html page ie name,image

    ## test image load time less than 3 seconds for singleitem
    #  or page load time for product list
    def test_email(self):
        #create message
        mail.send_mail(
        'Subject title',
        'Message: test email sent.',
        'from@example.com',
        ['to@example.com']
        )
        #test delivered content against expected sent content
        assert len(mail.outbox) == 1, "Inbox is not empty"
        assert mail.outbox[0].subject == 'Subject title'
        assert mail.outbox[0].body == 'Message: test email sent.'
        assert mail.outbox[0].from_email == 'from@example.com'
        assert mail.outbox[0].to == ['to@example.com']


    #close browser
    def tearDown(self):
       self.browser.quit()