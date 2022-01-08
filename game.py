import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
print("Welcome to the Adventure !!!")
name = input ("What's your name? ") #Storing the user's name
age = int(input("What is your age : ")) # storing the user's age

print("You are old enough to play the game.")
print("\nOK, " +  name +", let's get started.")
#Grabbing objects
sword = 0
flower = 0

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

#The story is broken into sections, starting with "intro"
def intro():
  print ("After a scary movie night out with friends, you awaken the "
  "next morning in a thick, dank, scary forest. Head spinning and " 
  "fighting the urge to vomit", 
  "unfamiliar setting. when you hear a ,"
  "different sound emitting behind you. A slobbering Monster is "
  "running towards you. You will:")
  time.sleep(1)
  print ("""  A. Grab a nearby rock and throw it at the Monster
  B. Lie down and wait 
  C. Run""")
  choice = input(" ") #Here is your first choice.
  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    print ("\nOOPS!, that was soo quick. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()

def option_rock(): 
  print ("\nThe Monster is stunned, but regains control. He begins "
  "running towards you again. Will you:")
  time.sleep(1)
  print ("""  A. Run
  B. Throw another rock
  C. Run towards a nearby cave""")
  choice = input(" ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\nYou decided to throw another rock, as if the first " 
    "rock thrown did much damage. The rock flew well over the "
    "Monsters head. You missed. \n\nYou died!")
  elif choice in answer_C:
    option_cave()
  else:
    print (required)
    option_rock()

def option_cave():
  print ("\nYou were hesitant, since the cave was dark and "
  "ominous. Before you fully enter, you notice a shiny sword on "
  "the ground. Do you pick up a sword. Y/N?")
  choice = input(" ")
  if choice in yes:
    sword = 1 #adds a sword
  else:
    sword = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  A. Hide in silence
  B. Fight
  C. Run""")
  choice = input(" ")
  if choice in answer_A:
    print ("\nReally? You're going to hide in the dark? I think "
    "Monsters can see very well in the dark, right? Not sure, but "
    "I'm going with YES, so...\n\nYou died!")
  elif choice in answer_B:
   if sword > 0:
    print ("\nYou laid in wait. The shimmering sword attracted "
    "the Monster, which thought you were no match. As he walked "
    "closer and closer, your heart beat rapidly. As the Monster "
    "reached out to grab the sword, you pierced the blade into "
    "its chest. \n\nYou survived!")
   else: #If the user didn't grab the sword
     print ("\nYou should have picked up that sword. You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_C:
    print ("As the Monster enters the dark cave, you sliently "
    "sneak out. You're several feet away, but the orc turns "
    "around and sees you running.")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  print ("\nYou run as quickly as possible, but the Monster's "
  "speed is too great. You will:")
  time.sleep(1)
  print ("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""")
  choice = input(" ")
  if choice in answer_A:
    print ("You're easily spotted. "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nYou're no match for the Monster. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_town()
  else:
    print (required)
    option_run()
    
def option_town():
  print ("\nWhile frantically running, you notice a rusted "
  "sword lying in the mud. You quickly reach down and grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a delapitated building, waiting for the Monster to come "
  "charging around the corner. You notice a purple flower "
  "near your foot. Do you pick it up? Y/N")
  choice = input(" ")
  if choice in yes:
    flower = 1 #adds a flower
  else:
    flower = 0
  print ("You hear its heavy footsteps and ready yourself for "
  "the impending Monster.")
  time.sleep(1)
  if flower > 0:
    print ("\nYou quickly hold out the purple flower, somehow "
    "hoping it will stop the Monster. It does! The Monster was looking "
    "for love. "
    "\n\nThis got weird, but you survived!")
  else: #If the user didn't grab the sword
     print ("\nMaybe you should have picked up the flower. "
     "\n\nYou died!")

intro()