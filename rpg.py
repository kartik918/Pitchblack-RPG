# -*- coding: utf-8 -*-
"""
Created on Thu Jun 6 11:42:48 2019

@author: Kartik
"""

import random
import time
import sys
import re

class GameSettings:
    PLAYER_ATTACK = random.randint(5, 10)
    MAX_ENEMY_STRENGTH = 15
    MIN_ENEMY_STRENGTH = 5
    ENEMIES = ['behemoth', 'goblin', 'hellstep', 'orc', 'golem', 'zombie', 'undead mermaid','brinebrute', 'soulcreep','murkmutant']
    ENEMY_PREFIX = ['big', 'giant', 'ugly', 'fat', 'angry', 'vicious', 'murderous', 'vile', 'fat', 'dyslexic', 'terribly anorexic']
    ENEMY_WEAPON = ['sword', 'warhammer', 'charming smile', 'axe', 'hammer', 'club', 'giant bone', 'mace', 'dagger', 'terrible case of body odor', ' shiny gauntlet from a dead city soldier']
    PLAYER_WEAPON = {"sword": 2, "axe": 3, "bow": 2}
    PLAYER_HEAL = 5
    
class Player:
    name = input('What is your name traveller? ')
    
    number = re.compile(r'[1,2,3]+')                                                        #characters allowed
    weapon_choice = input('Choose your weapon: 1. Sword, 2.Battle Axe, 3. Recurve Bow ')    #while loop that executes till the entered character entered is valid
    
    while not number.match(weapon_choice):                                                  #compares the character entered
        print ("Please enter a valid character")                                            #executes if character entered is invalid
        weapon_choice = input('Choose your weapon: 1. Sword, 2. Battle Axe, 3. Recurve Bow ')
    if weapon_choice == '1':
        weapon_bonus = 2
        weapon = 'sword'
    elif weapon_choice == '2':
        weapon_bonus = 3
        weapon = 'axe'
    elif weapon_choice == '3':
        weapon_bonus = 2
        weapon = 'bow'
    else:
        print("You did not choose a weapon, restarting game...")
        
    attack = GameSettings.PLAYER_ATTACK + weapon_bonus
    health = 15

class Enemy:
    name = random.choice(GameSettings.ENEMY_PREFIX) + ' ' + random.choice(GameSettings.ENEMIES)
    weapon = random.choice(GameSettings.ENEMY_WEAPON)
    attack = random.randint(GameSettings.MIN_ENEMY_STRENGTH, GameSettings.MAX_ENEMY_STRENGTH)
    health = random.randint(1, 20)

playAgain = 'Y'

def say(text):
    for char in text:
        print(char, end = '')
        time.sleep(.04)
    print('')
    time.sleep(.4)

def intro():
    say(f"Greetings, {Player.name}.")
    if Player.weapon == 'sword':
        say("You have a sword in your hand.")
    elif Player.weapon == 'axe':
        say("You have an axe by your side. Slow, but strong.")
    elif Player.weapon == 'bow':
        say("You picked the bow. Silent but deadly.")
    say('You were sent to clear out the Pitchblack cave by the kingdom.')
    say('You reach your destination, the cave dark as the night as you enter.')

def instance():
    say(f"You have encountered a {Enemy.name} wielding a {Enemy.weapon}.")
    say(f"Its attack is {Enemy.attack} and it has {Enemy.health} health.")
    say(f"Your attack would do {Player.attack} damage. You have {Player.health} health left.")
    say(f"You choose to:")
    say(f"1. Attack, 2. Run")
    
    number = re.compile(r'[1,2]+')                                                  #characters allowed
    choice = input()                                                                #while loop that executes till the entered character entered is valid
    
    while not number.match(choice):                                                 #compares the character entered
        print ("Please enter a valid character")
        choice = input()
    if choice == '1':
        battle()
    elif choice == '2':
        end()
 
        

def battle():
    while Enemy.health > 0:
        say(f"You attack the {Enemy.name} with your {Player.weapon}.")
        Enemy.health = Enemy.health - Player.attack
        if Enemy.health <= 0:
            say(f"Your attack did {Player.attack} damage. The {Enemy.name} falls.")
            victory()
            
        say(f"Your attack did {Player.attack} damage. The {Enemy.name} now has {Enemy.health} health.")
        
        Player.health = Player.health - Enemy.attack
        say(f"The {Enemy.name} attacks back. You take {Enemy.attack} damage. Your health is now {Player.health}.")
        if Player.health > 0 and Enemy.health <= 0:
            victory()
        if Player.health <= 0:
            say("You died. Game Over.")
        

def difficulty():
    instance.score = instance.score + 1
    Player.attack = Player.attack + random.randint(1, 3) * instance.score
    Player.health = Player.health + random.randint(1, 3) * instance.score
    Enemy.name = random.choice(GameSettings.ENEMY_PREFIX) + ' ' + random.choice(GameSettings.ENEMIES)
    Enemy.weapon = random.choice(GameSettings.ENEMY_WEAPON)
    Enemy.attack = Enemy.attack + random.randint(1, 3) * instance.score
    Enemy.health = random.randint(1, 20) + random.randint(1, 3) * instance.score

def victory():
    say(f"You defeated the {Enemy.name}.")
    difficulty()
    say(f"Your attack goes up to {Player.attack} and your health to {Player.health}")
    if GameSettings.PLAYER_HEAL > 0:
        say(f"You have {GameSettings.PLAYER_HEAL} meds left. Use them wisely.")
        say("Would you like to use one? Y/N")

    value = re.compile(r'[y,Y,n,N]+')                                               #characters allowed
    choice = input()
                                                                                    #compares the entered character                        
    while not value.match(choice):                                                  #while loop that executes till the entered character entered is valid
        print ("Please enter a valid character")
        choice = input()
    if choice == 'Y' or choice == 'y':
        Player.health = Player.health + (random.randint(1, 3) * instance.score)
        GameSettings.PLAYER_HEAL = GameSettings.PLAYER_HEAL - 1
        say(f"Your health goes up to {Player.health}. You have {GameSettings.PLAYER_HEAL} meds left.")
    else:
        say(f"You still have {GameSettings.PLAYER_HEAL} meds left.")
    if GameSettings.PLAYER_HEAL == 0:
        say("You are out of meds. Good luck.")
    say("Go deeper into the cave? Y/N")
    value = re.compile(r'[y,Y,n,N]+')
    choice = input()
    
    while not value.match(choice):
        print ("Please enter a valid character")
        choice = input()
    
    if choice == 'Y' or  choice == 'y':
        say('You march forward...')
        instance()
    if choice == 'N' or  choice == 'n':
        end()
def end():
    say("You decide to be smart and retreat...")
    say(f"You defeated {instance.score} monsters.")
    say(f"Thank you for playing.")
    sys.exit('Exit game')

        
while playAgain == 'Y' or playAgain == 'y':
        intro()
        instance.score = 0
        instance()
        end()
        break