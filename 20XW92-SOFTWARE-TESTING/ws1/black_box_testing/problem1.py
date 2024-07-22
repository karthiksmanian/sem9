import unittest

def password_screening(s):
    s_len = len(s)

    if s_len<6 or s_len>12:
        return False
    
    return True

class TestPasswordValidator(unittest.TestCase):
    def test_passlen_less_than6(self):
        self.assertEqual(password_screening("abcde"),False)
    
    def test_passlen_exactly6(self):
        self.assertEqual(password_screening("abcdef"),True)

    def test_passlen_bwin7_11(self):
        self.assertEqual(password_screening("abcdefg"),True)
    
    def test_passlen_exactly12(self):
        self.assertEqual(password_screening("abcdefghijkl"),True)
    
    def test_passlen_more_than12(self):
        self.assertEqual(password_screening("aabcdefghijklm"),False)

if __name__ == "__main__":
    unittest.main()