# Global-Scope
import random

class Game:
    def __init__(self):
        pass

    # The Nemesis Chance to Challenge the Player
    def encounter(self, chance, player, nemesis):
        dice = random.randint(chance, 100)
        if dice == 100:
            while True:
                print('Oh no! It\'s the Spelling Nemesis!')
                print('\nYou have ' + str(player.health) + ' hp!')
                print('The Spelling Nemesis has ' + str(nemesis.health) + ' hp.\n')
                print()
                print("What do you want to do?")

                # Attack Option
                if 'a' in player.inventory:
                    print ('1. Attack!')
                else: print ('1. ttck!')
                # Defend Option
                if 'd' in player.inventory:
                    print("2. Defend!")
                else:
                    print('2. efen!')
                # Run Away!
                print("3. run")

                print("> ",)
                # The Actual Options
                user_input = int(input())

                # Attack Function Call
                if user_input == 1:
                    player.attack(nemesis)
                    nemesis.attacksChance(player)
                if nemesis.health <= 0:
                    print("Impossible!") #Literally Impossible

                # Defend Function Call
                elif user_input == 2:
                    player.defend(nemesis)
        
                # Run Away Function Call
                elif user_input == 3:
                    print("You run away from the Nemesis...")
                    break
        else: 
            pass
    
    #-------------------------------------------------------------------------------------

    # The Final Encounter with the Nemesis
    def final_encounter(self, player, nemesis):
        print('Oh no! It\'s the Spelling Nemesis!')
        if 'a' in player.inventory and 'd' in player.inventory and 's' in player.inventory:
            nemesis.set_health(200)
            player.health = 100
        elif 'a' in player.inventory and 'd' in player.inventory:
            nemesis.set_health(200)
            player.health = 70
        else: pass
        while True:
            print('\nYou have ' + str(player.health) + ' hp!')
            print('The Spelling Nemesis has ' + str(nemesis.health) + ' hp.\n')
            print()
            print("What do you want to do?")
            print ('1. Attack!')
            print("2. Defend!")
            if 's' in player.inventory:
                print('3. Teach')
            else: 
                print('3. invalid')
            print("4. Run")
            print()
            # The Actual Options
            user_input = int(input('> '))

            # Attack Function Call
            if user_input == 1:
                player.attack(nemesis)
                nemesis.attacksFinal(player)

            # Defend Function Call
            elif user_input == 2:
                player.defend(nemesis)
            
            elif user_input == 3:
                player.teach(nemesis)
    

            # Run Away Function Call
            elif user_input == 4:
                print("You run away from the Spelling Nemesis...")
                break
            else: 
                print('Have you forgotten how to count? Try again. ')
            if nemesis.health <= 0:
                print('You\'ve defeated The Spelling Nemesis!')
                # player.congratulations()
                break
    

    # The Game Itself
    def dialogue(self, player, nemesis):
        while True:
            # You are in the BEDROOM
            if player.location == 'bedroom':
                while True:
                    print('\nYou are in the BEDROOM.')
                    print('What would you like to do?')
                    print('\n1. Take a Nap')
                    print('2. Check the Trashbin')
                    print("3. Go to the Bathroom")
                    print("4. Go to the Lobby")
                    print("5. Quit.\n")
                    user_input = int(input('> '))
                    if user_input == 1:
                        player.restore()
                    elif user_input == 2:
                        player.trash()
                    elif user_input == 3:
                        player.location = 'bathroom'
                        break
                    else:
                        print('Please enter a valid option.')
            # You are in the BATHROOM
            if player.location == 'bathroom':
                while True:
                        print('\nYou are in the BATHROOM.')
                        self.encounter(100, player, nemesis)
                        print('What would you like to do?')

                        print('\n1. Check the Mirror')
                        print('2. Go back to the Bedroom')
                        user_input = int(input('> '))
                        # Check the Mirror
                        if user_input == 1:
                                player.mirror()
                        # Go back to the Bedroom
                        elif user_input == 2:
                                player.location = 'bedroom'
                                break
                        else:
                            print('Please enter a valid option.')
            # You are in the LOBBY
            # Sam can be found here.
            # Sam prompts a puzzle.

            # You are OUTSIDE

            # You are at the GYM
            # Zach can be found here.


            # You are in the LIBRARY
            # A 100% encounter book can be found here.
            # The Librarian prompts a puzzle.

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power


class Player(Character):
    def __init__(self, name, health, power, location):
        super().__init__(name, health, power)
        self.inventory = ['a', 'd', 's']
        self.awareness = []
        self.trashbin = []
        self.location = location

    def alive(self):
        if self.health > 0:
            return True

    # Check the Trash for letters. Boss can append letters here.
    def trash(self):
        print('You check the trashbin.')
        if 'd' in self.trashbin:
            self.inventory.append('d')
            # index = self.inventory.index('d')
            # self.trashbin.pop(index)
            print('You recover the letter: \'d\'.')
        if 'a' in self.trashbin:
            self.inventory.append('a')
            # index = self.inventory.index('a')
            # self.trashbin.pop(index)
            print('You recover the letter: \'a\'.')
        if 's' in self.trashbin:
            self.inventory.append('s')
            print('You recover the letter \'s\'')
        else: print('\nThere is nothing in the trashbin.')

    # Rest in bedroom to restore HP
    def restore(self):
        self.health = 45
        print('\nYou take a nap and recover to full hp!')

    # Attack the Target
    def attack(self, target):
        if 'a' in self.inventory: 
            target.health -= self.power
            print('You attack ' + target.name + ' for ' + str(self.power) + 'dmg!')
        # Does not have the correct letter
        else: print('You fail to ttck ' + target.name + '.')
    
    def teach(self, target):
        if 's' in self.inventory:
            target.health -= self.power * 2
            print('You decide to teach The Spelling Nemesis a lesson. Literally.')
        else: print('Can\'t you read? This option is INVALID.')


    # Defend against the Target
    def defend(self, target):
        if 'd' in self.inventory:
            self.health = self.health - target.power/2
            print('\nYou defend yourself against the onslaught of ' + target.name + '. ' + target.name + ' does '+ str(target.power/2) + ' dmg. \n')

            # Chance to Heal
            dice = random.randint(1, 3)
            if dice == 2:
                self.health = self.health + 5
                print('BONUS! You were able to heal for 5 hp!\n')
                # Keeps HP to max
                if self.health >= 45:
                    self.health = 45
     
        # Does not have the correct letter
        else:
            print('You failed to efen yourself against ' + target.name + '.')
    
    # Find a Book in the Library, 100% Encounter
    def book(self, player):
        print('You decide to read a book.')
        player.power = player.power + 10
        print('Your power increases by 10!')
    

    # # Found a Letter, Goes to Inventory
    # def obtain(self, letter=''):
    #     if letter == 'a':
    #         test = 'a' #Array
    #         self.inventory.append(test)
    #     if letter == 'd':
    #         test2 = 'd' # Define
    #         self.inventory.append(test2)
    #     if letter == 's':
    #         test3 = 's' #String
    #         self.inventory.append(test3)


