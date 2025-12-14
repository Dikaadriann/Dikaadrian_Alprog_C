# komparasi (true false)
# > < >= <= == != is is-not
x = 25
y = 73

print ("========== lebih dari (>)")
hasil = x > 73
print (x, ">" , 73, "=", hasil)
hasil = x > 15
print (x, ">" , 15, "=", hasil)


print ("========== kurang dari (<)")
hasil = y < 25
print (y, "<", 25, "=", hasil)
hasil = y <  78
print (y, "<", 78, "=", hasil)


print ("========== lebih dari sama dengan (>=)")
hasil = x >= 73
print (x, ">=", 73, "=", hasil)
  
  
print ("========== kurang dari sama dengan (<=)")
hasil = y <= 25
print(y, "<=", 25, "=", hasil)

print ("========= sama dangan sama dengan (==)")
hasil = x == 73
print (x, "==", 73, "=", hasil)

print ("========== tidak sama dengan (!=)")
hasil = y != 25
print(y, "!=", 25, "=", hasil)

print ("========== is (is)")
hasil = x is 73
print(x, "is", 73, "=", hasil)

print ("========== is-not (is not)")
hasil = 25 is not y
print(25, "is-not", y, "is not", hasil)

