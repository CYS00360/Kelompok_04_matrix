import unittest
from coba1 import Matrix


class TestMatrix(unittest.TestCase):

    def test_row_1(self):
        m = Matrix("1")
        hasil = m.row(1)
        print("row(1) =", hasil)
        self.assertEqual(hasil, [1])

    def test_row_2(self):
        m = Matrix("1 2\n3 4")
        hasil = m.row(2)
        print("row(2) =", hasil)
        self.assertEqual(hasil, [3, 4])

    def test_row_3(self):
        m = Matrix("1 2\n10 20")
        hasil = m.row(2)
        print("row(2) =", hasil)
        self.assertEqual(hasil, [10, 20])

    def test_row_4(self):
        m = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
        hasil = m.row(4)
        print("row(4) =", hasil)
        self.assertEqual(hasil, [8, 7, 6])

    def test_column_1(self):
        m = Matrix("1 2 3\n4 5 6\n7 8 9")
        hasil = m.column(3)
        print("column(3) =", hasil)
        self.assertEqual(hasil, [3, 6, 9])

    def test_column_2(self):
        m = Matrix("1 2 3 4\n5 6 7 8\n9 8 7 6")
        hasil = m.column(4)
        print("column(4) =", hasil)
        self.assertEqual(hasil, [4, 8, 6])

    def test_column_3(self):
        m = Matrix("89 1903 3\n18 3 1\n9 4 800")
        hasil = m.column(2)
        print("column(2) =", hasil)
        self.assertEqual(hasil, [1903, 3, 4])


    # Dua kasus pengujian tambahan

    def test_row_5(self):
        m = Matrix("10 20 30\n40 50 60\n70 80 90")
        hasil = m.row(3)
        print("row(3) =", hasil)
        self.assertEqual(hasil, [70, 80, 90])

    def test_column_4(self):
        m = Matrix("11 22\n33 44\n55 66")
        hasil = m.column(1)
        print("column(1) =", hasil)
        self.assertEqual(hasil, [11, 33, 55])


if _name_ == "_main_":
    unittest.main(verbosity=2)
