# TO DO
#
# Add Skill Training
# Create Quests/Campagin

import random
import time
import string
import math

print '____________ _____   '
time.sleep(.3)
print '| ___ \ ___ \  __ \  '
time.sleep(.3)
print '| |_/ / |_/ / |  \/  '
time.sleep(.3)
print '|    /|  __/| | __   '
time.sleep(.3)
print '| |\ \| |   | |_\ \  '
time.sleep(.3)
print '\_| \_\_|    \____/  '
time.sleep(.3)

version = '1.2.7'
print 'Version ' + str(version)
print

class Player:
    def __init__(self):
        self.SaveFileName = raw_input("Enter User Name\n>> ")
        items = {}
        
    def Load(self):
        stats = []
        self.items = {}
        with open(self.SaveFileName, 'r') as savefile:
            line = savefile.readline()
        line = line.split(' ')
        for i in range(len(line)):
            stats.append(int(line[i]))
        (self.level, self.xp, self.attack, self.defense, self.hp, self.maxhp) = stats
        line = 'player loaded'
        with open(self.SaveFileName, 'r') as savefile:
            savefile.readline()
            print line
            while not line == '':
                line = savefile.readline()
                if len(line.split(' ')) == 2:
                    line = line.split(' ')
                    self.items[line[0]] = int(line[1])
        return self
        
    def New(self):
        newline = 'created new player'
        stats = [1, 0, 1, 1, 100, 100]
        weapon = None
        armor = None
        line = ' '.join(str(i) for i in (stats)) + '\n' + (str(weapon)) + '\n' + (str(armor))
        print newline
        with open(self.SaveFileName, 'w') as savefile:
            savefile.write(line)
    
    def Save(self):
        line = ' '.join(str(i) for i in (self.level, self.xp, self.attack, self.defense, self.hp, self.maxhp))
        with open(self.SaveFileName, 'w') as savefile:
            savefile.write(line)
            lines = []
            savefile.write('\n')
            for i in self.items:
                lines.append(i + ' ' + str(self.items[i]) + '\n')
            savefile.writelines(lines)
        print "player saved!"
        
    def DisplayStats(self):
        ('Level      : ' + str(self.level))
        print('XP         : ' + str(self.xp))
        print('Next Level : ' + str(100 * self.level * (self.level)))
        print
        print('Attack     : ' + str(self.attack))
        print('Defense    : ' + str(self.defense))
        print
        print('Max HP     : ' + str(self.maxhp))
        print('Curent HP  : ' + str(self.hp))
        

        
    
    def Battle(self):
        name = raw_input('    >>')
        name = name.replace(" ", "")
        xpgain = 0
        if name in Enemies.stats:
            enemy = Enemies(name[0].upper() + name[1:], Enemies.stats[name][1], Enemies.stats[name][2], Enemies.stats[name][3], Enemies.drops[name])
            print('Player:' + str(self.hp))
            print (enemy.name) + ':' + str(enemy.hp) 
            print
            while enemy.hp > 0 and self.hp > 0:
                
                enemyattack = random.randint(1, 6) + (enemy.attack)
                playerdefense = random.randint(1, 6) + (self.defense)
                if enemyattack > playerdefense:
                    self.hp = self.hp - (enemyattack - playerdefense)
                else:
                    xpgain = xpgain + random.randint(enemy.attack + playerdefense - enemyattack + 1, enemy.attack + playerdefense - enemyattack + 1) - self.defense
                
                playerattack = random.randint(1, 6) + (self.attack)
                enemydefense = random.randint(1, 6) + (enemy.defense)
                if playerattack > enemydefense:
                    enemy.hp = enemy.hp - (playerattack - enemydefense)
                    xpgain = xpgain + random.randint(enemy.defense + playerattack - enemydefense - 1, enemy.defense + playerattack - enemydefense + 1) - self.attack
                    
                if enemy.hp < 0:
                    enemy.hp = 0
                time.sleep(0.3)
                print('Player:' + str(self.hp))
                print(enemy.name.title() + ':' + str(enemy.hp))
                print
            if self.hp <= 0:
                print 'You lost'
                self.hp = self.maxhp
            else:
                self.xp = self.xp + xpgain
                print 'You win'
                print 'Enemy drops:'
                for i in range(len(enemy.drops)):
                    itemprob = random.randint(1,100)
                    if itemprob <= enemy.drops[i-1][1]:
                        quantity = random.randint(enemy.drops[i-1][2],enemy.drops[i-1][3])
                        if not enemy.drops[i-1][0] in self.items:
                            self.items[enemy.drops[i-1][0]] = 0
                        self.items[enemy.drops[i-1][0]] = self.items[enemy.drops[i-1][0]] + quantity
                        print('    ' + str(enemy.drops[i-1][0]) + '(' + str(quantity) + ')')
            if self.xp >= (100 * self.level * (self.level)):
                self.level = self.level + 1
                self.maxhp = self.maxhp + 10
                self.hp = self.hp + (self.maxhp/2)
                self.attack = self.attack + 1
                self.defense = self.defense + 1
                print ("You have leveled up!")
                print ("Type 'stats' to view your new stats")
                print ("You are now level {0}").format(self.level)
                if self.hp >= self.maxhp:
                    self.hp = self.maxhp
                    print "You have max HP"
                
    def Eat(self):
        fooditem = raw_input('    >>')
        fooditem = fooditem.lower()
        foodlist = Food()
        if fooditem == 'all':
            print "Type the food to eat until you have max HP"
            allfooditem = raw_input('    >>')
            allfooditem = allfooditem.lower()
            if allfooditem in foodlist.food and allfooditem in self.items:
                prehp = self.hp
                allfoodhp = (foodlist.food[allfooditem])
                quantity = int(self.maxhp - self.hp) / (allfoodhp)
                if quantity > (self.items[allfooditem]):
                    quantity = (self.items[allfooditem])
                self.hp = self.hp + (allfoodhp * quantity)
                self.items[allfooditem] = self.items[allfooditem] - quantity
                if self.hp >= self.maxhp:
                    self.hp = self.maxhp
                    print "You have max HP"
                    print "You ate " + str(quantity) + " " + str(allfooditem) + " and gained " + str(self.hp - prehp) + " HP"
                    print 'You now have ' + str(self.hp) + ' HP'
                else:
                    print "You ate " + str(quantity) + " " + str(allfooditem) + " and gained " + str(self.hp - prehp) + " HP"
                    print 'You now have ' + str(self.hp) + ' HP'
        if fooditem in foodlist.food and fooditem in self.items:
            if self.items[fooditem] == 0:
                print "You don't have anymore " + str(fooditem)
            if self.items[fooditem] > 0:
                prevhp = self.hp
                foodhp = (foodlist.food[fooditem])
                self.hp = self.hp + foodhp
                self.items[fooditem] = self.items[fooditem] - 1
                if self.hp >= self.maxhp:
                    self.hp = self.maxhp
                    print 'You have max HP'
                else:
                    print 'You ate some ' + str(fooditem) + ' and healed ' + str(foodhp) + ' HP'
                    print 'You now have ' + str(self.hp) + ' HP'
        if fooditem in self.items and fooditem not in foodlist.food:
            print "You can't eat that"
                    
                
    def Drink(self):
        drinkitem = raw_input('    >>')
        drinkitem = drinkitem.lower()
        drinkitem = drinkitem.replace(" ", "")
        potionlist = Potion()
        if drinkitem == 'all':
            print "Type the potion to drink until you have max HP"
            alldrinkitem = raw_input('    >>')
            alldrinkitem = alldrinkitem.lower()
            alldrinkitem = alldrinkitem.replace(" ", "")
            alldrinkitem = alldrinkitem.replace("s", "")
            if alldrinkitem in potionlist.potion and alldrinkitem in self.items:
                prehp = self.hp
                alldrinkhp = (potionlist.potion[alldrinkitem])
                quantity = int(self.maxhp - self.hp) / (allfoodhp)
                if quantity > (self.items[alldrinkitem]):
                    quantity = (self.items[alldrinkitem])
                self.hp = self.hp + (alldrinkhp * quantity)
                self.items[alldrinkitem] = self.items[alldrinkitem] - quantity
                if self.hp >= self.maxhp:
                    self.hp = self.maxhp
                    print "You have max HP"
                    print "You ate " + str(quantity) + " " + str(alldrinkitem) + " and gained " + str(self.hp - prehp) + " HP"
                    print 'You now have ' + str(self.hp) + ' HP'
                else:
                    print "You drank " + str(quantity) + " " + str(alldrinkitem) + "s and gained " + str(self.hp - prehp) + " HP"
                    print 'You now have ' + str(self.hp) + ' HP'
        if drinkitem in potionlist.potion and drinkitem in self.items:
            if self.items[drinkitem] == 0:
                print "You don't have anymore " + str(drinkitem)
            if self.items[drinkitem] > 0:
                prevhp = self.hp
                foodhp = (potionlist.potion[drinkitem])
                self.hp = self.hp + foodhp
                self.items[drinkitem] = self.items[drinkitem] - 1
                if self.hp >= self.maxhp:
                    self.hp = self.maxhp
                    print 'You have max HP'
                else:
                    print 'You ate some ' + str(drinkitem) + ' and healed ' + str(foodhp) + ' HP'
                    print 'You now have ' + str(self.hp) + ' HP'
        if drinkitem in self.items and drinkitem not in potionlist.potion:
            print "You can't eat that"
    
    
    
        



