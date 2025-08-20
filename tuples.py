tup=(2,3,4)
print(tup)

tup=(3,5,6)
print(tup)

print(tup[1])

tup=(tup.index(6))

tup=(3,4,5,4,4)
print(tup.count(4))

for i in tup:
    print(i)

if 3 in tup:
    print('yes')

if 3 not in tup:
    print('no')
if tup:
    print('tup is not empty')
