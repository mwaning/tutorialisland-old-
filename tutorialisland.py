import time
sleepshort = 0 #1
sleepmedium = 0 #1.5
sleeplong = 0 #2

print("----------------------------------------------------\n** RuneScape Tutorial Island Text Based Simulator **\n----------------------------------------------------\n") ; time.sleep(sleepshort)
print("Tips: option [1] is 99 percent of the time the option you need to progress. ")
print("Known issues: If you Return more than once the options menus will bug.\n")
player = input("Please enter a username.\n: ") ; time.sleep(sleepshort)

#Stats
level = ("1")
xp = ("0/100")
hp = ("25/25")
stats = (f"\n*Stats*\nLVL {level}\nXP {xp}\nHP {hp}\n")

#Equipment
equipment_head = ("empty")
equipment_cape = ("empty")
equipment_neck = ("empty")
equipment_ammunition = ("empty")
equipment_weapon = ("empty")
equipment_shield = ("empty")
equipment_body = ("empty")
equipment_legs = ("empty")
equipment_hands = ("empty")
equipment_feet = ("empty")
equipment_ring = ("empty")
equipment = (f"\n*Equipment*\nFirst Hand: {equipment_weapon}\nSecond Hand: {equipment_shield}\nAmmo: {equipment_ammunition}\nHead: {equipment_head}\nCape: {equipment_cape}\nNeck: {equipment_neck}\nChest: {equipment_body}\nLegs: {equipment_legs}\nHands: {equipment_hands}\nFeet: {equipment_feet}\nRing: {equipment_ring}\n")

#Inventory
inventory_1 = ("empty")
inventory_2 = ("empty")
inventory_3 = ("empty")
inventory_4 = ("empty")
inventory_5 = ("empty")
inventory_6 = ("empty")
inventory_7 = ("empty")
inventory_8 = ("empty")
inventory_9 = ("empty")
inventory_10 = ("empty")
inventory_11 = ("empty")
inventory_12 = ("empty")
inventory_13 = ("empty")
inventory_14 = ("empty")
inventory_15 = ("empty")
inventory_16 = ("empty")
inventory_17 = ("empty")
inventory_18 = ("empty")
inventory_19 = ("empty")
inventory_20 = ("empty")
inventory_21 = ("empty")
inventory_22 = ("empty")
inventory_23 = ("empty")
inventory_24 = ("empty")
inventory_25 = ("empty")
inventory_26 = ("empty")
inventory_27 = ("empty")
inventory_28 = ("empty")
inventory = (f"\n*Inventory*\n{inventory_1}\n{inventory_2}\n{inventory_3}\n{inventory_4}\n{inventory_5}\n{inventory_6}\n{inventory_7}\n{inventory_8}\n{inventory_9}\n{inventory_9}\n{inventory_10}\n{inventory_11}\n{inventory_12}\n{inventory_13}\n{inventory_14}\n{inventory_15}\n{inventory_16}\n{inventory_17}\n{inventory_18}\n{inventory_19}\n{inventory_20}\n{inventory_21}\n{inventory_22}\n{inventory_23}\n{inventory_24}\n{inventory_25}\n{inventory_26}\n{inventory_27}\n{inventory_28}\n")

print(f"\nWelcome, {player}!") ; time.sleep(sleepmedium)

print("* phasing you into the world *\n") ; time.sleep(sleeplong)

print("You find yourself in a small library like house with brick stone walls and a wooden framework.\nNot too far away from you there's a guy named Runescape Guide.\n") ; time.sleep(sleepmedium)

def scene_1():
    option_1 = input("Options 1\n[1] Talk to RuneScape Guide  [s] Stats\n[2] Examine Runescape Guide  [e] Equipment\n[3] Do nothing               [i] Inventory\n: ")
    if (option_1 == "1"):
            print(f"\n  <RuneScape Guide>\n> Greetings {player}! I see you are a new arrival to this land.\n> My job is to welcome all new visitors. So, welcome!\n> You have already learned the first thing needed to succeed in this world: talking to other people!\n> You will find many inhabitants of this world have useful things to say to you.\n> To continue the tutorial, go through that door over there and speak to your first instructor!")
            print("\nThe RuneScape Guide kindly opens the door for you...\n")
    elif (option_1 == "2"):
            print("\nYour introduction to the world of RuneScape.\n")
            return scene_1()
    elif (option_1 == "3"):
            print("\nThe RuneScape Guide patiently waits for you.\n")
            return scene_1()
    elif option_1 in ("s", "S"):
            print(f"\n*Stats*\nLVL {level}\nXP {xp}\nHP {hp}\n")
            return scene_1()
    elif option_1 in ("e", "E"):
            print(f"\n*Equipment*\nFirst Hand: {equipment_weapon}\nSecond Hand: {equipment_shield}\nAmmo: {equipment_ammunition}\nHead: {equipment_head}\nCape: {equipment_cape}\nNeck: {equipment_neck}\nChest: {equipment_body}\nLegs: {equipment_legs}\nHands: {equipment_hands}\nFeet: {equipment_feet}\nRing: {equipment_ring}\n")
            return scene_1()
    elif option_1 in ("i", "I"):
            print(f"\n*Inventory*\n{inventory_1}\n{inventory_2}\n{inventory_3}\n{inventory_4}\n{inventory_5}\n{inventory_6}\n{inventory_7}\n{inventory_8}\n{inventory_9}\n{inventory_9}\n{inventory_10}\n{inventory_11}\n{inventory_12}\n{inventory_13}\n{inventory_14}\n{inventory_15}\n{inventory_16}\n{inventory_17}\n{inventory_18}\n{inventory_19}\n{inventory_20}\n{inventory_21}\n{inventory_22}\n{inventory_23}\n{inventory_24}\n{inventory_25}\n{inventory_26}\n{inventory_27}\n{inventory_28}\n")
            return scene_1()
    else:
            print("\nOption not available. Try again.\n")
            return scene_1()
