import random

user_win = 0
computer_win = 0
draw = 0
options = ["rock", "paper", "scissors"]

while True:
  user_input = input("Type Rock/Paper/Scissors or Q to qiut: ").lower()

  if user_input == "q":
    break
  
  if user_input not in options:
    continue
  
  random_number = random.randint(0, 2)
  computer_pick = options[random_number]

  print("Computer picked", computer_pick + ".")

  if user_input == "rock" and computer_pick == "scissors":
    print("You won!")
    user_win += 1

  elif user_input == "paper" and computer_pick == "rock":
    print("You won!")
    user_win += 1

  elif user_input == "scissors" and computer_pick == "paper":
    print("You won!")
    user_win += 1
  
  elif user_input == computer_pick:
    print("You draw!")
    draw += 1

  else:
    print("You lost!")
    computer_win += 1
    continue
  
print("You won", user_win, "times")
print("You draw", draw, "times")
print("Computer won", computer_win, "times")
print("Goodbye")