import random
# survived = True
# points = 0
def introduction():
  print("You are poor. Your betroved has left you. Life is looking grim.")
  print("You hear that there is a dungeon nearby that promises gold to those who conquer it.")
  print("You know there is a slim chance that you will make it out alive, but you enter anyway because you dont care.")
  print("You enter the dungeon with a zeal to get rich.")

# introduction()



# def left():
#   print("You can move left")
# def right():
#   print("You can move right")
# def straight():
#   print("You can move straight")

# print("")

# def monster():
#   global survived
#   global points
#   survived = True
#   chance_of_monster = random.randint(1,4)
#   monster_attack_prob = random.randint(1,2)
#   if chance_of_monster == 1:
#     print("You encounter a monster.")
#     if monster_attack_prob == 1:
#       print("It attacks you")
#       if random.randint(1,2) == 1:
#         print("You die")
#         survived = False#-- MODIFY THIS CODE SO THAT THE CODE ENDS WHEN YOU DIE
#       else:
#         print("You boxed the monster up and survived.")
#         points += 1
#         survived = True
#     elif monster_attack_prob == 2:
#       print("The monster is peaceful.")
#       points += 1
#       survived = True
#   elif chance_of_monster == 2:
#     print("You find nothing")
#     points += 1
#     survived = True
#   elif chance_of_monster == 3 or chance_of_monster == 4:
#     print("You enter an obstacle course.")
#     if monster_attack_prob == 1:
#       print("You failed the obstacle course and died.")
#       survived = False
#     elif monster_attack_prob == 2:
#       print("You successfuly completed the course.")
#       points += 1
#       survived = True

# def randomization():
#   global survived
#   stored = []
#   if random.randint(1,2) == 2:
#     left()
#     l = "left"
#     stored.append(l)
#   if random.randint(1,2) == 2:
#     right()
#     r = "right"
#     stored.append(r)
#   if random.randint(1,2) == 2:
#     straight()
#     s = "straight"
#     stored.append(s)
#   answer = input("Which direction would you like to go? ")
#   if answer in stored:
#     print ("You move " + answer)
#   elif stored == []:
#     print("You entered a dead end and died from suffocation")
#     survived = False
#   elif answer not in stored and stored != []:
#     print("That was not an option. Due to your stupidity, you ran into a wall and died.")
#     survived = False

#     return survived
  
# total_points = 0
# total_points += points 
# print("Points: " + str(total_points))
# print(" --")
# print(" -")

# while survived:
#   randomization()
#   monster()
#   # (UNECESSARY) total_points += points 
#   # (UNECESSARY) print("Points: " + str(total_points))
#   print(" --")
#   print(" -")



# print("Rooms survived: " + str(points))
# while survived:
#   randomization()
#   print("Rooms survived: " + str(points))
#   print(" ")
#   print()

# else:
#   print("Your failed life flashes before your eyes . . . ")
#   print("You died")
#   print("ಥ_ಥ")


#|--Will's Help--|#

dungeon_map = [["Start", "Monster", "Empty"], 
               ["Empty", "Obstacle", "Monster"], 
               ["Monster", "Treasure", "Exit"]]

class Player:
  x = 0
  y = 0
  is_alive = True

  def move(self, options):
    selection = input("Select an option: ")

    while not selection in options:
      selection = input("That wasn't a choice, try again: ")

    if selection == "Right":
      self.x += 1
    elif selection == "Left":
      self.x -= 1
    elif selection == "Up":
      self.y -= 1
    elif selection == "Down":
      self.y += 1
    
def list_options(player: Player):
  options = []
  
  if not player.x + 1 > len(dungeon_map[player.y]) - 1: 
    options.append("Right")
  if not player.x - 1 < 0:
    options.append("Left")
  if not player.y + 1 > len(dungeon_map) - 1:
    options.append("Down")
  if not player.y - 1 < 0:
    options.append("Up")

  print("You can move")
  for option in options:
    print(option)
  return options

def check_encounter(player):
  current_room = dungeon_map[player.y][player.x]
  if current_room == "Monster":
    monster_encounter(player)
  elif current_room == "Empty":
    print("You enter an empty room")
  elif current_room == "Obstacle":
    obstacle_encounter(player)
  elif current_room == "Treasure":
    print("You found treasure!")
  elif current_room == "Start":
    print("You have ended up where you started")
  else:
    print("You escaped the dungeon with a hefty reward!")
    player.is_alive == False

def monster_encounter(player):
  print("You encountered a monster!")
  survival_chance = random.randint(1,2)
  if survival_chance == 1:
    print("You died.")
    player.is_alive = False
  else:
    print("You survived.")
    
def obstacle_encounter(player):
  print("You have entered an obstacle course")
  survival_chance = random.randint(1,2)
  if survival_chance == 1:
    print("You died.")
    player.is_alive = False
  else:
    print("You survived.")

def start_game_loop():
  player = Player()

  introduction()
  
  while player.is_alive:
    options = list_options(player)
    player.move(options)
    check_encounter(player)

start_game_loop()