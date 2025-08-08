#list

cities=["chennai","madurai","trichy","coimbatore","salem"]
val=[3,5,6,3,2,9]
list1=["chennai",3,"salem"]

#accessing list with indexing

print(cities[0])
print(val[2])
print(cities[:3])
print(cities[-2])
print(cities[::2])
print(val)

#modify

cities[2]="trichy"
print(cities)

#append

cities.append("karur")
print(cities)

#insert

cities.insert(3,"thanjavur")
print(cities)

#removing using del

del cities[3]
print(cities)

#removing using pop()

cities.pop(2)
print(cities)

#remove by value

city_del="coimbatore"
cities.remove(city_del)
print(cities)

#permanent sort

cities.sort()
print(cities)

#temporary sort

print(sorted(cities))
print(sorted(val))
print(cities)

#reverse

cities.reverse()
print(cities)

#length of a list

print(len(cities))
