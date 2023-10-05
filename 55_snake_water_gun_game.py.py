# snake, water, gun game
import random

print("welcome to masum patel game")

for i in range(1,100):
# ----user start----#
    print("please enter a number between 1 to 3")
    print("1 for snake")
    print("2 for water")
    print("3 for gun")
    user=int(input("Enter number:-"))
# ----user end----#

# ----computer start----#
    computer=random.randint(1,3)
    print(f"computer selected number is:-{computer}")
# ----computer end----#

# ----condition start ----#
    if user==1 and computer==2:
        print("congretulation you are win")
    elif user==1 and computer==3:
        print("sorry you are loss the game") 
    elif user==1 and computer==1:
        print("match draw please try again") 
    elif user==2 and computer==2:
        print("match draw please try again")          
    elif user==2 and computer==3:
        print("sorry you are loss the game")
    elif user==2 and computer==1:
        print("sorry you are loss the game")     
    elif user==3 and computer==1:
        print("congretulation you are win")        
    elif user==3 and computer==3:
        print("match draw please try again") 
    elif user==3 and computer==2:
        print("sorry you are loss the game")     
    else:
        print("Error 404")       
    # ----condition end ----#

    i+=1