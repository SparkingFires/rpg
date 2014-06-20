# TO DO
#
# Add Shop
# Create Campagin

import random
import time
import string

time.sleep(.3)
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

version = 1.0
print 'Version ' + str(version)

class Player:
    
    def __init__(self):
        self.SaveFileName = raw_input("Enter File Name\n>> ")
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
        line = ' '.join(str(i) for i in (stats))
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
        print "Player saved!"
        
    def DisplayStats(self):
        print('Level      : ' + str(self.level))
        print('XP         : ' + str(self.xp))
        print('Next Level : ' + str(100 * self.level * (self.level)))
        print()
        print('Attack     : ' + str(self.attack))
        print('Defense    : ' + str(self.defense))
        print()
        print('Max HP     : ' + str(self.maxhp))
        print('Curent HP  : ' + str(self.hp))
    
    def Battle(self):
        name = raw_input('    >>')
        xpgain = 0
        if name in Enemies.stats:
            enemy = Enemies(name[0].upper() + name[1:], Enemies.stats[name][1], Enemies.stats[name][2], Enemies.stats[name][3], Enemies.drops[name])
            print (enemy.name) + ':' + str(enemy.hp) 
            print()
            while enemy.hp>0 and self.hp>0:
                
                randomatt = random.randint(1, 6) + (enemy.attack)
                randomdef = random.randint(1, 6) + (self.defense)
                if randomatt > randomdef:
                    self.hp = self.hp - (randomatt - randomdef)
                else:
                    xpgain = xpgain + random.randint(enemy.attack + randomdef - randomatt + 1, enemy.attack + randomdef - randomatt + 1) - self.defense
                
                randomatt = random.randint(1, 6) + (self.attack)
                randomdef = random.randint(1, 6) + (enemy.defense)
                if randomatt > randomdef:
                    enemy.hp = enemy.hp - (randomatt - randomdef)
                    xpgain = xpgain + random.randint(enemy.defense + randomatt - randomdef - 1, enemy.defense + randomatt - randomdef + 1) - self.attack
                    
                time.sleep(0.3)
                print('Player:' + str(max(0,self.hp)))
                print(enemy.name.title() + ':' + str(max(0,enemy.hp)))
                print ()
            if self.hp<=0:
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
                print ("You are now level {0}").format(self.level)
                
    def Eat(self):
        fooditem = raw_input('    >>')
        foodlist = Food()
        if fooditem in foodlist.food and fooditem in self.items:
            prevhp = self.hp
            foodhp = (foodlist.food[fooditem])
            self.hp = self.hp + foodhp
            self.items[fooditem] = self.items[fooditem] - 1
            if self.hp > self.maxhp:
                self.hp = self.maxhp
                print 'You have max HP now'
            else:
                print 'You ate ' + str(fooditem) + ' and healed ' + str(foodhp) + ' HP'
            print 'Your health is now ' + str(self.hp)
        else:
            print 'You can\'t eat that'
                
    def Drink(self):
        drinkitem = raw_input('    >>')
        potionlist = Potion()
        if drinkitem in potionlist.potion and drinkitem in self.items:
            prevhp = self.hp
            drinkhp = (potionlist.potion[drinkitem])
            self.hp = self.hp + drinkhp
            self.items[drinkitem] = self.items[drinkitem] - 1
            if self.hp > self.maxhp:
                self.hp = self.maxhp
                print 'You have max HP now'
            else:
                print 'You drank a ' + str(drinkitem) + ' and healed ' + str(drinkhp) + ' HP'
            print 'Your health is now ' + str(self.hp)
        else:
            print 'You can\'t drink that'
        
            

