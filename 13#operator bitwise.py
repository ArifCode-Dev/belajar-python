# episode operator bitwise, operasi biner, binary

a = 9
b = 5

# bitwise OR {|}
c = a | b
print("\n===========OR============\n")
print("nilai :",a,",binary :",format(a,"08b"))
print("nilai :",b,",binary :",format(b,"08b"))
print("-------------------------------{|}")
print("nilai :",c,",binary :",format(c,"08b"))

# bitwise AND {&}
c = a & b
print("\n===========AND============\n")
print("nilai :",a,",binary :",format(a,"08b"))
print("nilai :",b,",binary :",format(b,"08b"))
print("-------------------------------{|}")
print("nilai :",c,",binary :",format(c,"08b"))

#bitwise XOR {^}
c = a ^ b
print("\n===========XOR============\n")
print("nilai :",a,",binary :",format(a,"08b"))
print("nilai :",b,",binary :",format(b,"08b"))
print("-------------------------------{|}")
print("nilai :",c,",binary :",format(c,"08b"))

#bitwise NOT {~}
c = ~a
print("\n===========NOT============\n")
print("nilai :",a,",binary :",format(a,"08b"))
print("-------------------------------{~}")
print("nilai :",c,",binary :",format(c,"08b"))
print("-------------------------------{^}")
d = 0b00001001
e = 0b11111111
print("nilai :",e^d," ,binary :",format(e^d,"08b"))

##shifting

#shift right(>>)
c = a >> 2
print("\n===========>>============\n")
print("nilai :",a,",binary :",format(a,"08b"))
print("-------------------------------{>>}")
print("nilai :",c,",binary :",format(c,"08b"))

#shift left(<<)
c = a << 2
print("\n===========<<============\n")
print("nilai :",a,",binary :",format(a,"08b"))
print("-------------------------------{<<}")
print("nilai :",c,",binary :",format(c,"08b"))