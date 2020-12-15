from unittest import TestCase
from app import app
from forex import convert, get_currency_symbol, invalid_from_code, invalid_to_code, invalid_amount
app.config['TESTING'] = True


class ForexRoutesTestCase(TestCase):

    def test_home_page(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1 class="text-center">CURRENCY CONVERTER</h1>', html)

    def test_invalid_amount(self):
        with app.test_client() as client:
            res = client.post('/', data={'from': 'USD', 'to': 'JPY', 'amount':""})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<p class="text-center error">Invalid amount</p>', html)

    def test_invalid_from_code(self):
        with app.test_client() as client:
            res = client.post('/', data={'from': 'XXX', 'to': 'JPY', 'amount':10})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<p class="text-center error">Invalid currency: XXX</p>', html)

    def test_invalid_to_code(self):
        with app.test_client() as client:
            res = client.post('/', data={'from': 'USD', 'to': 'ZZZ', 'amount':10})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<p class="text-center error">Invalid currency: ZZZ</p>', html)

    def test_result_display(self):
        with app.test_client() as client:
            res = client.post('/', data={'from': 'USD', 'to': 'USD', 'amount':10})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h2 class="text-center result">US$10.0</h2>', html)



class ForexFunctionsTestCase(TestCase):

    def test_convert(self):
        self.assertEqual(convert('USD', 'USD', 20), 20)


    def test_get_currency_symbol(self):
        self.assertEqual(get_currency_symbol('GBP'), '£')

    def test_from_code(self):
        self.assertTrue(invalid_from_code('XXX'))
        self.assertFalse(invalid_from_code('USD'))

    def test_to_code(self):
        self.assertTrue(invalid_to_code('YYY'))
        self.assertFalse(invalid_to_code('JPY'))

    def test_invalid_amount(self):
        self.assertTrue(invalid_amount(""))
        self.assertFalse(invalid_amount(100))