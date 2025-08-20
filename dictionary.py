user={'name':'ram','age':25,'gender':'male'}
print(user['gender'])
print(user)

#Add a new key value pair

user['city']='chennai'
print(user)

#modify

user['age']=26
print(user)

#delete

del user['gender']
print(user)

#looping

for keys,val in user.items():
    print("keys : " + keys)
    print("val : " + str(val))

for key in user.keys():
    print(keys)

for key in sorted(user.keys()):
    print(user[keys])

job={'priya':'cts','john':'amazon','vidhya':'cts'}
for company in job.values():
    print(company)

#list of dictionaries

users=[]
user={'name':'ram','age':25,'gender':'male'}
users.append(user)
user={'name':'ramya','age':26,'gender':'female'}
user.append(user)
print(users[1]['name'])

#list in dictionary

user['fav_food']=['poori','pizza','pasta']
print(user['fav_food'][0])