class Boss(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    # Check Status
    def alive(self):
        if self.health > 0:
            return True
    
    # Change Health 
    def set_health(self, value):
        self.health = value

    # Basic Attack
    def attack(self, player):
        player.health -= self.power
        print('The Spelling Nemesis attacks you with a jarble of words!')


    # Special Attack: Nemesis will prompt you to spell a word.
    def specialAttack(self, player):
        dice = random.randint(1, 2)
        if dice == 1:
            testing = input('So you think you can spell? Very well. How do you spell DEFINE? ')
            if testing == 'define':
                print('AGGGGGHHH!!')
            else:
                player.health -= self.power 
                print('I knew you were a fool!')
                print(self.name + ' kicks you for ' + str(self.power) + 'dmg.')
        if dice == 2:
            pass

    # Steals a letter from the Player, Throws in the Trash
    def curse(self, player):
        player.trashbin.append(player.inventory.pop())
        print('Oh no! ' + self.name + ' threw one of your letters in the trash!')
    
    # Randomizes what attck is used.
    def attacksChance(self, player):
        dice = random.randint(1, 100)
        if dice == 1:
            self.curse(player)
        elif dice > 1 and dice <= 20:
            self.specialAttack(player)
        else:
            self.attack(player)

    # Final Battle Options
    def attacksFinal(self, player):
        dice = random.randint(1, 100)
        if dice == 1:
            print("The Spelling Nemesis tries to steal one of your letters, but fails! Your spelling ability is too solid.")
            print('The Spelling Nemesis: \"Where has all this power come from?!\"')
        elif dice > 1 and dice <= 20:
            self.specialAttack(player)
        else:
            self.attack(player)


class NPC:
    def __init__(self, name):
        self.name = name 

    def hello(self, player):
        print(self.greeting)
        
    def secret(self, player):
        pass

# ====================================================================================================

    # First Conversation Zach
    def zachTalk(self):
        print('You decide to chat with Zach.')
        print('Zach: \"Hey! I\'m finishing my weekly write-up right now. Can you believe I found some of my notes in the trash? Glad I checked!\"')

        # Change option to 'Help Zach wih his Work'
        # Create the append for self.awareness to make this work
        # if player.awareness == 'zach1':

    # Second Conversation Zach
    def zachTalk2(self, player):
        print('You see that Zach is deep in thought.')
        print('Zach: \"Oh? I\'m alright. I was just trying to remember another word for a list.\"')
        answer = input('Zach: What was it again? >> ').lower()
        if answer == 'array':
            print('Zach: \"Wow thanks! Now I can finish my write-up.\"')
            print('Your memories are slowly coming back to you...')
            player.inventory.append('a')
            print('You obtain the letter \'A\'!')
        else:
            print('Zach: \"I don\'t think that\'s it...\"')
    
    def zachTalk3(self, player):
        print('Zach: \"Thanks again! I\'d head outside if you need some fresh air.\"')

    # First Conversation Sam
    def samTalk(self, player):
        print('You decide to approach Sam.')
        print('Sam: \"Hey! What\'s up? Are you looking for a new book? You should check the manga section. They\'ve added some really great additions recently.\"')

    # Second Conversation Sam
    def samTalk2(self, player):
        print('You talk to Sam again.')
        print('Sam: \"The Gym? It\'s right across the street and to the right from here. I don\'t think they are open right now though. Why do you ask?\"')

    def samTalk3(self, player):
        print('Sam: \"Don\'t forget to checkout once you\'re done!\"')



    # First Conversation ID Sean
    def seanTalk(self, player):
        print('You decide to approach Sean.')
        print('Sean: \"Nice to see you outside! Make sure you get some rest if you aren\'t feeling good.\"')
    
    # Second Conversation ID Sean
    def seanTalk2(self, player):
        print('Sean: \"You want a bonus question? OK! Here\'s a contrived example.\"')
        print('Sean: \"What\'s a word for wrapping related data?\"')
        answer = input('It starts with an \'E\'? >> ').lower()
        if answer == 'encapsulate':
            print('Sean: \"Awesome job!\"')
            player.inventory.append('s')
            print('Your memories are slowly coming back to you...')
            print('You obtain the letter \'S\'!')
        else:
            print('Sean: \"Nope! Sorry. You can always do a Google search for help!\"')
    
    # Ending Conversation
    def seanTalk3(self):
        print('Sean: \"Make sure you take breaks!\"')