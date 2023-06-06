import random
survived = True
points = 0
def introduction():
  print("You are poor. Your betroved has left you. Life is looking grim.")
  print("You hear that there is a dungeon nearby that promises gold to those who conquer it.")
  print("You know there is a slim chance that you will make it out alive, but you enter anyway because you dont care.")
  print("You enter the dungeon with a zeal to get rich.")
introduction()


import pickle
from os import path
def save(points, file):
  with open(file, "wb") as f:
    pickle.dump(points, f)
def load(file):
  if path.exists(file):
    with open(file, "rb") as f:
      return pickle.load(f)
    return None
introduction()

def left():
  print("You can move left")
def right():
  print("You can move right")
def straight():
  print("You can move straight")

print("")

def monster():
  global points
  global survived
  chance_of_monster = random.randint(1,4)
  monster_attack_prob = random.randint(1,2)
  if chance_of_monster == 1:
    print("You encounter a monster.")
    if monster_attack_prob == 1:
      print("It attacks you")
      if random.randint(1,2) == 1:
        print("You die")
        survived = False#-- MODIFY THIS CODE SO THAT THE CODE ENDS WHEN YOU DIE
      else:
        print("You boxed the monster up and survived.")
        points += 1
        survived = True
    elif monster_attack_prob == 2:
      print("The monster is peaceful.")
      points += 1
      survived = True
  elif chance_of_monster == 2:
    print("You find nothing")
    points += 1
    survived = True
  elif chance_of_monster == 3 or chance_of_monster == 4:
    print("You enter an obstacle course.")
    if monster_attack_prob == 1:
      print("You failed the obstacle course and died.")
      survived = False
    elif monster_attack_prob == 2:
      print("You successfuly completed the course.")
      points += 1
      survived = True

def randomization():
  global survived
  stored = []
  if random.randint(1,2) == 2:
    left()
    l = "left"
    stored.append(l)
  if random.randint(1,2) == 2:
    right()
    r = "right"
    stored.append(r)
  if random.randint(1,2) == 2:
    straight()
    s = "straight"
    stored.append(s)
  elif stored == []:
    straight()
    left()
    right()
  answer = input("Which direction would you like to go? ")
  if answer in stored:
    print ("You move " + answer)
  elif stored == []:
    print("You entered a dead end and died from suffocation")
    survived = False
  elif answer not in stored and stored != []:
    print("That was not an option. Due to your stupidity, you ran into a wall and died.")
    survived = False
    return survived
  
def left():
   print("You can move left")
def right():
   print("You can move right")
def straight():
   print("You can move straight")

print("")
def monster():
  global survived
  global points
  survived = True
  chance_of_monster = random.randint(1,4)
  monster_attack_prob = random.randint(1,2)
  if chance_of_monster == 1:
    print("You encounter a monster.")
    if monster_attack_prob == 1:
      print("It attacks you")
      if random.randint(1,2) == 1:
        print("You die")
        survived = False#-- MODIFY THIS CODE SO THAT THE CODE ENDS WHEN YOU DIE
      else:
        print("You boxed the monster up and survived.")
        points += 1
        survived = True
    elif monster_attack_prob == 2:
      print("The monster is peaceful.")
      points += 1
      survived = True
  elif chance_of_monster == 2:
    print("You find nothing")
    points += 1
    survived = True
  elif chance_of_monster == 3 or chance_of_monster == 4:
    print("You enter an obstacle course.")
    if monster_attack_prob == 1:
      print("You failed the obstacle course and died.")
      survived = False
    elif monster_attack_prob == 2:
      print("You successfuly completed the course.")
      points += 1
      survived = True

def randomization():
  
  global survived
  stored = []
  if random.randint(1,2) == 2:
    left()
    l = "left"
    stored.append(l)
  if random.randint(1,2) == 2:
    right()
    r = "right"
    stored.append(r)
  if random.randint(1,2) == 2:
    straight()
    s = "straight"
    stored.append(s)
  elif stored == []:
    straight()
    left()
    right()
  answer = input("Which direction would you like to go? ")
  if answer in stored:
    print ("You move " + answer)
  elif answer not in stored and stored != []:
    print("That was not an option. Due to your stupidity, you ran into a wall and died.")
    survived = False
    return survived

total_points = 0
total_points += points 
print("Points: " + str(total_points))
print(" --")
print(" -")

while survived:
  randomization()
  monster()
  print(" --")
  print(" -")

print("Rooms survived: " + str(points))
while survived:
  randomization()
  print("Rooms survived: " + str(points))
  print(" ")
  print()

else:
  print("Your failed life flashes before your eyes . . . ")
  print("You died")
  print("ಥ_ಥ")
  save(total_points, "high_scores.pkl")
  print("Your high score is: ")
  if "high_scores.pkl" == None:
    print("N/A")
  else:
    load(max("high_scores.pkl"))
while survived:
  randomization()
  monster()
  print(" --")
  print(" -")

print("Rooms survived: " + str(points))
while survived:
  randomization()
  print("Rooms survived: " + str(points))
  print(" ")
  print()
else:
  print("Your failed life flashes before your eyes . . . ")
  print("You died")
  print("ಥ_ಥ")