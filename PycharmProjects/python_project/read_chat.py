#import statements
from globals import friends
from select_friend import select_friend
from termcolor import colored

# function to read the chat history of friends
def read_chat():
    #read_for stores the value returned by select_a_friend()
    read_for = select_friend()

    print '\n'
    #iterating through friends chats list
    for chat in friends[read_for].chats:
        if chat.sent_by_me:#when True
            # The date and time is printed in blue
            print(colored(str(chat.time.strftime("%d %B %Y %A %H:%M")) + ",", 'magenta')),
            # The message is printed in red
            print(colored("You said:", 'yellow')),
            # black is by default
            print str(chat.message)
        else:#when False
            # The date and time is printed in blue
            print(colored(str(chat.time.strftime("%d %B %Y %A %H:%M")) + ",", 'magenta')),
            # The message is printed in red
            print(colored(str(friends[read_for].name) + " said:", 'yellow')),
            # Black color is by default
            print str(chat.message)