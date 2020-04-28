from django.test import TestCase

# Create your tests here.


class RankViewTest(TestCase):

    def test_post(self):
        response = self.client.post("/rankapi/rank", data={"client": "客户端0", "score": 100})
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        response = self.client.get("/rankapi/rank", data={"client": "客户端0", "start": 1, "end": 10})
        self.assertEqual(response.status_code, 200)
