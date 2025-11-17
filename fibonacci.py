import unittest
def fibo(n: int):
    elozo = 0
    most = 1
    veg = 0
    aktszam = [0,1]
    for i in range(n-1):
        most = aktszam[len(aktszam) -1]
        elozo = aktszam[len(aktszam) -2]
        aktszam.append(most + elozo)

    veg = aktszam[len(aktszam)-1]

    return veg

class TesztFibo(unittest.TestCase):
    def test_elso_eset(self):
        veg = fibo(3)
        self.assertEqual(veg,2)
    def test_masodik_eset(self):
        veg = fibo(7)
        self.assertGreater(veg,10)
    def test_harmadik_eset(self):
        veg = fibo(5)
        self.assertGreaterEqual(veg,5)
    def test_negyedik_eset(self):
        veg = fibo(10)
        self.assertLess(veg, 100)
    def test_otodik_eset(self):
        veg = fibo(6)
        self.assertLessEqual(veg, 10)

unittest.main()

