# ========== format string ==========


# contoh generic
nama = 'Arif'
format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# angka 
angka = 1945.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)


# bilangan dengan ordo ribuan
angka = 2000
format_str = f"ribuan = {angka:,}"
print(format_str)

angka = 2000000
format_str = f"juataan = {angka:,}"
print(format_str)


# bilangan desimal
angka = 10323.231231
format_str = f"desimal = {angka:.3f}"   # menampilkan beberapa angka di belakang koma
print(format_str)

# manampilkan leading zero
angka = 10323.231231
format_str = f"desimal = {angka:010.3f}"  
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = +238.3232
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"
print(format_minus)
print(format_plus)


# mengformat persen
persentase = 0.023
format_persen = f"persen = {persentase:.1%}"
print(format_persen)


# melakukan operasi aritmatika di dalam place holder
harga = 10000
jumlah = 5
format_string = f"harga total = Rp.{harga*jumlah:,}"
print(format_string)


# format angka lain (binary, octal ,hexadecimal)

angka = 1478
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)