import random
import time
import os
import sys
import time
def animated(text):
     for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.01)

logo = '''
   db    888888 888888    db     dP""b8 88  dP 
  dPYb     88     88     dPYb   dP   `" 88odP  
 dP__Yb    88     88    dP__Yb  Yb      88"Yb  
dP""""Yb   88     88   dP""""Yb  YboodP 88  Yb 

'''
animated(logo)
print('         »»»Devoloper By White_Devil«««')
print('     ______________________________________')

# Game settings
player_health = 1000
enemy_health = 1000
player_attack_power = 130
enemy_attack_power = 200

def print_status():
    print(f"\nPlayer Health: {player_health}")
    print(f"Enemy Health: {enemy_health}")

def player_turn():
    global enemy_health
    action = input("\nChoose an action: [A]ttack, [H]eal: ").strip().lower()
    if action == 'a':
        damage = random.randint(0, player_attack_power)
        enemy_health -= damage
        print(f"\nYou attack the enemy for {damage} damage!")
    elif action == 'h':
        heal_amount = random.randint(100, 150)
        global player_health
        player_health += heal_amount
        print(f"\nYou heal yourself for {heal_amount} health!")
    else:
        print("Invalid action!")

def enemy_turn():
    global player_health
    damage = random.randint(0, enemy_attack_power)
    player_health -= damage
    print(f"\nThe enemy attacks you for {damage} damage!")

def game_over():
    if player_health <= 0:
        print("\nYou have been defeated!")
        return True
    elif enemy_health <= 0:
        print("\nYou defeated the enemy!")
        return True
    return False

def main():
    global player_health, enemy_health
    print("Welcome to the Combat Game!")
    print("Fight the enemy and try to survive.")
    time.sleep(1)

    while True:
        print_status()
        player_turn()
        if game_over():
            break
        enemy_turn()
        if game_over():
            break
        time.sleep(1)

    print_status()
    print("Game Over")

if __name__ == "__main__":
    main()


