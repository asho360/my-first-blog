from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

import blog.views

class BaseTests(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_cv_home_page_returns_correct_html(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv_home.html')