scene_1()

def scene_1_1():
    option_1_1 = input("Options 1.1\n[1] Go outside    [s] Stats\n[2] Examine Door  [e] Equipment\n[3] Do nothing    [i] Inventory\n: ")
    if (option_1_1 == "1"):
            print("\nYou walk through the door...\n")
    elif (option_1_1 == "2"):
            print("\nA nicely fitted door.\n")
            return scene_1_1()
    elif (option_1_1 == "3"):
            print("\nThe Runescape Guide is hinting at you to leave the building.\n")
            return scene_1_1()
    elif option_1_1 in ("s", "S"):
            print(f"\n*Stats*\nLVL {level}\nXP {xp}\nHP {hp}\n")
            return scene_1_1()
    elif option_1_1 in ("e", "E"):
            print(f"\n*Equipment*\nFirst Hand: {equipment_weapon}\nSecond Hand: {equipment_shield}\nAmmo: {equipment_ammunition}\nHead: {equipment_head}\nCape: {equipment_cape}\nNeck: {equipment_neck}\nChest: {equipment_body}\nLegs: {equipment_legs}\nHands: {equipment_hands}\nFeet: {equipment_feet}\nRing: {equipment_ring}\n")
            return scene_1_1()
    elif option_1_1 in ("i", "I"):
            print(f"\n*Inventory*\n{inventory_1}\n{inventory_2}\n{inventory_3}\n{inventory_4}\n{inventory_5}\n{inventory_6}\n{inventory_7}\n{inventory_8}\n{inventory_9}\n{inventory_9}\n{inventory_10}\n{inventory_11}\n{inventory_12}\n{inventory_13}\n{inventory_14}\n{inventory_15}\n{inventory_16}\n{inventory_17}\n{inventory_18}\n{inventory_19}\n{inventory_20}\n{inventory_21}\n{inventory_22}\n{inventory_23}\n{inventory_24}\n{inventory_25}\n{inventory_26}\n{inventory_27}\n{inventory_28}\n")
            return scene_1_1()
    else:
            print("\nOption not available. Try again.\n")
            return scene_1_1()
scene_1_1()

time.sleep(sleepmedium)
print("As you step outside, you notice that the building is based on top of a hill overlooking the rest of the area.\nAround you there's grass, trees, blue flowers, and a small stairway ending in a path leading to your next objective.\nThe area is surrounded by fences. Surely they are afraid newcomes would get lost?\n")

def scene_2():
    option_2 = input("Options 2\n[1] Follow the path  [s] Stats\n[2] Examine Tree     [e] Equipment\n[3] Examine Flowers  [i] Inventory\n[4] Stay here\n: ")
    if (option_2 == "1"):
        print("\nYou climb down the small stairway and continue down the path.\n")
    elif (option_2 == "2"):
        print("\nA beautiful old oak.\n")
        return scene_2()
    elif (option_2 == "3"):
        print("\nYou don't see too many of these. I wonder what these are?\n")
        return scene_2()
    elif (option_2 == "4"):
        print("\nYou stay in place. You take a deep breath and enjoy the surroundings for a minute.\n")
        return scene_2()
    elif option_2 in ("s", "S"):
        print(f"\n*Stats*\nLVL {level}\nXP {xp}\nHP {hp}\n")
        return scene_2()
    elif option_2 in ("e", "E"):
        print(f"\n*Equipment*\nFirst Hand: {equipment_weapon}\nSecond Hand: {equipment_shield}\nAmmo: {equipment_ammunition}\nHead: {equipment_head}\nCape: {equipment_cape}\nNeck: {equipment_neck}\nChest: {equipment_body}\nLegs: {equipment_legs}\nHands: {equipment_hands}\nFeet: {equipment_feet}\nRing: {equipment_ring}\n")
        return scene_2()
    elif option_2 in ("i", "I"):
        print(f"\n*Inventory*\n{inventory_1}\n{inventory_2}\n{inventory_3}\n{inventory_4}\n{inventory_5}\n{inventory_6}\n{inventory_7}\n{inventory_8}\n{inventory_9}\n{inventory_9}\n{inventory_10}\n{inventory_11}\n{inventory_12}\n{inventory_13}\n{inventory_14}\n{inventory_15}\n{inventory_16}\n{inventory_17}\n{inventory_18}\n{inventory_19}\n{inventory_20}\n{inventory_21}\n{inventory_22}\n{inventory_23}\n{inventory_24}\n{inventory_25}\n{inventory_26}\n{inventory_27}\n{inventory_28}\n")
        return scene_2()
    else:
        print("\nOption not available. Try again.\n")
        return scene_2()
scene_2()

time.sleep(sleepmedium)
print("In the distance you see a lady standing by a pond surrounded by trees. She must be the next instructor.") ; time.sleep(sleepmedium)
print("You walk up to her.\n") ; time.sleep(sleepmedium)

