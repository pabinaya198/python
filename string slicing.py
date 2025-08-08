#string slicing

name="logic first"

#using indexing

print(name[3])
print(name[0:4])
print(name[:4])
print(name[2:4])
print(name[2:])
print(name[2:10:2])
print(name[-2])
print(name[-5:-2])
print(name[-2:-5:-1])
print(name[::-1])
print(name[:-3:-1])
print(name[2:-2])

#using slice method

x=slice(2,-2)
print(name[x])




