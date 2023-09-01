import unittest
from Translation import Translation


class Test_Translation_Notation(unittest.TestCase):

    def setUp(self):
        self.dvoi = Translation()

    def test_bin(self):
        for i in range(1,10000):
            self.assertEqual(self.dvoi.Translation(i,2),"{0:b}".format(i))
    def test_oct(self):
        for i in range(1,10000):
            self.assertEqual(self.dvoi.Translation(i,8),"{0:o}".format(i))
    

if __name__ == '__main__':
    unittest.main()