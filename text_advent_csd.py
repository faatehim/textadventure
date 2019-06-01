import time # importing module to add a pause

#Figuring out how the users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes", "Yes", "YES", "yES", "YEs", "YeS"]
no = ["N", "n", "no", "No", "NO"]

required = ("\nYou can only choose option A, B, or C\n") # Cutting down on duplication
required2 = ("\nYou can only choose option A or B\n")

print("""Welcome to the home of Usayd Ahmed Sheikh. Thank you for visiting. You won't regret it.\n\n""")



def intro():
    choice = input("Would you like to explore Usayd's home?\n >>> ")
    time.sleep(1) #this just means you are including a pause
    print("\n")
    if choice in yes: #see arrays above
        print("Let's go\n")
    elif choice in no:
        print ("\n Your loss.")
        raise SystemExit #This will exit the program and bring you back to command line

def learn_more():
  print ("""You have entered Usayd's home. Would you like to... """)
  time.sleep(1)
  choice2 = input("""
    Would you like to?
    
    A. Go up the stairs
    B. Go into the living room \n
    >>> """)
  print("\n")
  if choice2 in answer_A:
        choice2aa = input("\nYou see a room with an image of a McDonnell Douglas F-15 Eagle opposing it. That must be Usayd's room. Do you go in? \n >>> ")
        if choice2aa in yes:
            time.sleep(1)
            choice2ab = input("\nYou immediately see desk with a computer open with a big file called homework. There is no way that actually contains homework. Do you open it? \n >>> ")
            if choice2ab in yes:
                print("Wow. It actually contains homework. The good stuff must be else where.")
                time.sleep(4)
                print("You look around his room and notice that there is a small table full of various medicines, dressings, and bandages. Is Usayd fine? You are getting quite concerned. Anyway you keep wandering around.")
                time.sleep(6)
                choice2ac = input("You decide to open his closet and are astonished. You see MO ZAIDI!!??? He is handcuffed and bond to the wall with his mouth sealed with duck tape. He is squealing for help. Do you help him? \n >>>  ")
                time.sleep(1)
                if choice2ac in yes:
                    time.sleep(1)
                    print("You gotta look for a key to free Mo so you can get him out of there \n")
                    time.sleep(2)
                    print("You check under his bed. Nothing except a bunch of magazines.\n")
                    time.sleep(2)
                    print("You check in his desk compartments. Nothing except for a bunch of bad math grades. He must be hiding them from his parents.\n")
                    time.sleep(2)
                    print("You open his bottle of Tylenol and look in there. There it is!\n")
                    time.sleep(2)
                    print("You unlock the handcuffs and Mo comes out. His mouth is still sealed. You gotta run away.\n")
                    time.sleep(2)
                    print("But at the last second, you hear Usayd coming upstairs. What do you do?\n")
                    time.sleep(1)
                    choice2ad = input("""
                    A. Confront Usayd
                    B. Try to hide
                    C. Try to jump out the window
                    \n >>>  """)
                    if choice2ad in answer_A:
                        time.sleep(1)
                        print(" 'Yo Usayd. What's up with this?' \n")
                        time.sleep(1)
                        print("Usayd pulls out his airsoft gun and shoots you in the head. You have died\n")
                        raise SystemExit
                    if choice2ad in answer_B:
                        time.sleep(1)
                        print("You hide with Mo in the closet and stay dead silent\n")
                        time.sleep(1)
                        print("You see through the small peephole that Usayd has walked by the room.\n")
                        time.sleep(1)
                        print("You and Mo run as fast as you can down the stairs and out the house. Congratulations!")
                        raise SystemExit
                    if choice2ad in answer_C:
                        time.sleep(1)
                        print("You open the door and jump out. Unfortunetly, it is quite a height. You both die immediately on impact.")
                        raise SystemExit
        if choice2aa in no:
            learn_more()
  elif choice2 in answer_B:
        print("You see 13 boxes of various assortments of cereal brands\n")
        time.sleep(1)
        print("Does this kid only eat cereal?\n")
        time.sleep(0.5)
        print("Looking ahead, you see Usayd's two sisters busy watching a 10 hour compilation of Peppa Pig on their TV?\n")
        time.sleep(3)
        print("Is this all kids watch these days?\n")
        time.sleep(0.5) 
        choice2ba = input("Do you take the remote and turn it off? \n >>> ")
        if choice2ba in yes:
            time.sleep(0.5)
            print("You turn off the TV. The two look at you and start crying. Usayd's dad and mom - Rizwan and Ayesha run into the room. You are busted.")
            raise SystemExit
        if choice2ba in no:
            time.sleep(0.5)
            choice2bb = input("You sneak past them. You look outside and see Usayd on top of his playground pointing an airsoft gun at a can on top of his fence. Do you say something? \n >>> ")
            if choice2bb in yes:
                time.sleep(1)
                print("Usayd has seen you. He point his airsoft at you and shoots. You are dead.")
                raise SystemExit
            if choice2bb in no:
                time.sleep(0.5)
                choice2bc = input("You keep going and open a closet. And you see JAY KATYAN???????? He is handcuffed to the wall with his mouth sealed. He is squealing for help. Do you help him?")
                if choice2bc in yes:
                        time.sleep(0.5)
                        print("You gotta look for a key to free Jay so you can get him out of there\n")
                        time.sleep(2)
                        print("You check in the bathroom. Nothing.\n")
                        time.sleep(1)
                        print("You check in the closet hanger. Still nothing.\n")
                        time.sleep(1)
                        print("You check in Usayd's trenchcoat. You found it!\n")
                        time.sleep (1)
                        print("You unlock the handcuffs and Jay comes out. His mouth is still sealed. You gotta run away.\n")
                        time.sleep(3)
                        print("But at the last second, you hear Usayd coming downstairs. What do you do?\n")
                        time.sleep(1)
                        choice2bd = input("""
                        A. Confront Usayd
                        B. Try to hide
                        C. Run out the door.
                        \n >>> """)
                        if choice2bd in answer_A:
                            time.sleep(0.5)
                            print(" 'Yo Usayd. What's up with this?' \n")
                            time.sleep(1)
                            print("Usayd pulls out his airsoft gun and shoots you in the head. You have died")
                            time.sleep(2)
                            raise SystemExit
                        if choice2bd in answer_B:
                            time.sleep(1)
                            print("You hide with Jay in the closet and stay dead silent\n")
                            time.sleep(1)
                            print("You see through the small peephole that Usayd has turned on his PS4. \n")
                            time.sleep(3)
                            print("You and Jay run as fast as you can down the stairs and out the house. Congratulations!")
                            time.sleep(3)
                            raise SystemExit
                        if choice2bd in answer_C:
                            print("You open the door and run out. Congratulations!")
                            raise SystemExit
        
  else:
        print(required)
        time.sleep(0.5)
        learn_more()

intro()
learn_more()

