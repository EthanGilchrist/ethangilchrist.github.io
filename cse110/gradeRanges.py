grade = int(input("Enter your grade: "))
letter = 'E'
if (grade >= 90):
    letter = 'A'
elif (grade >= 80):
    letter = 'B'
elif (grade >= 70):
    letter = 'C'
elif (grade >= 60):
    letter = 'D'
else:
    letter = 'F'
plusOrMinus = ''
if (grade % 10 >= 7):
    plusOrMinus = '+'
if (grade % 10 < 3):
    plusOrMinus = '-'
if (grade > 96 or grade < 60):
    plusOrMinus = ''
print(letter + plusOrMinus)
if (grade >= 70):
    print("Congratulations!")
else:
    print("You can do it!")