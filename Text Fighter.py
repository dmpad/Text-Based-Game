#David Padalino     RNG Text-Based Fantasy Fighter
import time
import random
import math

items = [0, 0, 0, 0]    # health poitons = 0, gold = 1, roid = 2, tome = 3
lvls = (1, 1, 1)        # magic = 0, sword = 1, armor = 2
player = {'health' : [100, 100]}   #current health = 0,0, max health = 0,1
NAMES = ['orc', 'evil rabbit', 'tree fariy', 'rabbid owl', 'tree ent', 'baby dragon', 'golem guard', 'gremlin maid', 'sandman', 'pixie sourcerer', 'goblin spellcaster', 'mimic', 'spawned dragon hatchling', 'dragon', 'two headed dragon'] #0-3 = path, 4 = tree, 5-11 = castle
STATS = [['melee', 1, 1, 22], ['melee', 1, 0, 28], ['magic', 1, 0, 26], ['melee', 1, 2, 24], ['melee', 4, 2, 60], ['magic', 3, 3, 40], ['melee', 4, 4, 42], ['melee', 6, 3, 32], ['melee', 4, 2, 40], ['magic', 4, 0, 33], ['magic', 3, 2, 39], ['melee', 7, 5, 45], ['melee', 3, 3, 40], ['magic', 6, 5, 70], ['magic', 7, 8, 100]] #(attack type, attack strength, defense, health)
baseSDmg = 3.8
baseMDmg = 3.6

count = 0

def map():
    global count
    count += 1
    if count <= 8:
        print ('You continue down the beaten dirt path.')
        time.sleep(2)
        enemy = monsters('path')
        return enemy
    else:
        if count == 9:
            time.sleep(2)
            enemy = monsters('tree')
            return enemy
        else:
            if count == 10:
                print('You walk up to the ancient castle gates and break them open with ease.')
                print('However as you walk in you hear a commotion and various creatures yelling')
                print('"Get to the gates!", the door must have been enchanted and alerted every')
                print('creature within the castle.')
                time.sleep(2)
                return False
            else:
                if count > 10 and count < 25:
                    roll = random.randint(1, 10) #allowing for varience in castle rooms in later builds of the code
                    if roll <= 3:
                        print('You walk onward through a hallway in search for the tower steps')
                        time.sleep(2)
                        enemy = monsters('hallway')
                    if roll >3 and roll <= 6:
                        print('You walk onward into a small bedroom with creaky floors, torn curtains, and')
                        print('a perfectly kept bed in the center.')
                        time.sleep(2)
                        enemy = monsters('bedroom')
                    if roll >6 and roll <= 9:
                        print('You stumble into a room containing a chair, 5 candles, and filled bookshelves')
                        print('along all of the walls. You wonder "How many books does this mage have?!?"')
                        time.sleep(2)
                        enemy = monsters('bookroom')
                    if roll == 10:
                        print('You come upon a room guilded in gold and a chest in the center covered in jewels')
                        time.sleep(2)
                        enemy = monsters('chestroom')
                    return enemy
                else:
                    if count == 25:
                        enemy = boss1()
                        return enemy
                    else:
                        if count == 26:
                            enemy = boss2()
                            return enemy
                        else:
                            if count == 27:
                                enemy = boss3()
                                return enemy

