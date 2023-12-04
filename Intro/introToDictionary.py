rdictionary = {
    "fruit" : "apple",
    22 : "popcorn",
    99.99 : 77
    }

rdictionary["newkey"] = "newvalue"
print(rdictionary["newkey"])

rdictionary["fruit"] = "banana"
print(rdictionary["fruit"])

del rdictionary[22]
print(rdictionary)

for k in rdictionary:
    print(f"key: {k} -> value:{rdictionary[k]}")

#CRUD --> Create, Read(print), Update, Delete