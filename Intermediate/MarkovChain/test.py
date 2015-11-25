'''
Created on 2 Apr 2015

@author: paulross
'''
import unittest
import MarkovChain

class Test(unittest.TestCase):


    def setUp(self):
        self._c = MarkovChain.MarkovChain()

    def tearDown(self):
        pass

    def test_AB_table(self):
        self._c.add('A', 'B')
        self._c.add('B', 'A')
        self.assertEqual(self._c.probability_table('A'), {'B' : 1.0})
        self.assertEqual(self._c.probability_table('B'), {'A' : 1.0})

    def test_AB_most(self):
        self._c.add('A', 'B')
        self._c.add('B', 'A')
        self.assertEqual(('B',), self._c.most_probable('A'))
        self.assertEqual(('A',), self._c.most_probable('B'))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()