class Enemies():

    stats = {} # lvl A D HP
    stats['goblin'] = [1, 1, 1, 15]
    stats['hobgoblin'] = [2, 2, 2, 17]
    stats['imp'] = [4, 4, 2, 21]
    stats['lizardfolk'] = [5, 5, 4, 25]
    stats['harpy'] = [7, 7, 6, 32]
    stats['kobold'] = [8, 7, 8, 37]
    stats['spider'] = [9, 7, 9, 42]
    stats['troll'] = [11, 9, 11, 46]
    stats['skeleton'] = [14, 12, 14, 50]
    stats['orc'] = [16, 17, 15, 57]
    stats['giant'] = [19, 17, 20, 63]
    stats['gargoyle'] = [22, 22, 22, 75]
    stats['orge'] = [25, 25, 27, 84]
    stats['golem'] = [30, 23, 38, 90]
    stats['basilisk'] = [36, 35, 37, 97]
    stats['manticore'] = [48, 50, 45, 110]
    stats['minotaur'] = [56, 56, 55, 130]
    stats['wizard'] = [62, 65, 68, 150]
    stats['elemental'] = [67, 70, 75, 200]
    stats['dragon'] = [72, 77, 77, 400]
    stats['serpent'] = [84, 88, 85, 550]
    stats['wyvern'] = [87, 89, 91, 650]
    stats['hydra'] = [93, 94, 93, 750]
    stats['phoenix'] = [100, 100, 100, 1000]
    drops = {} # % chance, how many, out of how many
    drops['goblin'] = [['gold', 100, 1, 10],['fish', 40, 1, 1]]
    drops['hobgoblin'] = [['gold', 100, 1, 12],['meat', 75, 1, 1]]
    drops['imp'] = [['gold', 100, 1, 14],['bread', 50, 1, 1],['healthpotion', 25, 1, 1]]
    drops['lizardfolk'] = [['gold', 100, 1, 15],['fish', 50, 1, 2],['bread', 50, 1, 2]]
    drops['harpy'] = [['gold', 100, 1, 18],['bread', 75, 1, 2],['healthpotion', 50, 1, 1]]
    drops['kobold'] = [['gold', 100, 1, 21],['meat', 50, 1, 2],['healthpotion', 25, 1, 1]]
    drops['spider'] = [['gold', 100, 1, 24],['healthpotion', 75, 1, 2]]
    drops['troll'] = [['gold', 100, 5, 26],['meat', 100, 1, 4]]
    drops['skeleton'] = [['gold', 100, 7, 28],['healthpotion', 50, 1, 2]]
    drops['orc'] = [['gold', 100, 9, 31], ['meat', 100, 1, 3]]
    drops['giant'] = [['gold', 100, 12, 34], ['meat', 100, 1, 4]]
    drops['gargoyle'] = [['gold', 100, 10, 26],['healthpotion', 25, 1, 2]]
    drops['orge'] = [['gold', 100, 15, 35], ['meat', 100, 1, 4]]
    drops['golem'] = [['gold', 100, 18, 37],['healthpotion', 50, 1, 3]]
    drops['basilisk'] = [['gold', 100, 20, 40], ['meat', 100, 2, 6]]
    drops['manticore'] = [['gold', 100, 25, 44], ['meat', 100, 3, 8]]
    drops['minotaur'] = [['gold', 100, 30, 50], ['meat', 100, 4, 11]]
    drops['wizard'] = [['gold', 100, 40, 60], ['bread', 100, 5, 11]]
    drops['elemental'] = [['gold', 100, 50, 80],['healthpotion', 75, 3, 7]]
    drops['dragon'] = [['gold', 100, 60, 90], ['meat', 100, 7, 17]]
    drops['serpent'] = [['gold', 100, 70, 100], ['meat', 100, 10, 20]]
    drops['wyvern'] = [['gold', 100, 80, 120], ['meat', 100, 14, 20]]
    drops['hydra'] = [['gold', 100, 90, 150], ['meat', 100, 20, 32]]
    drops['phoenix'] = [['gold', 100, 200, 300],['healthpotion', 100, 3, 10]]
    
    def __init__(self,name,attack,defense,hp,drops):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.drops = drops
    
  
