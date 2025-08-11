import random
num=random.randint(1,20)
guess=int(input("can you guess the number I am thinking? Its less than 20"))
while num!=guess:
    if guess>num:
        print("your guess in higher")
    else:
        print("your guess in lower")
        guess=int(input("guess again:"))
        print("you won!")