def scene_3():
    option_3 = input("Options 3\n[1] Talk to Survival Expert  [s] Stats\n[2] Examine Survival Expert  [e] Equipment\n[3] Do nothing               [i] Inventory\n: ")
    if (option_3 == "1"):
        print("\n  <Survival Expert>\n> Hello there, newcomer. My name is Brynna.\n> My job is to teach you a few survival tips and tricks.\n> First off we're going to start with the most basic survival skill of all: making a fire.\n> To start off, here's an axe you can use to chop down the tree next to you. And a tinderbox to light the logs on fire.\n")
    elif (option_3 == "2"):
        print("\nVery much an outdoors type.\n")
        return scene_3()
    elif (option_3 == "3"):
        print("\n\n  <Survival Expert>\n> Were you sent here to see me?\n")
        return scene_3()
    elif option_3 in ("s", "S"):
        print(f"\n*Stats*\nLVL {level}\nXP {xp}\nHP {hp}\n")
        return scene_3()
    elif option_3 in ("e", "E"):
        print(f"\n*Equipment*\nFirst Hand: {equipment_weapon}\nSecond Hand: {equipment_shield}\nAmmo: {equipment_ammunition}\nHead: {equipment_head}\nCape: {equipment_cape}\nNeck: {equipment_neck}\nChest: {equipment_body}\nLegs: {equipment_legs}\nHands: {equipment_hands}\nFeet: {equipment_feet}\nRing: {equipment_ring}\n")
        return scene_3()
    elif option_3 in ("i", "I"):
        print(f"\n*Inventory*\n{inventory_1}\n{inventory_2}\n{inventory_3}\n{inventory_4}\n{inventory_5}\n{inventory_6}\n{inventory_7}\n{inventory_8}\n{inventory_9}\n{inventory_9}\n{inventory_10}\n{inventory_11}\n{inventory_12}\n{inventory_13}\n{inventory_14}\n{inventory_15}\n{inventory_16}\n{inventory_17}\n{inventory_18}\n{inventory_19}\n{inventory_20}\n{inventory_21}\n{inventory_22}\n{inventory_23}\n{inventory_24}\n{inventory_25}\n{inventory_26}\n{inventory_27}\n{inventory_28}\n")
        return scene_3()
    else:
        print("\nOption not available. Try again.\n")
        return scene_3()
scene_3()

print("The Survival Expert gives you a Tinderbox and a Bronze Axe.\n")
inventory_1 = ("Tinderbox")
inventory_2 = ("Bronze Axe")

def scene_3_1():
    option_3_1 = input("Options 3.1\n[1] Chop down Tree    [s] Stats\n[2] Wield Bronze Axe  [e] Equipment\n[3] Examine Tree      [i] Inventory\n[4] Examine Tinderbox\n[5] Examine Bronze Axe\n[6] Do nothing\n: ")
    if (option_3_1 == "1"):
        print("\nYou chop down the tree...\n")
    elif (option_3_1 == "2"):
        print("\nYou'll be told how to wield weapons later.\n")
        return scene_3_1()
    elif (option_3_1 == "3"):
        print("\nOne of the most common trees in RuneScape.\n")
        return scene_3_1()
    elif (option_3_1 == "4"):
        print("\nUseful for lighting a fire.\n")
        return scene_3_1()
    elif (option_3_1 == "5"):
        print("\nA woodcutter's axe.\n")
        return scene_3_1()
    elif (option_3_1 == "6"):
        print("\nYou should probably start chopping down that tree.\n")
        return scene_3_1()
    elif option_3_1 in ("s", "S"):
        print(f"\n*Stats*\nLVL {level}\nXP {xp}\nHP {hp}\n")
        return scene_3_1()
    elif option_3_1 in ("e", "E"):
        print(f"\n*Equipment*\nFirst Hand: {equipment_weapon}\nSecond Hand: {equipment_shield}\nAmmo: {equipment_ammunition}\nHead: {equipment_head}\nCape: {equipment_cape}\nNeck: {equipment_neck}\nChest: {equipment_body}\nLegs: {equipment_legs}\nHands: {equipment_hands}\nFeet: {equipment_feet}\nRing: {equipment_ring}\n")
        return scene_3_1()
    elif option_3_1 in ("i", "I"):
        print(f"\n*Inventory*\n{inventory_1}\n{inventory_2}\n{inventory_3}\n{inventory_4}\n{inventory_5}\n{inventory_6}\n{inventory_7}\n{inventory_8}\n{inventory_9}\n{inventory_9}\n{inventory_10}\n{inventory_11}\n{inventory_12}\n{inventory_13}\n{inventory_14}\n{inventory_15}\n{inventory_16}\n{inventory_17}\n{inventory_18}\n{inventory_19}\n{inventory_20}\n{inventory_21}\n{inventory_22}\n{inventory_23}\n{inventory_24}\n{inventory_25}\n{inventory_26}\n{inventory_27}\n{inventory_28}\n")
        return scene_3_1()
    else:
        print("\nOption not available. Try again.\n")
        return scene_3_1()
scene_3_1()

time.sleep(sleeplong)
print("You get some logs.\n")
inventory_3 = ("Logs")
time.sleep(sleepshort)
print("You gained 10 XP.\n")
xp = ("10/100")
time.sleep(sleepmedium)

def scene_3_2():
    option_3_2 = input("Options 3.2\n[1] Use Tinderbox > Logs  [s] Stats\n[2] Examine Logs          [e] Equipment\n[3] Do nothing            [i] Inventory\n: ")
    if (option_3_2 == "1"):
        print("\nYou make a fire...\n")
    elif (option_3_2 == "2"):
        print("\nA number of wooden logs.\n")
        return scene_3_2()
    elif (option_3_2 == "3"):
        print("\nYou should probably try making a fire using your tinderbox.\n")
        return scene_3_2()
    elif option_3_2 in ("s", "S"):
        print(f"\n*Stats*\nLVL {level}\nXP {xp}\nHP {hp}\n")
        return scene_3_2()
    elif option_3_2 in ("e", "E"):
        print(f"\n*Equipment*\nFirst Hand: {equipment_weapon}\nSecond Hand: {equipment_shield}\nAmmo: {equipment_ammunition}\nHead: {equipment_head}\nCape: {equipment_cape}\nNeck: {equipment_neck}\nChest: {equipment_body}\nLegs: {equipment_legs}\nHands: {equipment_hands}\nFeet: {equipment_feet}\nRing: {equipment_ring}\n")
        return scene_3_2()
    elif option_3_2 in ("i", "I"):
        print(f"\n*Inventory*\n{inventory_1}\n{inventory_2}\n{inventory_3}\n{inventory_4}\n{inventory_5}\n{inventory_6}\n{inventory_7}\n{inventory_8}\n{inventory_9}\n{inventory_9}\n{inventory_10}\n{inventory_11}\n{inventory_12}\n{inventory_13}\n{inventory_14}\n{inventory_15}\n{inventory_16}\n{inventory_17}\n{inventory_18}\n{inventory_19}\n{inventory_20}\n{inventory_21}\n{inventory_22}\n{inventory_23}\n{inventory_24}\n{inventory_25}\n{inventory_26}\n{inventory_27}\n{inventory_28}\n")
        return scene_3_2()
    else:
        print("\nOption not available. Try again.\n")
        return scene_3_2()
