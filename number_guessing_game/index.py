import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
  top_of_range = int(top_of_range)
  if top_of_range <= 0:
    print("Please type the number larger than 0 next time!")
    quit()
else:
  print("Please type the number next time!")
  quit()


random_number = random.randint(0, top_of_range)
# print(random_number)
guesses = 0
while True:
  guesses += 1
  answer = input("Guess the correct number: ")
  if answer.isdigit():
    answer = int(answer)
  else:
    print("Please type the number next time!")
    continue

  if answer == random_number:
    print("You got the correct number!")
    break;
  elif answer > random_number:
    print("you were above the number!")
  else:
    print("you were below the number!")

print("You got it in", guesses, "guesses")