import unittest
import calc

class TestForFunction(unittest.TestCase):

    def test_summa(self):
        self.assertEqual(calc.summa(2,3),5)
        self.assertEqual(calc.summa(3, -6),-3)
        self.assertEqual(calc.summa(0,0),0)
        self.assertEqual(calc.summa(0.5, 0.2), 0.7)
        #negotive test
        self.assertRaises(ValueError, calc.summa,'k',0)
        self.assertRaises(ValueError, calc.summa, 3, 'rty')
        self.assertRaises(ValueError, calc.summa, 'k', 'sdfg')

    def test_sub(self):
        self.assertEqual(calc.sub(2,3),-1)
        self.assertEqual(calc.sub(3, -6),9)
        self.assertEqual(calc.sub(0,0),0)
        self.assertEqual(calc.sub(7, 2), 5)
        self.assertEqual(calc.sub(5.2, 0.2), 5)
        #negotive test
        self.assertRaises(ValueError, calc.sub,'iu',16)
        self.assertRaises(ValueError, calc.sub, 0.5, 'ert')
        self.assertRaises(ValueError, calc.sub,'gj', 's')

    def test_mult(self):
        self.assertEqual(calc.mult(2,3),6)
        self.assertEqual(calc.mult(4, -6),-24)
        self.assertEqual(calc.mult(0,100),0)
        self.assertEqual(calc.mult(1, 9), 9)
        self.assertEqual(calc.mult(0.5, 9), 4.5)
        #negotive test
        self.assertRaises(ValueError, calc.mult,'mm',1.12)
        self.assertRaises(ValueError, calc.mult, 4, 'fs')
        self.assertRaises(ValueError, calc.mult,'yt', 'tu')

    def test_div(self):
        self.assertEqual(calc.div(4, 2), 2)
        self.assertEqual(calc.div(12, -6), -2)
        self.assertEqual(calc.div(62, 1), 62)
        self.assertEqual(calc.div(-3, 5), -0.6)
        self.assertEqual(calc.div(0, 21), 0)
        self.assertEqual(calc.div(3, 0.1), 30)
        self.assertEqual(calc.div(0.4, 2), 0.2)
        # negotive test
        self.assertRaises(ValueError, calc.div, 'qq', 11)
        self.assertRaises(ValueError, calc.div, 2, 't')
        self.assertRaises(ValueError, calc.div, 'nc', 'u')
        self.assertRaises(ArithmeticError, calc.div, 5, 0)

    def test_sqrt(self):
        self.assertEqual(calc.sqrt(4), 2)
        self.assertEqual(calc.sqrt(9), 3)
        self.assertEqual(calc.sqrt(1), 1)
        self.assertEqual(calc.sqrt(0), 0)
        self.assertEqual(calc.sqrt(5), 2.23606797749979)
        self.assertEqual(calc.sqrt(0.04), 0.2)
        # negotive test
        self.assertRaises(ValueError, calc.sqrt, 'qq')
        self.assertRaises(ValueError, calc.sqrt, 'nc')
        self.assertRaises(ArithmeticError, calc.sqrt, -1)

    def test_factorial(self):
        self.assertEqual(calc.factorial(3), 6)
        self.assertEqual(calc.factorial(9), 362880)
        self.assertEqual(calc.factorial(1), 1)
        self.assertEqual(calc.factorial(0), 1)
        # negotive test
        self.assertRaises(ValueError, calc.factorial, 'qq')
        self.assertRaises(ValueError, calc.factorial, 'nc')
        self.assertRaises(ValueError, calc.factorial, 0.3)
        self.assertRaises(ArithmeticError, calc.factorial, -1)

    def test_degree(self):
        self.assertEqual(calc.degree(3,3), 27)
        self.assertEqual(calc.degree(1,4), 1)
        self.assertEqual(calc.degree(0, 5), 0)
        self.assertEqual(calc.degree(5, 0), 1)
        self.assertEqual(calc.degree(-3, 4), 81)
        self.assertEqual(calc.degree(6, -2), 0.027777777777777776)
        self.assertEqual(calc.degree(-5, 3), -125)
        # negotive test
        self.assertRaises(ValueError, calc.degree, 'qq', 0.4)
        self.assertRaises(ValueError, calc.degree, 3, 'nc')