scene_3_2()

print("The logs catch fire and start crackling...\n")
inventory_3 = ("empty")
time.sleep(sleeplong)
print("You gained 10 XP.\n")
xp = ("20/100")
time.sleep(sleepmedium)

def scene_3_3():
    option_3_3 = input("Options 3.3\n[1] Talk to Survival Expert  [s] Stats\n[2] Examine Fire             [e] Equipment\n[3] Do nothing               [i] Inventory\n: ")
    if (option_3_3 == "1"):
        print("\n  <Survival Expert>\n> Well done!\n> Next we need to get some food in our bellies. We'll need something to cook.\n> There are shrimp in the pond there, so let's catch and cook some.")
    elif (option_3_3 == "2"):
        print("\nHot!\n")
        return scene_3_3()
    elif (option_3_3 == "3"):
        print("\n\n  <Survival Expert>\n> Shall we go on with your training?\n")
        return scene_3_3()
    elif option_3_3 in ("s", "S"):
        print(f"\n*Stats*\nLVL {level}\nXP {xp}\nHP {hp}\n")
        return scene_3_3()
    elif option_3_3 in ("e", "E"):
        print(f"\n*Equipment*\nFirst Hand: {equipment_weapon}\nSecond Hand: {equipment_shield}\nAmmo: {equipment_ammunition}\nHead: {equipment_head}\nCape: {equipment_cape}\nNeck: {equipment_neck}\nChest: {equipment_body}\nLegs: {equipment_legs}\nHands: {equipment_hands}\nFeet: {equipment_feet}\nRing: {equipment_ring}\n")
        return scene_3_3()
    elif option_3_3 in ("i", "I"):
        print(f"\n*Inventory*\n{inventory_1}\n{inventory_2}\n{inventory_3}\n{inventory_4}\n{inventory_5}\n{inventory_6}\n{inventory_7}\n{inventory_8}\n{inventory_9}\n{inventory_9}\n{inventory_10}\n{inventory_11}\n{inventory_12}\n{inventory_13}\n{inventory_14}\n{inventory_15}\n{inventory_16}\n{inventory_17}\n{inventory_18}\n{inventory_19}\n{inventory_20}\n{inventory_21}\n{inventory_22}\n{inventory_23}\n{inventory_24}\n{inventory_25}\n{inventory_26}\n{inventory_27}\n{inventory_28}\n")
        return scene_3_3()
    else:
        print("\nOption not available. Try again.\n")
        return scene_3_3()
scene_3_3()

time.sleep(sleepshort)
print("\nThe Survival Expert gives you a Net.\n")
inventory_3 = ("Small Fishing Net")
time.sleep(sleepmedium)

def scene_3_4():
    option_3_4 = input("Options 3.4\n[1] Use Small Fishing Net > Fishing Spot  [s] Stats\n[2] Examine Small Fishing Net             [e] Equipment\n[3] Examine Fishing Spot                  [i] Inventory\n[4] Do nothing\n: ")
    if (option_3_4 == "1"):
        print("\nYou lower your net in the water...\n")
    elif (option_3_4 == "2"):
        print("\nUseful for catching small fish.\n")
        return scene_3_4()
    elif (option_3_4 == "3"):
        print("\nI can see fish swimming in the water.\n")
        return scene_3_4()
    elif (option_3_4 == "4"):
        print("\n\n  <Survival Expert>\n> Yes, you're on the right track. Firmly grasp the net.\n> Firmly grasp it!\n> Now slowly lower it into the water. Yes, there we go...\n")
        return scene_3_4()
    elif option_3_4 in ("s", "S"):
        print(f"\n*Stats*\nLVL {level}\nXP {xp}\nHP {hp}\n")
        return scene_3_4()
    elif option_3_4 in ("e", "E"):
        print(f"\n*Equipment*\nFirst Hand: {equipment_weapon}\nSecond Hand: {equipment_shield}\nAmmo: {equipment_ammunition}\nHead: {equipment_head}\nCape: {equipment_cape}\nNeck: {equipment_neck}\nChest: {equipment_body}\nLegs: {equipment_legs}\nHands: {equipment_hands}\nFeet: {equipment_feet}\nRing: {equipment_ring}\n")
        return scene_3_4()
    elif option_3_4 in ("i", "I"):
        print(f"\n*Inventory*\n{inventory_1}\n{inventory_2}\n{inventory_3}\n{inventory_4}\n{inventory_5}\n{inventory_6}\n{inventory_7}\n{inventory_8}\n{inventory_9}\n{inventory_9}\n{inventory_10}\n{inventory_11}\n{inventory_12}\n{inventory_13}\n{inventory_14}\n{inventory_15}\n{inventory_16}\n{inventory_17}\n{inventory_18}\n{inventory_19}\n{inventory_20}\n{inventory_21}\n{inventory_22}\n{inventory_23}\n{inventory_24}\n{inventory_25}\n{inventory_26}\n{inventory_27}\n{inventory_28}\n")
        return scene_3_4()
    else:
        print("\nOption not available. Try again.\n")
        return scene_3_4()
