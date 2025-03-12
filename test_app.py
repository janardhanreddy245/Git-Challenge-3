import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    # Set up the test client
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test the home page route
    def test_home_page(self):
        # Send a GET request to the root URL and check the response
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World from Flask', response.data)

if __name__ == '__main__':
    unittest.main()
