import random
options=["rock","scissors","paper"]

user_choice=input("choose rock,paper or scissors  :   ")
computer_choice=random.choice(options)

print("your choice",user_choice)
print("computer choice",computer_choice)


if user_choice==computer_choice:
    print("It is a tie")
elif user_choice=="rock" and computer_choice=="scissors":
    print("you win")
elif user_choice=="paper" and computer_choice=="rock":
    print("you win")
elif user_choice=="sccisors" and computer_choice=="paper":
    print("you win")
else:
    print("computer wins")
