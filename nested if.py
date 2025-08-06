num=int(input("enter a num: "))
if num > 99 and num < 1000:
    if num % 2 == 0:
        print(str(num) + "is a three digit even number")
else:
    print(str(num) + "is not a three digit even number")


name="Sathya"
if name[0] == 'S' or name[0] == 's':
    print("the name starts with S")
