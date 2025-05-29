no = "Sorry, you may not ride."
firstAge = int(input("What is the age of the first rider? "))
firstHeight = int(input("What is the height of the first rider? "))
if (firstHeight < 36):
    print(no)
    exit
secondAge = -1
secondHeight = -1
secondRider = False
if (input("").lower() == "yes"):
    secondAge = int(input("What is the age of the second rider? "))
    secondHeight = int(input("What is the height of the second rider? "))
    secondRider = True
if ((firstAge < 18 or firstHeight < 62) and not secondRider):
    print(no)
    exit
if (firstAge < 18 and secondAge < 18):
    print(no)
    exit
print("Welcome to the ride. Please be safe and have fun!")