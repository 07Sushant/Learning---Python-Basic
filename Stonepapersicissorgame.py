from multiprocessing import RLock
from random import random


user_input = input("Enter a choice : Rock,paper,scissor")
possible_action = ["Rock","paper","scissor"]
computer_action = random.choice(possible_action)

#Logic behind the game
if((user_input == Rock and computer_action == paper) or (computer_action == paper and user_input == Rock))
print("paper won")
elif((user_input == Rock and computer_action == scissors) or (computer_action == Rock and user_input == scissors))
