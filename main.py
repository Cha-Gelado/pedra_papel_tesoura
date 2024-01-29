import random
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



print("Welcome to the Rock, Paper, Scissors Game!")
print("Type 0 for Rock, 1 for Paper, 2 for Scissors")
print("What do you choose?")
User = input()
      
if User == "0":
  print (rock)
elif User == "1":
  print(paper)
else :
  print(scissors)

print("Computer chose:")
Computer = random.randint(0,2)
if Computer == 0:
  print (rock)
elif Computer == 1:
  print(paper)
else :
  print(scissors)

if User == "0" and Computer == 0:
  print("It's a draw!")
elif User == "0" and Computer == 1:
  print("You lose!")
elif User == "0" and Computer == 2:
  print("You win!")
elif User == "1" and Computer == 0:
  print("You win!")
elif User == "1" and Computer == 1:
  print("It's a draw!")
elif User == "1" and Computer == 2:
  print("You lose!")
elif User == "2" and Computer == 0:
  print("You lose!")
elif User == "2" and Computer == 1:
  print("You win!")
else:
  print("It's a draw!")
