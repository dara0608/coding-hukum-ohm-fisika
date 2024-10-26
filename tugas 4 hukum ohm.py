def hitung_tegangan(I,R):
    V =I * R
    return V

def hitung_kuat_arus_listrik(V,R):
    if R ==0:
       return None
    I = V / R
    return I

def hitung_hambatan_listrik(V,I):
    R=V/I
    return R

def main():
    print("program untuk menghitung Hukum Ohm")
    print("1. Hitung tegangan (V)")
    print("2. Hitung kuat arus listrik (I)")
    print("3. Hitung Hambatan listrik (R)")

    pilihan = input("Masukkan pilihan 1/2/3:")

    if pilihan == "1":
        I = float(input("Masukkan nilai kuat arus listrik dalam ampere:"))
        R = float(input("Masukkan nilai Hambatan listrik dalam ohm:"))
        V = hitung_tegangan(I,R)
        print(f"Tegangan listriknya sebesar : {V: .2f} volt")

    elif pilihan == "2":
        V = float(input("Masukkan tegangan listrik dalam volt:"))
        R = float(input("Masukkan nilai hambatan listrik dalam ohm:"))
        I = hitung_kuat_arus_listrik(V,R)
        if R is None:
           print("Hambatan listrik tidak boleh nol")
        else:
            print(f"Kuat arus listriknya sebesar : {I: .2f} ampere")  

    elif pilihan == "3":
        V = float(input("Masukkan nilai tegangan listrik dalam volt:"))
        I = float(input("Masukkan nilai kuat arus listrik dalam ampere:"))
        R = hitung_hambatan_listrik(V,I)
        print(f"Hambatan listrik sebesar: {R: .2f} ohm")

    else:
        print("pilihan tidak sesuai, silakan pilih 1/2/3")

if __name__ =="__main__":
    main()
    