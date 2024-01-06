rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
print("Welcome to the Rock Paper Scissor Challenge.\n")

# We'll create a list just for storing the ASCII images
choices = [rock,paper,scissors]

player_choice = int(input("What do you want to choose? Enter 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if player_choice >= 3:
    print("Invalid Entry! Please type again.")
else:
    computer_choice = random.randint(0,2)

    print(choices[player_choice])
    print(choices[computer_choice])

    outcome = ["Its a Draw","You Loose","You Win"]
  # Draw will always be at 1st position i.e index[0]
  # the other 2 will change positions as per the next code i.e. C-P or P-C
    print(outcome[ computer_choice - player_choice])


