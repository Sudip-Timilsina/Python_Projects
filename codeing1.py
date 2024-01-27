import random
def number(x):
    random_nunber = random.randint(1,x)
    a=0
    b=10
    while a<10:
        guess = int(input(f"Enter a number between (1) to {x}"))
        if(guess<random_nunber):
            print("Sorry wrong guess. Try agaim with bigger numbers")

        elif(guess>random_nunber):
            print("Sorry wrong guess.Try again with smaller numbers")

        else:
            print("U got the number. Congratulation!")
            break

        a=a+1
        print(f"U have got {b-1} chances")
        b=b-1
number(100)