class monsters(object):

    global NAMES
    global STATS
    global count

    def __init__(self, location):
        if location == 'path':
            enemy = random.randint(0, 3)
            self.name = NAMES[enemy]
            self.stats = STATS[enemy][:]
            print('You have run into a ' + self.name + '!"')
            print(self.stats)
            time.sleep(1)
        else:
            if location == 'tree':
                print('As you walk upto the old and twisted tree you see it move as')
                time.sleep(2)
                print('you realize it is a giant tree ent. The ent looks down at you')
                print("and you notice the brown leaves on its branches shaking. You")
                print("then dodge the enraged ent's branch as it forcefully swings")
                print('one of its large branches at you.')
                self.name = NAMES[4]
                self.stats = STATS[4][:]
                print('You are now fighting the ' + self.name + '!!!')
                print(self.stats)
                time.sleep(1)
            else:
                if location == 'hallway':
                    enemy = random.randint(5, 6)
                    self.name = NAMES[enemy]
                    self.stats = STATS[enemy][:]
                    print('You have walked into the sights of a ' + self.name + '!"')
                    print(self.stats)
                    time.sleep(1)
                if location == 'bedroom':
                    enemy = random.randint(7, 8)
                    self.name = NAMES[enemy]
                    self.stats = STATS[enemy][:]
                    print('You have been attacked by a ' + self.name + '!"')
                    print(self.stats)
                    time.sleep(1)
                if location == 'bookroom':
                    enemy = random.randint(9, 10)
                    self.name = NAMES[enemy]
                    self.stats = STATS[enemy][:]
                    print('A magical being called ' + self.name + ' has spotted you!"')
                    print(self.stats)
                    time.sleep(1)
                if location == 'chestroom':
                    roll = random.randint(1, 10)
                    if roll <= 4:
                        self.name = NAMES[11]
                        self.stats = STATS[11][:]
                        print('You have been attacked by a ' + self.name + '!"')
                        print(self.stats)
                        time.sleep(1)
                    else:
                        self.name = 'Chest'
                        self.stats = ['melee', 0, 0, 0]
                        print('You discovered a chest with loot in it!')
                    time.sleep(1)
                if location == 'boss1':
                    self.name = NAMES[12]
                    self.stats = STATS[12]
                if location == 'boss2':
                    self.name = NAMES[13]
                    self.stats = STATS[13]
                if location == 'boss3':
                    self.name = NAMES[14]
                    self.stats = STATS[14]
        if location == 'NA':
            self.name = 'NA'
            self.stats = ['none', 0, 0, 0]

    def drop(self):
        if count <= 8:
            roll = random.randint(1, 10)
            if roll <= 5:
                amount = int(math.ceil(roll * 0.5))
                actions('potion', amount, self)
            roll = random.randint(1, 10)
            if roll <= 2:
                amount = 1
                levels('magic', amount)
            if roll > 2 and roll <= 4:
                amount = 1
                levels('sword', amount)
            if roll > 4 and roll <= 6:
                amount = 1
                levels('armor', amount)
            amount = random.randint(50, 150)
            actions('gold', amount, self)
            
        if count == 9:
            levels('sword', 1)
            levels('magic', 1)
            levels('armor', 1)
            actions('gold', 350, self)

        if count > 9 and count < 25:
            if self.name == 'chest':
                roll = random.randint(1, 10)
                if roll >= 5:
                    amount = (roll * 0.5)
                    actions('addRoid', amount, self)
                else:
                    amount = ((roll - 5) * 0.5)
                    actions('addTome', amount, self)
                roll = random.randint(1, 2)
                if roll == 1:
                    actions('gold', 500, self)
                else:
                    actions('gold', 650, self)
            else:
                if self.name == NAMES[8] or self.name == NAMES[9]:
                    roll = random.randint(1, 10)
                    if roll <= 6:
                        actions('addTome', 1, self)
                else:
                    roll = random.randint(1, 10)
                    if roll <= 2:
                        actions('addTome', 1, self)
                    if roll >2 and roll <= 4:
                        actions('addRoid', 1, self)
                        
                    roll = random.randint(1, 10)
                    if roll <= 3:
                        amount = 1
                    else:
                        if roll > 3 and roll < 5:
                            amount = 2
                            actions('potion', amount, self)
                        
                amount = random.randint(250, 499)
                actions('gold', amount, self)
        if count == 25:
            actions('potion', 3, self)
            actions('gold', 750, self)
        if count == 26:
            actions('potion', 4, self)
            actions('gold', 1000, self)
        if count == 27:
            actions('potion', 4, self)
            actions('gold', 1400, self)
                    
def combat(monster):
    roll = random.randint(1, 10)
    if roll <= 2:
        amount = 1.25
    else:
        amount = 1.0
        
    if monster.stats[0] == 'melee':
        player['health'][0] = int(player['health'][0] - (float(baseSDmg * monster.stats[1] * amount))-(float(baseSDmg * monster.stats[1])* (lvls[2] * 0.07)))
    if monster.stats[0] == 'magic':
        player['health'][0] = math.floor(float(player['health'][0]) - float(baseMDmg * monster.stats[1] * amount) -(float(baseMDmg * monster.stats[1])* (lvls[2] * 0.06)))

    print('Your health is at ' + (str(player['health'][0])) +' hp.')

def actions(action, amount, monster):
    global items

    if action == 'heal':
        if items[0] > 0:
            items[0] -= 1
            player['health'][0] += int(player['health'][1]*0.2)
            if player['health'][0] > player['health'][1]:
                player['health'][0] = player['health'][1]
        else:
            print ('No health potions available')
    if action == 'swing':
        monster.stats[3] = int(monster.stats[3] - ((float(baseSDmg * lvls[1] * amount))-((float(baseSDmg * lvls[1]))* (monster.stats[2] * 0.07))))
        print(monster.name + ' has ' + (str(monster.stats[3])) + 'hp.')
    if action == 'cast':
        monster.stats[3] = math.floor(float(monster.stats[3]) - float(baseMDmg * lvls[0] * amount) -(float(baseMDmg * lvls[1])* (monster.stats[2] * 0.06)))
        print(monster.name + ' has ' + (str(monster.stats[3])) + 'hp.')
    if action == 'potion':
        items[0] += amount
        print('you gained ' + (str(amount)) + ' potion(s)!')
    if action == 'gold':
        items[1] += amount
        print('you gained ' + (str(amount)) + ' gold!')
    if action == 'die':
        print('You have died, your gold was at ' + (str(items[1])) + '.')
        items[1] -= (items[1]*0.2)
        print('Now your gold is at ' + (str((int(items[1])))) + ' and your health is fully restored.')
    if action == 'addRoid':
        items[2] += amount
        print('you gained ' + (str(amount)) + ' roid(s)!')
    if action == 'addTome':
        items[3] += amount
        print('you gained ' + (str(amount)) + ' tome(s)!')
    if action == 'roid':
        items[2] -= amount
        levels('roid', amount)
    if action == 'tome':
        items[3] -= amount
        levels('tome', amount)
        
    items[1] = int(items[1])
    

