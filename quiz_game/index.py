print("\nWelcome to my Quiz Game!\n")

playing = input("Do you want to play? (yes/no) ");

if playing.lower() != "yes":
  quit()
  
print("Okay! Let's play :")

totalCorrectAnswer = 0
totalWrongAnswer = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
  print("Correct")
  totalCorrectAnswer += 1
else:
  print("Incorrect! \nThe answer is Central Processing Unit")
  totalWrongAnswer += 1

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
  print("Correct")
  totalCorrectAnswer += 1
else:
  print("Incorrect! \nThe answer is Graphics Processing Unit")
  totalWrongAnswer += 1

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
  print("Correct")
  totalCorrectAnswer += 1
else:
  print("Incorrect! \nThe answer is Random Access Memory")
  totalWrongAnswer += 1

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
  print("Correct")
  totalCorrectAnswer += 1
else:
  print("Incorrect! \nThe answer is Power Supply")
  totalWrongAnswer += 1

print("Total correct answer: {0}".format(totalCorrectAnswer))
print("Total incorrect answer: {0}".format(totalWrongAnswer))