scene_3_4()

time.sleep(sleeplong)
print("You caught a shrimp.\n")
inventory_4 = ("Shrimp")
print("You gained 10 XP.\n")
xp = ("30/100")
time.sleep(sleepmedium)

def scene_3_5():
    option_3_5 = input("Options 3.5\n[1] Use Shrimp > Fire  [s] Stats\n[2] Examine Shrimp     [e] Equipment\n[3] Do nothing         [i] Inventory\n: ")
    if (option_3_5 == "1"):
        print("\nYou cook the shrimp...\n")
    elif (option_3_5 == "2"):
        print("\nI should try cooking this.\n")
        return scene_3_5()
    elif (option_3_5 == "3"):
        print("\n\n  <Survival Expert>\n> Almost done. Just cook them.\n")
        return scene_3_5()
    elif option_3_5 in ("s", "S"):
        print(f"\n*Stats*\nLVL {level}\nXP {xp}\nHP {hp}\n")
        return scene_3_5()
    elif option_3_5 in ("e", "E"):
        print(f"\n*Equipment*\nFirst Hand: {equipment_weapon}\nSecond Hand: {equipment_shield}\nAmmo: {equipment_ammunition}\nHead: {equipment_head}\nCape: {equipment_cape}\nNeck: {equipment_neck}\nChest: {equipment_body}\nLegs: {equipment_legs}\nHands: {equipment_hands}\nFeet: {equipment_feet}\nRing: {equipment_ring}\n")
        return scene_3_5()
    elif option_3_5 in ("i", "I"):
        print(f"\n*Inventory*\n{inventory_1}\n{inventory_2}\n{inventory_3}\n{inventory_4}\n{inventory_5}\n{inventory_6}\n{inventory_7}\n{inventory_8}\n{inventory_9}\n{inventory_9}\n{inventory_10}\n{inventory_11}\n{inventory_12}\n{inventory_13}\n{inventory_14}\n{inventory_15}\n{inventory_16}\n{inventory_17}\n{inventory_18}\n{inventory_19}\n{inventory_20}\n{inventory_21}\n{inventory_22}\n{inventory_23}\n{inventory_24}\n{inventory_25}\n{inventory_26}\n{inventory_27}\n{inventory_28}\n")
        return scene_3_5()
    else:
        print("\nOption not available. Try again.\n")
        return scene_3_5()
scene_3_5()

time.sleep(sleeplong)
print("You successfully cooked the shrimp.\n")
inventory_4 = ("Cooked Shrimp")
print("You gained 10 XP.\n")
xp = ("40/100")
time.sleep(sleepmedium)

def scene_3_6():
    option_3_6 = input("Options 3.6\n[1] Eat Cooked Shrimp      [s] Stats\n[2] Examine Cooked Shrimp  [e] Equipment\n[3] Do nothing             [i] Inventory\n: ")
    if (option_3_6 == "1"):
        print("\nYou eat the cooked shrimp...\n")
    elif (option_3_6 == "2"):
        print("\nSome nicely cooked shrimp.\n")
        return scene_3_6()
    elif (option_3_6 == "3"):
        print("\n\n  <Survival Expert>\n> Go on, it's yours. Eat up.\n")
        return scene_3_6()
    elif option_3_6 in ("s", "S"):
        print(f"\n*Stats*\nLVL {level}\nXP {xp}\nHP {hp}\n")
        return scene_3_6()
    elif option_3_6 in ("e", "E"):
        print(f"\n*Equipment*\nFirst Hand: {equipment_weapon}\nSecond Hand: {equipment_shield}\nAmmo: {equipment_ammunition}\nHead: {equipment_head}\nCape: {equipment_cape}\nNeck: {equipment_neck}\nChest: {equipment_body}\nLegs: {equipment_legs}\nHands: {equipment_hands}\nFeet: {equipment_feet}\nRing: {equipment_ring}\n")
        return scene_3_6()
    elif option_3_6 in ("i", "I"):
        print(f"\n*Inventory*\n{inventory_1}\n{inventory_2}\n{inventory_3}\n{inventory_4}\n{inventory_5}\n{inventory_6}\n{inventory_7}\n{inventory_8}\n{inventory_9}\n{inventory_9}\n{inventory_10}\n{inventory_11}\n{inventory_12}\n{inventory_13}\n{inventory_14}\n{inventory_15}\n{inventory_16}\n{inventory_17}\n{inventory_18}\n{inventory_19}\n{inventory_20}\n{inventory_21}\n{inventory_22}\n{inventory_23}\n{inventory_24}\n{inventory_25}\n{inventory_26}\n{inventory_27}\n{inventory_28}\n")
        return scene_3_6()
    else:
        print("\nOption not available. Try again.\n")
        return scene_3_6()
scene_3_6()

time.sleep(sleeplong)
print("You eat the cooked shrimp.\n")
inventory_4 = ("empty")
time.sleep(sleepmedium)

print("You gain 3 HP!\n...But you're already at max HP.")
time.sleep(sleepmedium)

