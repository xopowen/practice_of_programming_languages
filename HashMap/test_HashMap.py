from unittest import TestCase
from HashMap.HashMap import SpecialHashMap

class TestSpecialHashMap(TestCase):
    def setUp(self):
        self.maps = SpecialHashMap()
        self.maps["value2"] = 2
        self.maps["value3"] = 3
        self.maps["value1"] = 1
        self.maps["1"] = 10
        self.maps["2"] = 20
        self.maps["3"] = 30
        self.maps["1, 5"] = 100
        self.maps["5, 5"] = 200
        self.maps["10, 5"] = 300
        self.maps["(1, 5)"] = 100
        self.maps["(5, 5)"] = 200
        self.maps["(10, 5)"] = 300
        self.maps["(1, 5, 3)"] = 400
        self.maps["(5, 5, 4)"] = 500
        self.maps["(10, 5, 5)"] = 600

class Test_iloc(TestSpecialHashMap):
    def test_iloc(self):

        self.fail()

class Test_ploc(TestSpecialHashMap):
    def test_ploc(self):
        self.assertEqual(self.maps.ploc("<>1, >0,>1"),{'(10, 5, 5)': 600, '(5, 5, 4)': 500})
        self.assertEqual(self.maps.ploc("<>1! >0,>1"), {'(10, 5, 5)': 600, '(5, 5, 4)': 500})
        self.assertEqual(self.maps.ploc("<    >1,    >0,>1"), {'(10, 5, 5)': 600, '(5, 5, 4)': 500})
        self.assertEqual(self.maps.ploc("<>1! >0,>!1"), {'(10, 5, 5)': 600, '(5, 5, 4)': 500})
        self.assertEqual(self.maps.ploc("<>1, >0"),{'(10, 5)': 300, '(5, 5)': 200})
        self.assertEqual(self.maps.ploc("<>1"),{'value3': 3, 'value2': 2, 'value1': 1, '(2,)': 20, '(3,)': 30})

    def test_errors(self):
        self.assertRaises(ValueError, self.maps.ploc, "1j")
        self.assertRaises(ValueError, self.maps.ploc, "<>")
        self.assertRaises(ValueError, self.maps.ploc, "<>1, >0,1j ,")
        self.assertRaises(ValueError,self.maps.ploc,"<>1, ,1j")
        self.assertRaises(ValueError, self.maps.ploc, "<>,<>")
        self.assertRaises(ValueError, self.maps.ploc, "<>1,")