name=input(" what's your name: ")
print(" Hello " + name)
height=int(input(" what's your height: "))
print(" you are " + str(height/2.54) + " inches tall ")

height_inches="{:.2f}".format(height/2.54)
print(" you are " + height_inches + " inches tall ")
