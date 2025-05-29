print("You have narrowly escaped being slain by a dragon and can see the city of Helgen burning to the ground. Will you RETURN or EXPLORE?")
deathMessage = "\nWhat you just said made so little sense that the only explanation is that you had a stroke. You died."
userInput = input().lower()
if (userInput == "return"):
    print("\nWith the dragon gone, you may safely search the ruins for useful items. Will you search the KEEP or the BLACKSMITH?")
    userInput = input().lower()
    if (userInput == "keep"):
        print("\nYou find a spellbook and some potions. You learn the spell and practice it a little. Seems like a useful skill to master. The potions seem useful, too. Will you study SPELLS, or POTIONS?")
        userInput = input().lower()
        if (userInput == "spells"):
            print("You keep practicing your spells and eventually join the College of Winterhold!")
        elif (userInput == "potions"):
            print("You travel across the land finding new ingredients and learning more about potions, but one day you drink the wrong one and paralyze yourself for 187,027,498 seconds. See you in six years!")
    elif (userInput == "blacksmith"):
        print("\nYou find a sword, a shield, and some armor. You feel ready to fight. Will you fight a TROLL or a WITCH")
        userInput = input().lower()
        if (userInput == "troll"):
            print("The troll is too toxic and you die. Womp womp.")
        elif (userInput == "witch"):
            print("After verifying that the person you suspect to be a witch does in fact weigh the same as a duck, you burn her! You are now a certified witch hunter.")
        else:
            print(deathMessage)
    else:
        print(deathMessage)
elif (userInput == "explore"):
    print("\nYou come across the Guardian Stones. You may pick one and receive it's blessing, but only one. Will you choose the WARRIOR stone, the MAGE stone, or the THIEF stone?")
    userInput = input().lower()
    if (userInput == "warrior"):
        print("Warrior text")
    elif (userInput == "mage"):
        print("Mage text")
    elif (userInput == "thief"):
        print("You feel sneaky. You decide to practice your sneaking skills. Will you practice on WOLVES or BANDITS?")
        userInput = input().lower()
        if (userInput == "wolves"):
            print("A level 50 rogue named Ambrose sneaks up on you and stabs you in the back for daring to harass the adorable puppies.")
        elif (userInput == "bandits"):
            print("You enter Embershard mine and pick off the bandits one by one. Congratulations, you are now the hero of Embershard Mine!")
        else:
            print(deathMessage)
    else:
        print(deathMessage)
else:
    print(deathMessage)