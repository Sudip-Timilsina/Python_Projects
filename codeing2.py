import random
print("\b\b  Welcome to Rock and PAper GAme      ")
def rock():
    object=['rock','paper','scissor']
    user_choice=input("What do u choice:Rock, Paper or scissor =").lower()
    computer_choice= random.choice(object)
    print(f"User choice:{user_choice}  Computer chocie:{computer_choice}")
    if (user_choice==computer_choice):
        print("It's a tie")
    elif (user_choice=='paper'):
        if(computer_choice=='rock'):
            print("U won")
        else:
            print("COmputer won")
    elif(user_choice=='scissor'):
        if(computer_choice=='rock'):
            print(" U won")
        else:
            print("Computer won")
    elif(user_choice=='rock'):
        if(computer_choice=='scissor'):
            print("U won")
        else:
            print("Computer won")
    a=input(" Wanna play  again, Please enter 'y'=").lower()
    if(a=='y'):
        rock()
    else:
        print( 'Thank u for playing.')


rock()