print("\n  <Survival Expert>\n> Well done, you made your first RuneScape meal.\n> If you'd like a recap on anything you've learnt so far, let me know.\n")
time.sleep(sleepshort)
def scene_3_7():
    option_3_7 = input("Options 3.7\n[1] Move on      [s] Stats\n[2] Woodcutting  [e] Equipment\n[3] Fishing      [i] Inventory\n[4] Cooking\n[5] Do nothing\n: ")
    if (option_3_7 == "1"):
        print(f"\n  <{player}>\n> That was all for now.")
        print("\n  <Survival Expert>\n> Well, then you can move on to the next instructor.\n> Go through the gate and follow the path.\n")
    elif (option_3_7 == "2"):
        print(f"\n  <{player}>\n> Tell me about woodcutting again.")
        print("\n  <Survival Expert>\n> Woodcutting, eh? Don't worry, newcomer, it's really very easy.\n> Simply equip your axe and click on a nearby tree to chop away.\n> As you explore the mainland you will discover many different kind of trees-\n> that will require different levels to chop down.\n> Logs are not only useful for making fires.\n> Many archers use the skill known as Fletching to craft their own bows and arrows from trees.\n> Was there anything else you wished to hear again?\n")
        return scene_3_7()
    elif (option_3_7 == "3"):
        print(f"\n  <{player}>\n> Tell me about fishing again.")
        print("\n  <Survival Expert>\n> Ah, yes. Fishing! Fishing is undoubtedly one of the most popular hobbies here in RuneScape!\n> Not only are fish absolutely delicious when cooked,\n> there are always fighters willing to buy a well cooked fish when they're low on health.\n> I would recommend everybody has a go at Fishing at least once in their lives!\n> Was there anything else you wished to hear again?\n")
        return scene_3_7()
    elif (option_3_7 == "4"):
        print(f"\n  <{player}>\n> Tell me about cooking again.")
        print("\n  <Survival Expert>\n> Yes, the most basic of survival techniques.\n> Most simple meals can be cooked on a fire. Eating food will restore a little health.\n> The harder something is to cook, the more it will heal you.\n> Somewhere around here is a chef who will tell you more about food and cooking it.\n")
        return scene_3_7()
    elif (option_3_7 == "5"):
        print("\n  <Survival Expert>\n>In case you're waiting for me to continue, this was all. But feel free to ask if you want me to repeat something.\n")
        return scene_3_7()
    elif option_3_7 in ("s", "S"):
        print(f"\n*Stats*\nLVL {level}\nXP {xp}\nHP {hp}\n")
        return scene_3_7()
    elif option_3_7 in ("e", "E"):
        print(f"\n*Equipment*\nFirst Hand: {equipment_weapon}\nSecond Hand: {equipment_shield}\nAmmo: {equipment_ammunition}\nHead: {equipment_head}\nCape: {equipment_cape}\nNeck: {equipment_neck}\nChest: {equipment_body}\nLegs: {equipment_legs}\nHands: {equipment_hands}\nFeet: {equipment_feet}\nRing: {equipment_ring}\n")
        return scene_3_7()
    elif option_3_7 in ("i", "I"):
        print(f"\n*Inventory*\n{inventory_1}\n{inventory_2}\n{inventory_3}\n{inventory_4}\n{inventory_5}\n{inventory_6}\n{inventory_7}\n{inventory_8}\n{inventory_9}\n{inventory_9}\n{inventory_10}\n{inventory_11}\n{inventory_12}\n{inventory_13}\n{inventory_14}\n{inventory_15}\n{inventory_16}\n{inventory_17}\n{inventory_18}\n{inventory_19}\n{inventory_20}\n{inventory_21}\n{inventory_22}\n{inventory_23}\n{inventory_24}\n{inventory_25}\n{inventory_26}\n{inventory_27}\n{inventory_28}\n")
        return scene_3_7()
    else:
        print("\nOption not available. Try again.\n")
        return scene_3_7()
scene_3_7()

print("You walk away from Brynna and soon find a fence gate in front of you.\n")

def scene_4():
    option_4 = input("Options 4\n[1] Open Gate     [s] Stats\n[2] Examine Gate  [e] Equipment\n[3] Do nothing    [i] Inventory\n: ")
    if (option_4 == "1"):
        print("\nYou open the gate and walk down the path.\n")
    elif (option_4 == "2"):
        print("\nA wooden gate.\n")
        return scene_4()
    elif (option_4 == "3"):
        print("\nYou stroke your chin and admire the amount of craftmanship put into the gate.\n")
        return scene_4()
    elif option_4 in ("s", "S"):
        print(f"\n*Stats*\nLVL {level}\nXP {xp}\nHP {hp}\n")
        return scene_4()
    elif option_4 in ("e", "E"):
        print(f"\n*Equipment*\nFirst Hand: {equipment_weapon}\nSecond Hand: {equipment_shield}\nAmmo: {equipment_ammunition}\nHead: {equipment_head}\nCape: {equipment_cape}\nNeck: {equipment_neck}\nChest: {equipment_body}\nLegs: {equipment_legs}\nHands: {equipment_hands}\nFeet: {equipment_feet}\nRing: {equipment_ring}\n")
        return scene_4()
    elif option_4 in ("i", "I"):
        print(f"\n*Inventory*\n{inventory_1}\n{inventory_2}\n{inventory_3}\n{inventory_4}\n{inventory_5}\n{inventory_6}\n{inventory_7}\n{inventory_8}\n{inventory_9}\n{inventory_9}\n{inventory_10}\n{inventory_11}\n{inventory_12}\n{inventory_13}\n{inventory_14}\n{inventory_15}\n{inventory_16}\n{inventory_17}\n{inventory_18}\n{inventory_19}\n{inventory_20}\n{inventory_21}\n{inventory_22}\n{inventory_23}\n{inventory_24}\n{inventory_25}\n{inventory_26}\n{inventory_27}\n{inventory_28}\n")
        return scene_4()
    else:
        print("\nOption not available. Try again.\n")
        return scene_4()
scene_4()

time.sleep(sleepmedium)
print("You walk by some more grassy scenery. There's an ocean to the left. It's all pretty much to the same really.\nAs you arrive to the next instructor's house, you see a waterfall with bugged graphics to your left.\n")
time.sleep(sleepshort)

