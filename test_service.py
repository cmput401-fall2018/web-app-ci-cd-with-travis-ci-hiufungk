from unittest import TestCase
from unittest.mock import patch
from service import Service

class TestService(TestCase):
    def setUp(self):
        self.service = Service()
    
    @patch("service.Service.bad_random", return_value=10)
    def test_bad_random(self, mock_bad_random):
        self.assertEqual(self.service.bad_random(),10)
    
    @patch("service.Service.bad_random", return_value=10)
    def test_divide(self, mock_bad_random):
        self.assertEqual(self.service.divide(2), 5)
        try:
            self.service.divide(0)
            self.assertEqual(True, False)
        except:
            self.assertEqual(True, True)
        try:
            self.service.divide("sghf")
            self.assertEqual(True, False)
        except:
            self.assertEqual(True, True)

    def test_abs_plus(self):
        self.assertEqual(self.service.abs_plus(-1), 2)
        self.assertEqual(self.service.abs_plus(0), 1)
        self.assertEqual(self.service.abs_plus(1), 2)
        try:
            self.service.abs_plus("jksdfhhdfbd")
            self.assertEqual(True, False)
        except:
            self.assertEqual(True, True)
        
    
    @patch("service.Service.bad_random")    
    def test_complicated_function(self, mock_bad_random):
        mock_bad_random.return_value = 10
        rv1, rv2 = self.service.complicated_function(2)
        self.assertEqual(rv1, 5)
        self.assertEqual(rv2, 0)
        mock_bad_random.return_value = 11
        rv1, rv2 = self.service.complicated_function(2)
        self.assertEqual(rv1, 5.5)
        self.assertEqual(rv2, 1)       
