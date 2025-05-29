print("Please answer the following questions on a scale from 1 to 10.")
loan = int(input("How large is the loan? "))
hist = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down = int(input("How large is your down payment? "))
if (loan > 10 or hist > 10 or income > 10 or down > 10 or loan < 1 or hist < 1 or income < 1 or down < 1):
    print("You are not qualified to receive a loan on the grounds that you couldn't even follow the instructions.")
    exit
decision = False
if (loan >= 5):
    if (hist >= 7 and income >= 7):
        decision = True
    elif ((hist >= 5 or income >= 5) and down >= 5):
        decision = True
elif (hist >= 4):
    decision = income >= 7 or down >= 7 or (income >= 4 and down >= 4)

if (decision):
    print("Approved")
else: print("Denied")