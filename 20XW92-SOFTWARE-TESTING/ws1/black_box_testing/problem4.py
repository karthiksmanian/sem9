import unittest

def order_pizza(n):
    if 1<=n<=10:
        return "Success"
    elif 11<=n<=100:
        return "Only 10 Pizza can be ordered."
    else:
        return "Invalid"

class TestOrderPizza(unittest.TestCase):
    def test_order_pizza_less_than_lb(self):
        self.assertEqual(order_pizza(0), "Invalid")
    
    def test_order_pizza_on_lb(self):
        self.assertEqual(order_pizza(1), "Success")
        self.assertEqual(order_pizza(11), "Only 10 Pizza can be ordered.")

    def test_order_pizza_on_rb(self):
        self.assertEqual(order_pizza(10), "Success")
        self.assertEqual(order_pizza(100), "Only 10 Pizza can be ordered.")

    def test_order_pizza_greater_than_rb(self):
        self.assertEqual(order_pizza(101), "Invalid")
    
    def test_order_pizza(self):
        self.assertEqual(order_pizza(50), "Only 10 Pizza can be ordered.")

if __name__=="__main__":
    unittest.main()