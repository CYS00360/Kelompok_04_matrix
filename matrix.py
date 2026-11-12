class Matrix:
    
    def _init_(self, matrix_string):

        self.data = []

        daftar_baris = matrix_string.split("\n")

        for baris in daftar_baris:

            daftar_angka = baris.split()

            baris_angka = []

            for angka in daftar_angka:
                baris_angka.append(int(angka))
          

            self.data.append(baris_angka)
        

    
