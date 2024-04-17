# operator dalam bentuk method

## merubah case dari string

#merubah semua ke upper case
salam = 'bro'
print('normal = ' + salam)
salam = salam.upper()
print('upper = ' + salam)

#merubah semua ke lower case
alay = 'aKu KeCe ABieezzzZZZzZZzZ'
print('normal = ' + alay)
alay = alay.lower()
print('lower = ' + alay)

# pengcekan dengan isX method

#contoh pengecekan lower case
salam = 'sist'
apakah_lower = salam.islower()   #hasilnya bool
print(salam + ' is lower = ' + str(apakah_lower))

apakah_lower = salam.isupper()   #hasilnya bool
print(salam + ' is upper = ' + str(apakah_lower))

# isalpha() <-- untuk mengecek semuanya huruf
#   ?????  |cari di internet|  ????? 

# isalnum() <-- huruf dan angka
#   ?????  |cari di internet|  ????? 

# isdecimal() <-- angka saja
#   ?????  |cari di internet|  ????? 

# isspace() <-- spasi, tab, newline, \n
#   ?????  |cari di internet|  ????? 

# istitle() <-- samua kata dimulai dengan huruf besar
judul = 'It Is Okey Not To Be Orkay'
cek_judul = judul.istitle()  # hasil bool

print(judul + ' is title = ' + str(cek_judul))

#ngecek komponen startswith() endswith() <-- keren
cek_start = 'Sangjangnim Oppa'.startswith('Sangjangnim')
print('statr = ' + str(cek_start))

cek_end = 'Sangjangnim Oppak'.endswith('Oppak')
print('end = ' + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)


gabungan = 'akuehmsayangehmkamu'
print(gabungan.split('ehm'))


## alokasi karakter rjust(). ljust() center()

kanan = 'surotong'.rjust(10)
print('"'+kanan+'"')

kiri = 'surotong'.ljust(10)
print('"'+kiri+'"')

tengah = 'surotong'.center(20,':')
print('"'+tengah+'"')

 # kebalikannya -> strip()
tengah = 'surotong'.strip(':')   # menghilangkan tanda :
print('"'+tengah+'"')
