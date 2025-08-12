str="A,B,V,C,E,R"
str2=''
for i in str:
    if i==',':
        continue
    str2=str2+i
print(str2)