def levels(value, amount):
    global lvls
    magic = lvls[0]
    sword = lvls[1]
    armor = lvls[2]
    
    if value == 'magic':
        magic += amount
        print('you went up ' + (str(amount)) + ' in magic!')
    else:
        if value == 'sword':
            sword += amount
            print('you went up ' + (str(amount)) + ' in swordskills!')
        else:
            if value == 'armor':
                armor += amount
                print('you went up ' + (str(amount)) + ' in armor!')

    if value == 'roid':
        sword += (amount * 2)
        armor += (amount * 2)
        magic -= amount

    if value == 'tome':
        magic += (amount * 2)
        sword -= amount
        armor -= amount

    del lvls
    lvls = (magic, sword, armor)

def story():
    print('You wake up in the log cabin you stayed the night in.')
    time.sleep(1)
    print('You gather your things and set off onto the path through')
    print('the woods towards the large gothic castle to defeat the')
    print('evil dragon mage while collecting loot on the way.')
    print('press enter to continue')
    ans = input()

def boss1():
    print('You find a staircase leading to the top of the tower!')
    print('Upon reaching the top of the tower you encounter the dragon')
    print('mage. She says "you have come far, but can you truely stop me!"')
    print('The mage starts by summoning a baby dragon.')
    enemy = monsters('boss1')
    return enemy

def boss2():
    print('The dragon mage starts to become enraged from seeing')
    print('her baby dragon die. She then says "you will pay!"')
    print('The dragon mage now summons a fully grown dragon!')
    enemy = monsters('boss2')
    return enemy

def boss3():
    print('Seeing the defeat of the dragon mage screams "I will')
    print('end you!" after she says this she chants "rik la zil!')
    print('She then suddenly transforms into a massive 2 headed dragon!')
    enemy = monsters('boss3')
    return enemy

def main():
    gameOn = True
    story()
    while(gameOn == True):
        print('Your stats are magic: ' + (str(lvls[0])) + ', swordskill: ' + (str(lvls[1])) + ', armor: ' + (str(lvls[2])))
        print('Your inventory currently holds ' + (str(items[0])) + ' potions, ' + (str(items[2])) + ' roids, ' + (str(items[3])) + ' tomes, and ' + (str(items[1])) + ' gold.')
        print('What do you do?')
        time.sleep(1)
        print('"walk forward", "heal", "tome", "roid", "end game"')
        time.sleep(1)
        decision = input()
        check = True
        while(check == True):
            if decision == 'walk forward':
                enemy = map()
                if enemy != False:
                    fight = True
                    while enemy.stats[3] > 0 and fight == True:
                        print('Choose an action:')
                        time.sleep(1)
                        if items[0] > 0:
                            print('"swing", "cast", "heal", "run"')
                        else:
                            print('"swing", "cast", "run"')
                        action = input()
                        if action == 'swing' or action == 'cast':
                            crit = random.randint(1, 5)
                            if crit < 5:
                                actions(action, 1, enemy)
                            else:
                                actions(action, 1.25, enemy)
                            if enemy.stats[3] > 0:
                                combat(enemy)
                        else:
                            if action == 'heal':
                                actions(action, 0, enemy)
                                combat(enemy)
                            if action == 'run':
                                if enemy.name ==  NAMES[4] or enemy.name == 'spawned dragon hatchling' or enemy.name == 'dragon' or enemy.name == 'two headed dragon':
                                    print('You attempt to escape but are unable to leave.')
                                else:
                                    check = False
                                    fight = False

                        if player['health'][0] <= 0:
                            actions('die', 0, enemy)
                            player['health'][0] = player['health'][1]
                    check = False
                    if enemy.stats[3] <= 0:
                        enemy.drop()
                        if enemy.name == 'two headed dragon':
                            print('You have defeated the dragon mage!')
                            time.sleep(1)
                            print('The mage turnes back into a person as her power leaves her.')
                            print('Your quest is complete!')
                            gameOn = False
            else:
                if decision == 'end game':
                    gameOn = False
                else:
                    if decision == 'heal' and items[0] > 0:
                        enemy = monsters('NA')
                        actions(decision, 1, enemy)
                        print('Your health has been healed up to ' + (str(player['health'][0])) + '.')
                    else:
                        if decision == 'roid' and items[2] > 0:
                            enemy = monsters('NA')
                            actions(decision, 1, enemy)
                        else:
                            if decision == 'tome' and items[3] > 0:
                                enemy = monsters('NA')
                                actions(decision, 1, enemy)
                check = False
    print('Your final gold is ' + (str(items[1])) + '.')
                    
            
main()
