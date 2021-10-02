from django.test import TestCase


# Create your tests here.
class MyTest(TestCase):
    def test_api_overview(self):
        response = self.client.get("/api/")
        return self.assertEqual(response.status_code, 200)

    def test_links(self):
        response = self.client.get("/api/links")
        return self.assertEqual(response.status_code, 200)
