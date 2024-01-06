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
options = [rock,paper,scissors]

user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
user_input_n = int(user_input)

if user_input_n >= 3:
  print("Invalid option! Please re-enter.")
else:
  comp_choice = random.randint(0,2) #Taking the input from the computer
  
  #using list indexing with the received inputs to show ASCII images
  print(options[user_input_n])
  print(options[comp_choice])
  
  # ***********These are the Possible Result matrix scenarios formed from RPS options. 
  # result_set = [["draw","lose","win"],
  #              ["win","draw","lose"],
  #              ["lose","win","draw"]]
  # *** Rock = 0, Paper = 1 and scissors = 2 ***
  
  game = [user_input_n,comp_choice] # we know that game is based on inputs so we create a new list
  
  if user_input_n == comp_choice:
    print(" Its a Draw! Try Again.\n")
    
  elif game == [0,2] or game == [1,0] or game == [2,1]:
    print("You Win")
    
  elif game == [0,1] or game == [1,2] or game == [2,0]:
    print("You Lose.")
