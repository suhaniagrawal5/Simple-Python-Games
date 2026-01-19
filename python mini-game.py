
print("welcome to treasure island.your mission is to find the treasure")
value=input("enter 0 for moving left or enter 1 for moving right")

if value==1:
    print("fall into a hole")
else:
     swim=input("enter 1 for swim and 0 for wait")
if swim==1:
        print("attacked by a beast")
else:
        door=input("enter to colour to move into a door(red,blue,yellow)")
        if door=="blue":
         print("eaten by beasts")
        elif door=="red":
         print("burned by fire")
        elif door=="yellow":
           print("congrats!,you win")
        else:
            print("invalid")
    