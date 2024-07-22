import unittest

def calc_discount(price):
    if price==0:
        return "Not a item purchased"
    if 1<=price<50:
        return 0
    elif 50<=price<=200:
        return 0.05*price
    elif 201<=price<=500:
        return 0.1*price
    else:
        return 0.15*price

class TestCalcDiscount(unittest.TestCase):
    def test_calc_discount_less_than_lboundary(self):
        self.assertEqual(calc_discount(0), "Not a item purchased")
        self.assertEqual(calc_discount(49), 0)
        self.assertEqual(calc_discount(200), 10)
        self.assertEqual(calc_discount(500), 50)
    
    def test_calc_discount_exactly_at_lboundary(self):
        self.assertEqual(calc_discount(1), 0)
        self.assertEqual(calc_discount(50), 2.5)
        self.assertEqual(calc_discount(201), 20.1)
        self.assertEqual(calc_discount(501), 75.15)

    def test_calc_discount_exactly_at_uboundary(self):
        self.assertEqual(calc_discount(50), 2.5)
        self.assertEqual(calc_discount(200), 10)
        self.assertEqual(calc_discount(500), 50)
    
    # def test_calc_discount_in_the_range(self):
        # self.assertEqual()

if __name__=="__main__":
    unittest.main()