def LoadPlayer():
    player = Player()
    choice = raw_input('Enter \'new\' for a new player or press enter to load this player\n>> ')
    if choice == 'new':
        player.New()
        player.stats = player.Load()
    else:
        player.stats = player.Load()
    return player
        

class Food():
    
    def __init__(self):
        self.food = {}
        self.food['bread'] = 2
        self.food['fish'] = 3
        self.food['meat'] = 5
        
class Potion():
    
    def __init__(self):
        self.potion = {}
        self.potion['healthpotion'] = 10

        
class Menu():
    def RunMenu(self, player):
        choice = ''
        while not choice == 'exit':
            levelup = str(100 * player.level * (player.level))
            choice = raw_input('>>')
            choice = choice.lower()
            choice = choice.replace(" ", "")
            if choice == 'save':
                player.Save()
            if choice == 'help':
                newHelp = self.Help()
                newHelp.RunHelp()
            if choice == 'stats':
                player.DisplayStats()
            if choice == 'battle':
                player.Battle()
            if choice == 'shop':
                player.Shop()
            if choice == 'eat':
                player.Eat()
            if choice == 'drink':
                player.Drink()
            if choice == 'i' or choice == 'inv' or choice == 'inventory':
                print str(player.items)
            if choice == 'enemies':
                DisplayEnemies()
            if choice == 'hp':
                print ('Your current HP is ' + str(player.hp))
                time.sleep(.3)
                print ('Your max HP is ' + str(player.maxhp))
            if choice == 'attack' or choice == 'att':
                print ('Your attack is ' + str(player.attack))
            if choice == 'defense' or choice == 'def':
                print ('Your defense is ' + str(player.defense))
            if choice == 'lvl' or choice == 'level':
                print ('You are level ' + str(player.level))
            if choice == 'xp':
                print 'You have ' + str(player.xp) + ' XP'
                time.sleep(.3)
                print 'You need ' + levelup + ' XP to level up'
                time.sleep(.3)
                print 'You need ' + str(int(levelup) - int(player.xp)) + ' more XP to level up'
            if choice == 'version':
                print 'This Game is Version ' + str(version)
            if choice == 'credits':
                Credits()
            if choice == 'tutorial':
                Tutorial()
            if choice in player.items:
                print(choice + '(' + str(player.items[choice]) + ')')
                

    class Help():
        
        def RunHelp(self):
            print('Enter \'tutorial\' to see the tutorial')
            print('To quit the game, enter \'exit\', but remeber to save using \'save\' first!')
            print('To fight, enter \'battle\' followed by enemy name. For the list of enemies, enter \'enemies\'.')
            print('You may eat or drink an item by entering \'eat\' or \'drink\', then entering the item\'s name')
            print('To view the credits, enter \'credits\' below')
            choice = raw_input('    >>')
            if choice == 'enemies':
                DisplayEnemies()
            if choice == 'credits':
                Credits()
            if choice == 'tutorial':
                Tutorial()
            
    
        
