print("Please enter the following:\n")
areYouSure = False
while areYouSure == False:
    adj = input("adjective: ")
    animal = input("animal: ")
    verb = input("verb: ")
    exclamation = input("exclamation: ")
    verb2 = input("verb: ")
    verb3 = input("verb: ")
    areYouSure = input("Are you sure? (y/n) ").lower()[0] != 'n'
print("\nYour story is:\n")
print("The other day, I was really in trouble. It all started when I saw a very")
print(adj + " " + animal + " " + verb + " down the hallway. \"" + exclamation.capitalize() + "!\" I yelled. But all")
print("I could think to do was to " + verb2 + " over and over. Miraculously,")
print("that caused it to stop, but not before it tried to " + verb3)
print("right in front of my family.")