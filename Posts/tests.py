from django.test import TestCase


# Create your tests here.
class MyTest(TestCase):
    def test_worker(self):
        response = self.client.post("/api/worker")
        self.assertEqual(response.status_code, 200)

    def test_api_overview(self):
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, 200)

    def test_links(self):
        response = self.client.get("/api/links")
        self.assertEqual(response.status_code, 200)
