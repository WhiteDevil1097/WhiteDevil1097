import curses
import random
import time
import requests
import os
import sys
import time
def animated(text):
     for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.01)

logo = '''
 _______           _______  _______ _________
(  ____ \|\     /|(  ___  )(  ___  )\__   __/
| (    \/| )   ( || (   ) || (   ) |   ) (   
| (_____ | (___) || |   | || |   | |   | |   
(_____  )|  ___  || |   | || |   | |   | |   
      ) || (   ) || |   | || |   | |   | |   
/\____) || )   ( || (___) || (___) |   | |   
\_______)|/     \|(_______)(_______)   )_(   
'''
animated(logo)
print('       »»»Devoloper By White_Devil«««')
print('      _________________________________')

# Define the player, enemy, and boss ASCII art
PLAYER = ["  O  ", "/|\\", "/ \\"]
ENEMY = ["\\|/", "-O-", "/|\\"]
BOSS = [
    "   _____   ",
    "  /     \\  ",
    " |  O O  | ",
    " |  \\_/  | ",
    "  \\_____/  "
]

def draw_entity(win, entity, y, x):
    """Draws a multi-line entity (like player, enemy, or boss) at the given position."""
    for i, line in enumerate(entity):
        win.addstr(y + i, x, line)

def main(stdscr):
    # Set up the screen
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(200) # Refresh rate in ms

    sh, sw = stdscr.getmaxyx()  # Get screen height and width

    # Initialize player position
    player_x = sw // 2
    player_y = sh - len(PLAYER) - 1

    # Initialize bullets, enemies, and boss
    bullets = []
    enemy_bullets = []
    enemies = []
    boss = None
    boss_health = 10
    boss_active = False

    score = 0
    game_over = False

    while True:
        stdscr.clear()  # Clear the screen

        if not game_over:
            # Handle user input
            key = stdscr.getch()
            if key == curses.KEY_LEFT and player_x > 0:
                player_x -= 1
            elif key == curses.KEY_RIGHT and player_x < sw - len(PLAYER[0]):
                player_x += 1
            elif key == ord(' '):
                bullets.append([player_y - 1, player_x + len(PLAYER[0]) // 2])

            # Add new enemies randomly
            if not boss_active and random.randint(1, 20) == 1:
                enemies.append([0, random.randint(0, sw - len(ENEMY[0]))])

            # Move bullets
            bullets = [[y - 1, x] for y, x in bullets if y > 0]

            # Move enemy bullets
            enemy_bullets = [[y + 1, x] for y, x in enemy_bullets if y < sh - 1]

            # Move enemies
            enemies = [[y + 1, x] for y, x in enemies if y < sh - 1]

            # Check for bullet-enemy collisions
            for bullet in bullets[:]:
                for enemy in enemies[:]:
                    if (bullet[0] in range(enemy[0], enemy[0] + len(ENEMY)) and
                            bullet[1] in range(enemy[1], enemy[1] + len(ENEMY[0]))):
                        bullets.remove(bullet)
                        enemies.remove(enemy)
                        score += 10

            # Check for game over (enemy or bullet reaches player)
            for enemy in enemies:
                if enemy[0] + len(ENEMY) >= player_y:
                    game_over = True
                    break

            for bullet in enemy_bullets:
                if bullet[0] == player_y and bullet[1] in range(player_x, player_x + len(PLAYER[0])):
                    game_over = True
                    break

            # Boss fight activation
            if score >= 50 and not boss_active:
                boss_active = True
                boss = [0, sw // 2 - len(BOSS[0]) // 2]  # Spawn boss in the center

            # Boss movement, shooting, and bullet collisions
            if boss_active:
                boss[0] += 1  # Boss moves down the screen
                if boss[0] + len(BOSS) >= sh:
                    boss[0] = 0  # Reset boss position

                # Boss shoots bullets
                if random.randint(1, 10) == 1:
                    enemy_bullets.append([boss[0] + len(BOSS), boss[1] + len(BOSS[0]) // 2])

                for bullet in bullets[:]:
                    if (bullet[0] in range(boss[0], boss[0] + len(BOSS)) and
                            bullet[1] in range(boss[1], boss[1] + len(BOSS[0]))):
                        bullets.remove(bullet)
                        boss_health -= 1
                        if boss_health == 0:
                            boss_active = False
                            score += 50

                # Draw boss
                draw_entity(stdscr, BOSS, boss[0], boss[1])

            # Draw player
            draw_entity(stdscr, PLAYER, player_y, player_x)

            # Draw bullets
            for y, x in bullets:
                stdscr.addch(y, x, '|')

            # Draw enemy bullets
            for y, x in enemy_bullets:
                stdscr.addch(y, x, '*')

            # Draw enemies
            for y, x in enemies:
                draw_entity(stdscr, ENEMY, y, x)

            # Display the score and boss health
            stdscr.addstr(0, 2, f'Score: {score}')
            if boss_active:
                stdscr.addstr(1, 2, f'Boss Health: {boss_health}')

        else:
            stdscr.addstr(sh // 2, sw // 2 - 7, "GAME OVER")
            stdscr.addstr(sh // 2 + 1, sw // 2 - 14, "Press 'q' to quit or 'r' to restart")
            key = stdscr.getch()
            if key == ord('q'):
                break
            elif key == ord('r'):
                return main(stdscr)  # Restart the game

        stdscr.refresh()  # Refresh the screen
        time.sleep(0.10)  # Control the game speed

curses.wrapper(main)

