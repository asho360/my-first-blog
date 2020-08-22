from django.test import TestCase
from django.http import HttpRequest
import blog.views
from .models import CV, Experience


class CVBaseTests(TestCase):

    def test_cv_home_page_returns_correct_html(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv_home.html')

    def test_cv_edit_page_returns_correct_html(self):
        response = self.client.get('/cv/edit_cv/')
        self.assertTemplateUsed(response, 'cv/edit_cv.html')

    def test_show_cv(self):
        CV.objects.create(name='nameTest', address='addressTest', number='numberTest', email='emailTest', bio='bioTest')
        
        response = self.client.get('/cv/')

        self.assertIn('nameTest', response.content.decode())
        self.assertIn('addressTest', response.content.decode())
        self.assertIn('numberTest', response.content.decode())
        self.assertIn('emailTest', response.content.decode())
        self.assertIn('bioTest', response.content.decode())

    def test_show_Experiences(self):
        Experience.objects.create(title="titleTest", company="companyTest", description="descriptionTest", start_date="2020-03-01", end_date="2020-08-12")

        response = self.client.get('/cv/')

        self.assertIn('titleTest', response.content.decode())
        self.assertIn('companyTest', response.content.decode())
        self.assertIn('descriptionTest', response.content.decode())
        self.assertIn('March 1, 2020', response.content.decode())
        self.assertIn('Aug. 12, 2020', response.content.decode())

class EditCVTest(TestCase):

    def test_save_a_POST_request(self):
    
        response = self.client.post('/cv/edit_cv/', data={'name': 'nameTest', 'address': 'addressTest', 'number': 'numberTest', 'email': 'emailTest', 'bio': 'bioTest'})
        self.assertRedirects(response, '/cv/')

        self.assertEqual(CV.objects.count(), 1)
        cv = CV.objects.first()
        self.assertEqual(cv.name, 'nameTest')
        self.assertEqual(cv.address, 'addressTest')
        self.assertEqual(cv.number, 'numberTest')
        self.assertEqual(cv.email, 'emailTest')
        self.assertEqual(cv.bio, 'bioTest')