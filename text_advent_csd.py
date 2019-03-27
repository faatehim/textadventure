import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
key = 0
flashlight = 0

required = ("\nYou can only choose option A, B, or C\n") #Cutting down on duplication
required2 = ("\nYou can only choose option A or B\n")

print("""Welcome to the town of Hillers Hollow. Life can be
a bit strange here; many of us have come to accept our town's
'eccentricities' without a second thought...what will you
think?\n\n""")


#The story is broken into sections, starting with "intro"
#When you see def name() it means you are defining a function which you will later call
def intro():
    choice = input("Would you like to find out more about the dark past of Hillers Hollow?\n >>> ")
    time.sleep(1) #this just means you are including a pause
    print("\n")
    if choice in yes: #see arrays above
        print("Perhaps a visit to the Hillers Hollow Historical Society is in order.\n")
    elif choice in no:
        print ("\nGo on living with your head under a rock. "
        "\n\nBut don't come crying to me when darkness finds you.")
        raise SystemExit #This will exit the program and bring you back to command line

def learn_more():
  print ("""The preservationist at the historical society tells you
they take appointments for those researching the town's history
and artifacts. Do you: """)
  time.sleep(1)
  choice2 = input("""
    A. Make an appointment
    B. Cut your losses and move on
    C. Decide this isn't worth your time\n
    >>> """)
  print("\n")
  if choice2 in answer_A:
        print("We will see you tomorrow at noon.")
  elif choice2 in answer_B:
        print("The town libary might have some clues...\n")
        raise SystemExit
  elif choice2 in answer_C:
        print ("\nGo on living with your head under a rock. "
        "\n\nBut don't come crying to me when darkness finds you.\n")
        raise SystemExit
  else:
        print(required)
        time.sleep(0.5)
        learn_more()
    #option_rock()

def appointment():
    print("""  \nThe next day, the head archivist greets you: Thank you for coming to visit us at
the Historical Society again today. What is it you are researching?""")
    time.sleep(1)
    choice3 = input("""
    A. Mysterious disappearences of town residents from the 1980s
    B. The mill fire of 1973
    C. Extraterrestrial life-forms spotted in Hillers Hollow in the past decade\n
    >>> """)
    print("\n")
    if choice3 in answer_A:
          print("The archivist says to you: You're delusional and wasting our time.\n")
          time.sleep(0.5)
          print("""Feeling somewhat offended, you gather your things and start heading towards
the door, weaving your way through shelves and cases of town artifacts.\n""")
          key()
    elif choice3 in answer_B:
          print("""An unfortunate accident that left many jobless, and some homeless.
Nothing left to be said.\n""")
          raise SystemExit
    elif choice3 in answer_C:
          print("You're delusional and wasting our time.\n")
          time.sleep(1)
          terrestrial()
          raise SystemExit
    else:
          print(required)
          time.sleep(1)
          appointment()

def key():
    print("Pssssst...\n")
    time.sleep(0.75)
    print("As you are leaving, you hear someone whispering to get your attention.\n")
    time.sleep(0.75)
    print("""You turn around and find a mousy looking woman with oversized spectacles
staring back at you.\n""")
    time.sleep(0.75)
    print("What is it?, you ask.\n")
    time.sleep(0.75)
    print("""The woman tells you that you're not delusional and quickly presses
a tarnished key into your hand, before scurrying away
at the sound of approaching footsteps.\n""")
    choice4 = input("""Do you leave the key at the historical society, or do you put it in your pocket?\n
    A. Leave the key; this is more annoying than it's worth
    B. Quickly put the key in your pocket, and prepare to face
    the approaching footsteps\n
    >>> """)
    print("\n")
    if choice4 in answer_A:
        print("You're pretty lazy. Are you sure you have what it takes to live in this town?\n")
        raise SystemExit
    elif choice4 in answer_B:
        print("Smart move, that key is going to become very important.\n")
    else:
          print(required2)
          key()

def coffeeshop():
    print("""Those approaching footsteps were from the stern archivist you had
your appointment with. She rudely reminded you that you were no longer
welcome at the historical society. After giving her a snarky reply, you
made your way to a nearby coffee shop where you are sitting now, comtemplating
what to do next.\n""")
    time.sleep(0.75)
    print("""As you sip your regrettably weak coffee (what is with this town?),
you notice an older gentleman staring at you from across the cafe.
Feeling slightly creeped out, you settle up your bill and begin
gathering your things.\n""")
    time.sleep(0.75)
    print("""You begin to make your way towards the door, and the man gets up
and follows you. This day just keeps getting weirder and weirder.\n""")
    time.sleep(0.75)
    print("""Self-consciously, you put your hand in your pocket, as he approaches,
making sure the key you were given is still there.\n""")
    time.sleep(0.75)
    print("""Do I know you?, you ask the strange man.\n""")
    time.sleep(0.75)
    print("""No, he says, but I have a message for you: The number etched on that key
is a clue.\n""")

def keyclue ():
    print("""The number etched on the key is 13, in what appears to be
    an old-fashioned font.""")

def terrestrial():
    print("""Are you really a person who believes in extraterrestrial life
forms? If so, this is not the adventure for you. This is Hillers Hollow
after all, not Roswell, New Mexico. Just saying.\n""")

#This is where you call all the functions so they run
intro()
learn_more()
appointment()
coffeeshop()
