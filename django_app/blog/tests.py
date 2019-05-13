from django.test import TestCase

from blog.models import Blog

class BlogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Blog.objects.create(title="testing model title", body="testing model body")

    def test_title_content(self):
        blogpost = Blog.objects.get(id=1)
        expected_object_name = Blog._meta.get_field('title').verbose_name
        self.assertEquals(expected_object_name, "testing model title")

    def test_body_content(self):
        blogpost = Blog.objects.get(id=1)
        expected_object_name = Blog._meta.get_field('body').verbose_name
        self.assertEquals(expected_object_name, "testing model body")




# # generic test outline from Mozilla
# class YourTestClass(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass
#
#     def setUp(self):
#         print("setUp: Run once for every test method to setup clean data.")
#         pass
#
#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)
#
#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(False)
#
#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)
# #
