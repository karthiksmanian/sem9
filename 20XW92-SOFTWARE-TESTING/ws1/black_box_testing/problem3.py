# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import unittest

def calculate_average(marks):
    n = len(marks)
    tot = sum(marks)
    return tot/n

def check_marks(*marks):
    avg = calculate_average(marks)
    if avg>100 or avg<0:
        return "Invalid"
    
    if avg>=90 and avg<=100:
        return "Distinction"
    elif avg>=75 and avg<=89:
        return "First Class"
    elif avg>=60 and avg<=74:
        return "Second Class"
    elif avg>=50 and avg<=59:
        return "Third Class"
    else:
        return "Fail"

class TestCheckMarks(unittest.TestCase):

    def test_check_marks_below_lb(self):
        self.assertEqual(check_marks(89,89,89),"First Class")
        self.assertEqual(check_marks(74,74,74),"Second Class")
        self.assertEqual(check_marks(59,59,59),"Third Class")
        self.assertEqual(check_marks(49,49,49),"Fail")
        
    def test_check_marks_at_lb(self):
        self.assertEqual(check_marks(90,90,90),"Distinction")
        self.assertEqual(check_marks(75,75,75),"First Class")
        self.assertEqual(check_marks(50,50,50),"Third Class")

    def test_check_marks_in_mid(self):
        self.assertEqual(check_marks(94,94,94),"Distinction")
        self.assertEqual(check_marks(77,77,77),"First Class")

    def test_check_marks_at_rb(self):
        self.assertEqual(check_marks(100,100,100),"Distinction")
        self.assertEqual(check_marks(89,89,89),"First Class")

    def test_check_marks_above_rb(self):
        self.assertEqual(check_marks(101,101,101),"Invalid")
        self.assertEqual(check_marks(89,89,89),"First Class")

if __name__=="__main__":
    unittest.main()