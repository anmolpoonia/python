name  = "john"
surname = 'wick'
print("hello" + " " + name)

print(name[0])
print(name[1])
print(name[2])
print(name[3])

print(surname[0])
print(surname[1])
print(surname[2])
print(surname[3])
print('use of for loop')
for i in name:
    print(i)

for i in surname:
    print(i)

print("he said, \"i want to eat an apple.\"")
ab = '''hsdffhjsfgnxfhm
hhfhfh
adhfggnfxhhj
dfstnfsgnfsgf
fsthhfsgsgn'''

print(ab)

#string slicing

naam= "clair,eclairs"
print(len(naam))
print(naam[0:8])
print(naam[1:8])
print(naam[:])
print(naam[0:-3])
print(naam[0:8])
print(naam[-3:-1])


nm='HaRry!!!!!'
print(nm[-4:-2])

print(nm.upper())
print(nm.lower())
print(nm.rstrip("!"))
print(nm.replace("HaRry","John"))
print(nm.split("r"))
print(nm.capitalize())


mm= "welcome yo the ost boring university daiict"
print(mm.capitalize())
print(len(mm))
print(mm.center(150))
print(len(mm.center(150)))
print(mm.count("r"))
print(mm.endswith("t"))

nn= "indian criket team will loose the world cup final and thats for sure and no chace they will win"
print(nn.find("and"))
print(nn.isalnum())
print(nn.swapcase())
print(nn.istitle())