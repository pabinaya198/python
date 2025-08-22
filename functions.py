print("hello")

def greet():
    print("hello")
    print("********")
    print("how are you")
greet()
greet()

def greet(name):
    print("hello" + name)
    print("how are you?")
greet("ram")
print("********")
greet("hari")

name="ram"
greet(name)#passing
print("********")
name="ganesh"
greet(name)

def greet(fname,lname):
    print("hello" + fname + "" + lname)
    print("how are you?")

n="ram"
greet(fname="ram",lname="kumar")
print("********")
name="ganesh"
greet("logic","first")

def sum(num):
    sum_result=num*(num+1)/2
    return(sum_result)
    result=sum(11)
    print(result)
    print(sum(20))