class Enemies():

    stats = {} # lvl A D HP
    stats['goblin'] = [1, 1, 1, 15]
    stats['spider'] = [7, 5, 8, 40]
    stats['hobgoblin'] = [2, 2, 2, 17]
    stats['imp'] = [4,3,1,21]
    stats['lizardfolk'] = [4, 5, 3, 25]
    stats['kobold'] = [6, 6, 7, 35]
    stats['gargoyle'] = [11, 16, 15, 51]
    stats['skeleton'] = [12, 9, 14, 67]
    stats['troll'] = [14, 14, 16, 70]
    stats['vampire'] = [16, 20, 12, 60]
    stats['orc'] = [19, 21, 16, 75]
    stats['orge'] = [25, 25, 27, 97]
    stats['golem'] = [30, 23, 38, 90]
    stats['basilisk'] = [34, 35, 37, 82]
    stats['manticore'] = [47, 50, 45, 110]
    stats['minotaur'] = [55, 56, 55, 130]
    stats['wizard'] = [61, 65, 68, 150]
    stats['elemental'] = [67, 70, 75, 200]
    stats['dragon'] = [72, 77, 77, 400]
    stats['serpent'] = [84, 88, 85, 550]
    stats['wyvern'] = [87, 89, 91, 650]
    stats['hydra'] = [93, 94, 93, 750]
    stats['phoenix'] = [100, 100, 100, 1000]
    drops = {} # % chance, how many, out of how many
    drops['goblin'] = [['gold', 100, 1, 15],['fish', 40, 1, 1]]
    drops['spider'] = [['gold', 10, 5, 10],['healthpotion', 50, 1, 2]]
    drops['hobgoblin'] = [['gold',100, 1, 12],['meat',50,1,2]]
    drops['imp'] = [['gold',100, 1,10],['bread',50,1,1],['healthpotion',25,1,1],['meat',60,1,3]]
    drops['lizardfolk'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['kobold'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['gargoyle'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['skeleton'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['troll'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['vampire'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['orc'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['giant'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['orge'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['golem'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['basilisk'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['manticore'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['minotaur'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['wizard'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['elemental'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['dragon'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['serpent'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['wyvern'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['hydra'] = [['gold', 100, 1, 10], ['meat', 50, 1, 2]]
    drops['phoenix'] = [['firerod', 100, 1, 1], ['you win', 100, 1, 1]]
    
    def __init__(self,name,attack,defense,hp,drops):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.drops = drops
        
        

class Food():
    
    def __init__(self):
        self.food = {}
        self.food['fish'] = 3
        self.food['meat'] = 5
        self.food['bread'] = 2
        
class Potion():
    
    def __init__(self):
        self.potion = {}
        self.potion['healthpotion'] = 10
    
  
def LoadPlayer():
    player = Player()
    choice = raw_input('Enter \'new\' for a new player or press enter to load this player\n>> ')
    if choice == 'new':
        player.New()
        player.stats = player.Load()
    else:
        player.stats = player.Load()
    return player
    

        
class Menu():
    
    def RunMenu(self, player):
        choice = ''
        print choice
        while not choice == 'exit':
            choice = raw_input('>>')
            if choice == 'save':
                player.Save()
            if choice == 'help':
                newHelp = self.Help()
                newHelp.RunHelp()
            if choice == 'stats':
                player.DisplayStats()
            if choice == 'battle':
                player.Battle()
            if choice == 'eat':
                player.Eat()
            if choice == 'drink':
                player.Drink()
            if choice == 'inv':
                print str(player.items)
            if choice == 'enemies':
                DisplayEnemies()
            if choice == 'hp':
                print ('Your current HP is ' + str(player.hp))
            if choice == 'maxhp':
                print ('Your max HP is ' + str(player.maxhp))
            if choice == 'att':
                print ('Your attack is ' + str(player.attack))
            if choice == 'def':
                print ('Your defense is ' + str(player.defense))
            if choice == 'xp':
                print ('You have ' + str(player.xp) + ' XP')
            if choice in player.items:
                print(choice + '(' + str(player.items[choice]) + ')')
                

    class Help():
        
        def RunHelp(self):
            print('To fight, enter \'battle\' followed by enemy name. For the list of enemies, enter \'enemies\'.')
            print('To quit the game, enter \'exit\', but remeber to save using \'save\' first!')
            print('You may eat or drink an item by typing \'eat\' or \'drink\', then typing the item\'s name')
            print('For a more complex explanation of the game, type \'help\' below.')
            print('To view the credits, type \'credits\' below')
            choice = raw_input('    >>')
            if choice == 'enemies':
                DisplayEnemies()
            if choice == 'help':
                ComplexHelp()
            if choice == 'credits':
                Credits()
            
    
        
def DisplayEnemies():
    print('Level   Name')
    print()
    enemylist = []
    for i in Enemies.stats:
        enemylevel = Enemies.stats[i][0]
        enemylist.append([(enemylevel),(' ' + str(enemylevel) + ((9-len(str(enemylevel))) * ' ') + i[0].upper() + i[1:])])
    enemylist.sort()
    for i in enemylist:
        print(i[1])
                
def ComplexHelp():
    print('This is a full explanation of all the game and its functions')
    print('Type a number to learn about that subject')
    print('1. Saving and Loading Player Files')
    print('2. Fighting')
    print('3. Food and Potions')
    print('4. Commands')
    print('Type \'exit\' to exit')
    choice = ''
    print choice
    while not choice == 'exit':
        choice = raw_input('>>')
        if choice == '1':
            print('When you start up the game, it will ask you for a file name')
            print('If you enter a new file name, then enter \'new\' at the propmt')
            print('This will create a new text file in the folder with this game')
            print('To load a game, enter the file name of a game that has already been played and saved')
            print('Then, don\'t enter new, just press the enter key')
            print('This way, you may store several different players')
        if choice == '2':
            print('To fight an enemy, type \'battle\'')
            print('You will see this:')
            print('    >>')
            print('Enter the name of the enemy you wish to fight')
            print('Then the battle will start and you will fight the enemy')
            print('If you lose, you will not gain XP or items')
            print('If you win, you will gain XP, along with items dropped by the enemy')
        if choice == '3':
            print('To eat or drink an item, enter \'eat\' or \'drink\'\n')
            print('You will see this:')
            print('    >>')
            print('Enter the food item you wish to eat')
            print('The item will disapear from your inventory, and you will gain health')
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
            print("'hp: displays your current HP")
            print("'maxhp': displays your max HP")
            print("'xp': displays your max HP")
            
        
def Credits():
    print('Coded in Python 2.7.7 by Jayden Wilhelm')
    print('Based on an idea by Wigglesniff at\nhttp://www.dreamincode.net/forums/topic/243936-rpg-in-python/')
    

def RunGame():
    player = LoadPlayer()
    print('If you need help at any time, type \'help\'.')
    menu = Menu()
    menu.RunMenu(player)
    
RunGame()
                
        
        
