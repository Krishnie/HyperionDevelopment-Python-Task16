# This program creates an sms simulator
# First it creates a class called SMSMessage
# It then defines  parameters (self, messageText,fromNumber) in a constructor
# It then assigns attributes to the parameters
# Within the class it creates a method called MarkAsRead which changes hasBeenRead to true
# Outside the class it initialises the SMSStore to empty
# The next method addSMS adds an instance of SMSMessage to SMSStore
# GetCount returns how many sms's messages were sent
# GetMessage changes the status of hasBeenRead from unread to read and returns the ith element messageText  from SMSstore
# GetUnread methods checks which messages are unread and adds them to a list called URlist
# The remove method removes ith item from the SMSStore
# The  while  loops runs until the userChoice is equal to quit
# The first if statement checks that if the userChoice is equal to "read" and outputs the getMessage method
# The second  statement checks that if the userChoice is equal to "send" and uses the addSMS to add the instance of SMSMessage to SMSStore
# The third logic statement checks that if the userChoice is equal to quit then prints a message saying "Goodbye" is outputted
# Otherwise it just says ("Oops - incorrect input")



class SMSMessage(): # Create class
    ''' This class represents a sms message. '''
    def __init__(self, messageText, fromNumber): # constructor with paramaters
        self.fromNumber = fromNumber  # Assign attributes
        self.messageText = messageText
        self.hasBeenRead = False 

    def MarkAsRead(self): 
        ''' This method turns a has been read to from true to false.'''
        self.hasBeenRead = True
        
SMSStore = [] # Initialise 
def add_SMS(SMSStore,messageText,fromNumber):
    ''' This method adds  adds an instance of SMSMessage to the list called SMSStore.'''
    SMSStore.append(SMSMessage(messageText,fromNumber))
   
def get_count(SMSStore): 
    ''' This method returns the length of the SMSStore. '''

    return len(SMSStore)

def get_message(SMSStore,i): 
    ''' GetMessage changes the status of hasBeenRead from unread to read and returns the ith element messageText  from SMSStore.'''
    SMSStore[i].MarkAsRead() 
    return SMSStore[i].messageText 

def get_unread_message(SMSStore): 
    ''' GetUnread methods checks which messages are unread and adds them to a list called URlist.'''
    URList=[]
    for sms in SMSStore:
        if sms.hasBeenRead==False:
            URList.append(sms)


def remove(SMSStore,i): 
    ''' The remove method removes ith item from the SMSStore.'''
    return SMSStore.pop(i)
    

userChoice = "" #  initialise 

# Logic Conditions
while userChoice != "quit":
    userChoice = input("What would you like to do - read/send/quit? ").lower()
    if userChoice == "read":
        userChoice1 = int(input('Please input the index of the message you would like to read  '))
        print(get_message(SMSStore,userChoice1-1)) 
    elif userChoice == "send":
        userChoice2 = input('Please input the text of the message  ')
        userChoice3 = int(input('Please input the number of the recipient  '))
        add_SMS(SMSStore,userChoice2,userChoice3)
        print(f' This is the message : " {SMSStore[-1].messageText}" received from {SMSStore[-1].fromNumber}')
    elif userChoice == "quit":
        print ("Goodbye")
    else:
        print ("Oops - incorrect input")