def scene_4_1():
    option_4_1 = input("Options 4.1\n[1] Open Door     [s] Stats\n[2] Examine Door  [e] Equipment\n[3] Do nothing    [i] Inventory\n: ")
    if (option_4_1 == "1"):
        print("\nYou open the door and walk inside.\n")
    elif (option_4_1 == "2"):
        print("\nA nicely fitted door. Yep, exactly the same door as the one in the beginning.\n")
        return scene_4_1()
    elif (option_4_1 == "3"):
        print("\nYou stand in front of the door expecting it to open by itself. Maybe it requires some secret passcode?\n")
        passcode = input(": ")
        print("f\n\n  <{player}>\n> {passcode}\n")
        print("Someone opens the door.\nThat was it. It worked!\n")
    elif option_4_1 in ("s", "S"):
        print(f"\n*Stats*\nLVL {level}\nXP {xp}\nHP {hp}\n")
        return scene_4_1()
    elif option_4_1 in ("e", "E"):
        print(f"\n*Equipment*\nFirst Hand: {equipment_weapon}\nSecond Hand: {equipment_shield}\nAmmo: {equipment_ammunition}\nHead: {equipment_head}\nCape: {equipment_cape}\nNeck: {equipment_neck}\nChest: {equipment_body}\nLegs: {equipment_legs}\nHands: {equipment_hands}\nFeet: {equipment_feet}\nRing: {equipment_ring}\n")
    elif option_4_1 in ("i", "I"):
        return scene_4_1()
        print(f"\n*Inventory*\n{inventory_1}\n{inventory_2}\n{inventory_3}\n{inventory_4}\n{inventory_5}\n{inventory_6}\n{inventory_7}\n{inventory_8}\n{inventory_9}\n{inventory_9}\n{inventory_10}\n{inventory_11}\n{inventory_12}\n{inventory_13}\n{inventory_14}\n{inventory_15}\n{inventory_16}\n{inventory_17}\n{inventory_18}\n{inventory_19}\n{inventory_20}\n{inventory_21}\n{inventory_22}\n{inventory_23}\n{inventory_24}\n{inventory_25}\n{inventory_26}\n{inventory_27}\n{inventory_28}\n")
        return scene_4_1()
    else:
        print("\nOption not available. Try again.\n")
        return scene_4_1()
scene_4_1()

time.sleep(sleepshort)
print("You walk inside the building and see a guy looking at you. It looks like he's seconds away from bursting into laughter.\n")
time.sleep(sleepshort)

def scene_5():
    option_5 = input("Options 5 \n[1] Talk to Master Chef  [s] Stats\n[2] Examine Master Chef  [e] Equipment\n[3] Do nothing           [i] Inventory\n: ")
    if (option_5 == "1"):
        print("\n  <Master Chef>\n> Ah! Welcome, newcomer. I am the Master Chef, Lev.\n> It is here I will teach you how to cook food truly fit for a king.\n")
    elif (option_5 == "2"):
        print("\nAn expert on all things culinary.\n")
        return scene_5()
    elif (option_5 == "3"):
        print("\nStare back and smile.\n")
        return scene_5()
    elif option_5 in ("s", "S"):
        print(f"\n*Stats*\nLVL {level}\nXP {xp}\nHP {hp}\n")
        return scene_5()
    elif option_5 in ("e", "E"):
        print(f"\n*Equipment*\nFirst Hand: {equipment_weapon}\nSecond Hand: {equipment_shield}\nAmmo: {equipment_ammunition}\nHead: {equipment_head}\nCape: {equipment_cape}\nNeck: {equipment_neck}\nChest: {equipment_body}\nLegs: {equipment_legs}\nHands: {equipment_hands}\nFeet: {equipment_feet}\nRing: {equipment_ring}\n")
        return scene_5()
    elif option_5 in ("i", "I"):
        print(f"\n*Inventory*\n{inventory_1}\n{inventory_2}\n{inventory_3}\n{inventory_4}\n{inventory_5}\n{inventory_6}\n{inventory_7}\n{inventory_8}\n{inventory_9}\n{inventory_9}\n{inventory_10}\n{inventory_11}\n{inventory_12}\n{inventory_13}\n{inventory_14}\n{inventory_15}\n{inventory_16}\n{inventory_17}\n{inventory_18}\n{inventory_19}\n{inventory_20}\n{inventory_21}\n{inventory_22}\n{inventory_23}\n{inventory_24}\n{inventory_25}\n{inventory_26}\n{inventory_27}\n{inventory_28}\n")
        return scene_5()
    else:
        print("\nOption not available. Try again.\n")
        return scene_5()
scene_5()

time.sleep(sleepshort)
print(f"\n  <{player}>\n> I already know how to cook. Brynna taught me just now.\n")
time.sleep(sleepshort)
print("\n  <Master Chef>\n> Hahahahahaha! You call THAT cooking?\n> Some shrimp on an open log fire?\n> Oh, no, no, no. I am going to teach you the fine art of cooking bread.\n")
print("\nThe Cooking Guide gives you a bucket of water and a pot of flour!\n")
inventory_4 = "Bucket of Water"
inventory_5 = "Pot of Flour"

