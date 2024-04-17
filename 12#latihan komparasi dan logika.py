#latihan logika dan komparasi

#membuat gabungan area rentang dari angka

inputUser = float(input("masukkan angka yang bernilai\nkurang dari 3\natau \nlebih besar dari 10:"))

#+++++++3-----------10++++++++

#+++++++3-------
#memriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang Dari 3 =",isKurangDari)

#------------10++++++++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih Dari 10 =",isLebihDari)

#+++++++3-----------10++++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukka: ",isCorrect)


# ------3+++++++++10----------
# kasus irisan
print("\n",10*"=","\n")
inputUser = float(input("masukkan angka yang bernilai\nlebih dari 3\natau \nkurang dari 10:"))


#----------3+++++++++
#lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 =",isLebihDari)

# +++++++++++10---------
#kurang dari 10
isKurangDari = inputUser < 10
print("kurang dari 10 =",isKurangDari)


# ------3+++++++++10----------
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukka: ",isCorrect)
