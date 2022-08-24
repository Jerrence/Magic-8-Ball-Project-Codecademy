# Generating a random number (lines 2 and 9 to 13)
import random

# Setting up (lines 5 to 7)
name = "Lawrence"
question = "Will it rain today?"
answer = ""

# .randint() explaination: https://www.geeksforgeeks.org/python-randint-function/
# Optional Challenges (lines 11, 35 to 40, and 49 to 60)
random_number = random.randint(1, 12)

# test function for .randint()
# print(random_number)

# Control Flow (lines 16 to 35)
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Poor internet connection, talk to you later."
elif random_number == 11:
  answer = "Sorry, Magic 8-Ball is currently unavailable. Try again later."
elif random_number == 12:
  answer = "ERROR, status code: 500 (the server encountered an unexpected condition that prevented it from fulfilling the request)."
else:
  answer = """
  ERROR,

  random_number = random.randint(1, 12) | line 10
  .randint() Out of Bounds."""

# Seeing the result (lines 38 and 39)
if question == "":
  print("""
  ERROR,
  
  variable question is undefined | line 6""")
  # The exit() function ingnores everything after it runs
  exit()

if name:
  print(name + " asks: " + question)
else:
  print("Question: " + question)

print("Magic 8-Ball's answer: " + answer)