def DisplayEnemies():
    print('Level     Name')
    print
    enemylist = []
    for i in Enemies.stats:
        enemylevel = Enemies.stats[i][0]
        enemylist.append([(enemylevel),(' ' + str(enemylevel) + ((9-len(str(enemylevel))) * ' ') + i[0].upper() + i[1:])])
    enemylist.sort()
    for i in enemylist:
        print(i[1])
                
def Tutorial():
    print('This is a full explanation of all the game and its functions')
    print('Type a number to learn about that subject')
    print('1. Saving and Loading Player Files')
    print('2. Fighting')
    print('3. Food and Potions')
    print('4. Commands List')
    print('Type \'exit\' to exit the tutorial')
    choice = ''
    print choice
    while not choice == 'exit':
        choice = raw_input('    >>')
        if choice == '1':
            print('When you start up the game, it will ask you for a file name')
            print('If you enter a new file name, then enter \'new\' at the propmt')
            print('This will create a new text file in the folder with this game')
            print('To load a game, enter the file name of a game that has already been played and saved')
            print('Then, don\'t enter new, just press the enter key')
            print('This way, you may store several different players')
            print('Type \'exit\' to exit the tutorial')
        if choice == '2':
            print('To fight an enemy, enter \'battle\'')
            print('You will see this:')
            print('    >>')
            print('Enter the name of the enemy you wish to fight')
            print('Then the battle will start and you will fight the enemy')
            print('If you lose, you will not gain XP or items')
            print('If you win, you will gain XP, along with items dropped by the enemy')
            print('Type \'exit\' to exit the tutorial')
        if choice == '3':
            print('To eat or drink an item, enter \'eat\' or \'drink\'\n')
            print('You will see this:')
            print('    >>')
            print('Enter the item you wish to consume')
            print('Then the item will disapear from your inventory, and you will gain health')
            print
            print("You can also eat all of a certain item until you run out of that item, or you have max HP")
            print("To do this, type \'eat\'")
            print("Like before, you will see this:")
            print('    >>')
            print("Enter \'all\'")
            print("Then you will eat that item until you have max HP")
            print('Type \'exit\' to exit the tutorial')
        if choice == '4':
            print("'exit': exits the game")
            print("'save': saves the game")
            print("'battle': type the name of the enemy you want to fight at the prompt")
            print("'enemies': lists all the enemies and their levels")
            print("'eat': type the item you want to eat at the prompt")
            print("'drink': type the item you want to drink at the prompt")
            print("'help': displays help")
            print("'inv': displays items in inventory")
            print("'def': displays your defense")
            print("'att': displays your attack")
            print("'hp: displays your current HP and max HP")
            print("'xp': displays your xp, next level xp, and xp need to reach the next level")
            print("'lvl': displays your current level")
            print("'version': displays the current version of the game")
            print("'stats': displays all your stats")
            print('Type \'exit\' to exit the tutorial')
            # These commands make it easier to test individual functions of the game
            
        
def Credits():
    print '____________ _____   '
    time.sleep(.3)
    print '| ___ \ ___ \  __ \  '
    time.sleep(.3)
    print '| |_/ / |_/ / |  \/  '
    time.sleep(.3)
    print '|    /|  __/| | __   '
    time.sleep(.3)
    print '| |\ \| |   | |_\ \  '
    time.sleep(.3)
    print '\_| \_\_|    \____/  '
    time.sleep(.3)
    print('Based on an idea by Wigglesniff at\nhttp://www.dreamincode.net/forums/topic/243936-rpg-in-python/')
    time.sleep(1)
    print('ASCII Art Font by http://patorjk.com/software/taag/#p=display&f=Doom&t=RPG')
    time.sleep(1)
    print('Coded in Python 2.7.7 by Jayden Wilhelm')


def RunGame():
    player = LoadPlayer()
    print('If you need help at any time, type \'help\'.')
    menu = Menu()
    menu.RunMenu(player)
    
RunGame()


