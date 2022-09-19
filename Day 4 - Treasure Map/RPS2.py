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

cpu_choices = [rock, paper, scissors]

print("Let's play Rock, Paper, Scissors!")
player_choice = int(input("What's your choice? Type 0 for 'Rock', 1 for 'Paper', or 2 for 'Scissors': "))
end_range = len(cpu_choices) - 1
cpu_pick = random.randint(0, end_range)
win_condition = 0


if player_choice >= 3 or player_choice < 0:
    print("You picked an invalid number. You lose.")
else:
    if player_choice == 0 and cpu_pick == 1:
            win_condition = 0
    elif player_choice == 1 and cpu_pick == 0:
            win_condition = 1
    elif player_choice == 0 and cpu_pick == 2:
            win_condition = 1
    elif player_choice == 2 and cpu_pick == 0:
            win_condition = 0
    elif player_choice == 2 and cpu_pick == 1:
            win_condition = 1
    elif player_choice == 1 and cpu_pick == 2:
            win_condition = 0
    elif player_choice == cpu_pick:
            win_condition = 3

    if player_choice == 0:
        print(f"Player Pick = {rock}")
    elif player_choice == 1:
        print(f"Player Pick = {paper}")
    else:      
        print(f"Player Pick = {scissors}")
        
    print("CPU pick = \n" + cpu_choices[cpu_pick]) 
    
    if win_condition == 1:
        print("You win!")
    elif win_condition == 0:
        print("You Lose. Try Again!")
    elif win_condition == 3:
        print("It's a draw!")
        

   