import unittest
from app.models import Quote

class TestQuote(unittest.TestCase):
    def setUp(self):
    
        self.random_quote = Quote( "Caleb","Never give up")

    def test_instance(self):
        self.assertTrue(isinstance(self.random_quote, Quote))

    def test_init(self):
        self.assertEqual(self.random_quote.author,"Caleb" )
        self.assertEqual(self.random_quote.quote,"Never give up")