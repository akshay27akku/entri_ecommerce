from django.test import TestCase

def demo(text1,text2):
    return text1 + text2

class Testdemo(TestCase):
    def test_concentate(self):
        self.assertEqual(demo("python ","program"),"python program")