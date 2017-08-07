print "Let's play game..!"

print "The Game is about you have to guess a random number which is choosen by the computer... "

Temp=raw_input("To start the game write start or if you want to exit the game write exit..\n")
Temp=Temp.lower()
if(Temp=="exit"):
    print "Thank you for playing the game"
elif(Temp=="start"):

    num=int(raw_input("Enter you no."))
    computer_no=5

    if(num<computer_no):
         print "oops you gussed the number too low.."
    elif(num==computer_no):
        print "congratulations you got it right.."
    elif(num>computer_no):
         print "oops you gusses the number too high"


