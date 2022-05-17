import random

name = "Tom"
question = "Will I get a new job this year?"
answer = ""
random_number = random.randint(1, 12)

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
  answer = "It is a certainty."
elif random_number == 11:
  answer = "Signs unclear."
elif random_number == 12:
  answer = "Inconceivable."
else:
  answer = "Error"

if question == "":
  print("An unsolicited answers weakens a person's curiosity.")
else:
  if name == "":
    print("Question:", question)
  else:
    print(name, "asks:", question)
  print("Magic 8-Ball's answer:", answer)
