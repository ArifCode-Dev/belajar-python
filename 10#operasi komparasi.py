#operasi komparasi

#setiap hasil dari operasi komparasi adalah boolean 

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

#lebih besar dari >
print('=====Lebih Besar Dari (>)=====')
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = a > 2
print(a,'>',2,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

#kurang dari <
print('=====Kurang Dari (<)=====')
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = a < 2
print(a,'<',2,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

#lebih dari sama dengan >=
print('===== lebih dari sama dengan (>=)=====')
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = a >= 2
print(a,'>=',2,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

#kurang dari sama dengan <=
print('=====Kurang Dari sama dengan (<=)=====')
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = a <= 2
print(a,'<=',2,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

#sama dengan (==)
print('=====sama dengan(==)=====')
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

#tidak sama dengan (!=)
print('==========tidak sama dengan(!=)=====')
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

#'is' sebagai komperasi object indentity
print("==========is==========")
x = 5 #ini adalah assigment membuat object
y = 5
print('nilai x =,',x,',id = ',hex(id(x)))
print('nilai x =,',y,',id = ',hex(id(y)))
hasil = x is 5
print('x is 5 =',hasil)

x = 5
y = 6
print('nilai x =,',x,',id = ',hex(id(x)))
print('nilai x =,',y,',id = ',hex(id(y)))
hasil = x is not 6
print('x is not 6 =',hasil)
