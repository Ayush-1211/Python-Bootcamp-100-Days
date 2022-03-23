enemies = 1   #Global Scope
def increase_enemies():
  enemies = 2   #Local Scope
  print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies outside function: {enemies}")


player_health = 10  #Global Scope
def game():
  def drink_potion():
    potion_strenth = 2  #Local Scope
    print(player_health)
  drink_potion()
print(player_health)

#There is no block scope in python
game_level = 3
enemies2 = ["Skeleton", "Aliens", "Zombie"]
if game_level < 5:
  new_enemy = enemies2[0]
print(new_enemy)    #we can call this from "if, for loop, while loop, etc... But we can not call this from a function


#Modifying Global Variable    METHOD-1
counter = 10
def increase_counter():
  global counter
  counter = 2
  print(f"Counter inside function: {counter}")
increase_counter()
print(f"Counter outside function: {counter}")

#Modifying Global Variable    METHOD-2
counter2 = 10
def increase_counter2():
  print(f"Counter inside function: {counter2}")
  return counter2 + 2
counter2 = increase_counter2()
print(f"Counter outside function: {counter2}")


#Global Constant
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDEL = "@ayush_prajapati"