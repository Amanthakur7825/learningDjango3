from django.test import TestCase
from django.urls import reverse

class BlogViewTests(TestCase):
    def test_post_list_status_code(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, 'My Blog Posts')
