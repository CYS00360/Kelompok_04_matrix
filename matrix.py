class Matrix:
    
    def __init__(self, matrix_string):

        self.data = []

        daftar_baris = matrix_string.split("\n")

        for baris in daftar_baris:

            daftar_angka = baris.split(' ')

            baris_angka = []

            for angka in daftar_angka:
                baris_angka.append(int(angka))
          

            self.data.append(baris_angka)
            
    def row(self, index):
        return self.data[index - 1]
   
    def column(self, index):

        hasil = []

        for baris in self.data:
            hasil.append(baris[index - 1])

        return hasil

    