def scene_5_1():
    option_5_1 = input ("Options 5.1\n[1] Talk to Master Chef      [s] Stats\n[2] Examine Bucket of Water  [e] Equipment\n[3] Examine Pot of Flour     [i] Inventory\n[4] Do nothing\n: ")
    if (option_5_1 == "1"):
        print(f"\n  <{player}>\n> So what do I do with this?\n")
        print("\n  <Master Chef>\n> To start off, you're gonna have to make dough. This is the base for many of the meals.\n> To make dough we must mix flour and water.\n")
    elif (option_5_1 == "2"):
        print("\nIt's a bucket of water.\n")
        return scene_5_1()
    elif (option_5_1 == "3"):
        print("\nIt's a pot of flour.\n")
        return scene_5_1()
    elif (option_5_1 == "4"):
        print("\n  <Master Chef>\n> Any more questions?")
        return scene_5_1()
    elif option_5_1 in ("s", "S"):
        print(f"\n*Stats*\nLVL {level}\nXP {xp}\nHP {hp}\n")
        return scene_5_1()
    elif option_5_1 in ("e", "E"):
        print(f"\n*Equipment*\nFirst Hand: {equipment_weapon}\nSecond Hand: {equipment_shield}\nAmmo: {equipment_ammunition}\nHead: {equipment_head}\nCape: {equipment_cape}\nNeck: {equipment_neck}\nChest: {equipment_body}\nLegs: {equipment_legs}\nHands: {equipment_hands}\nFeet: {equipment_feet}\nRing: {equipment_ring}\n")
        return scene_5_1()
    elif option_5_1 in ("i", "I"):
        print(f"\n*Inventory*\n{inventory_1}\n{inventory_2}\n{inventory_3}\n{inventory_4}\n{inventory_5}\n{inventory_6}\n{inventory_7}\n{inventory_8}\n{inventory_9}\n{inventory_9}\n{inventory_10}\n{inventory_11}\n{inventory_12}\n{inventory_13}\n{inventory_14}\n{inventory_15}\n{inventory_16}\n{inventory_17}\n{inventory_18}\n{inventory_19}\n{inventory_20}\n{inventory_21}\n{inventory_22}\n{inventory_23}\n{inventory_24}\n{inventory_25}\n{inventory_26}\n{inventory_27}\n{inventory_28}\n")
        return scene_5_1()
    else:
        print("\nOption not available. Try again.\n")
        return scene_5_1()
scene_5_1()

def scene_5_2():
    option_5_2 = input("Options 5.2\n[1] Use Bucket of Water > Pot of Flour [s] Stats\n[2] Do nothing                         [e] Equipment\n                                       [i] Inventory\n: ")
    if (option_5_2 == "1"):
        print("\nYou mix the water and flour togeter...\n")
    elif (option_5_2 == "2"):
        print("\n  <Master Chef>\n> You know how to put one and one together, don't you?\n")
        return scene_5_2()
    elif option_5_2 in ("s", "S"):
        return scene_5_2()
        print(f"\n*Stats*\nLVL {level}\nXP {xp}\nHP {hp}\n")
    elif option_5_2 in ("e", "E"):
        print(f"\n*Equipment*\nFirst Hand: {equipment_weapon}\nSecond Hand: {equipment_shield}\nAmmo: {equipment_ammunition}\nHead: {equipment_head}\nCape: {equipment_cape}\nNeck: {equipment_neck}\nChest: {equipment_body}\nLegs: {equipment_legs}\nHands: {equipment_hands}\nFeet: {equipment_feet}\nRing: {equipment_ring}\n")
        return scene_5_2()
    elif option_5_2 in ("i", "I"):
        print(f"\n*Inventory*\n{inventory_1}\n{inventory_2}\n{inventory_3}\n{inventory_4}\n{inventory_5}\n{inventory_6}\n{inventory_7}\n{inventory_8}\n{inventory_9}\n{inventory_9}\n{inventory_10}\n{inventory_11}\n{inventory_12}\n{inventory_13}\n{inventory_14}\n{inventory_15}\n{inventory_16}\n{inventory_17}\n{inventory_18}\n{inventory_19}\n{inventory_20}\n{inventory_21}\n{inventory_22}\n{inventory_23}\n{inventory_24}\n{inventory_25}\n{inventory_26}\n{inventory_27}\n{inventory_28}\n")
        return scene_5_2()
    else:
        print("\nOption not available. Try again.\n")
        return scene_5_2()
scene_5_2()

inventory_4 = "Bucket"
inventory_5 = "Pot"
inventory_6 = "Dough"

print("\n  <Master Chef>\n> Now you have made dough, you can cook it. To cook the dough, use the range in front of you\n")

def scene_5_3():
    option_5_3 = input("Options 5.3 \n[1] ... [s] Stats\n[2] ...  [e] Equipment\n[3] ...  [i] Inventory\n: ")
    if (option_5_3 == "1"):
        print("\n\n")
    elif (option_5_3 == "2"):
        print("\n\n")
        return scene_()
    elif (option_5_3 == "3"):
        print("\n\n")
        return scene_5_3()
    elif option_5_3 in ("s", "S"):
        print(f"\n*Stats*\nLVL {level}\nXP {xp}\nHP {hp}\n")
        return scene_5_3()
    elif option_5_3 in ("e", "E"):
        print(f"\n*Equipment*\nFirst Hand: {equipment_weapon}\nSecond Hand: {equipment_shield}\nAmmo: {equipment_ammunition}\nHead: {equipment_head}\nCape: {equipment_cape}\nNeck: {equipment_neck}\nChest: {equipment_body}\nLegs: {equipment_legs}\nHands: {equipment_hands}\nFeet: {equipment_feet}\nRing: {equipment_ring}\n")
        return scene_5_3()
    elif option_5_3 in ("i", "I"):
        print(f"\n*Inventory*\n{inventory_1}\n{inventory_2}\n{inventory_3}\n{inventory_4}\n{inventory_5}\n{inventory_6}\n{inventory_7}\n{inventory_8}\n{inventory_9}\n{inventory_9}\n{inventory_10}\n{inventory_11}\n{inventory_12}\n{inventory_13}\n{inventory_14}\n{inventory_15}\n{inventory_16}\n{inventory_17}\n{inventory_18}\n{inventory_19}\n{inventory_20}\n{inventory_21}\n{inventory_22}\n{inventory_23}\n{inventory_24}\n{inventory_25}\n{inventory_26}\n{inventory_27}\n{inventory_28}\n")
        return scene_5_3()
    else:
        print("\nOption not available. Try again.\n")
        return scene_5_3()
scene_5_3()
