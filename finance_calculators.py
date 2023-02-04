import math

# print investment or bond description then ask for input
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")
investment = input("\nEnter either investment or bond from the menu above to proceed: ")

# convert investment type to lowercase so all entries are recognised
investment_type = investment.lower()


# if the user selects investment
if investment_type == "investment":
    deposit = float(input("How much money are you depositing: "))
    interest_rate = float(input("What is the interest rate in numbers: "))
    interest_percent = interest_rate / 100
    years = float(input("How many years do you plan on investing: "))
    interest = input("What interest type do you want? (simple or compound) ")
    if interest == "simple":
        total = round(deposit * (1 + interest_percent * years), 2)
        print(f"\nThe amount you will have after your investment ends is {total}")
    elif interest == "compound":
        total = round(deposit * math.pow((1 + interest_percent) , years) , 2)
        print(f"\nThe amount you will have after your investment ends is {total}")
# if the user selects bond
elif investment_type == "bond":
    house_value = float(input("What is the current value of the house: "))
    interest_rate = float(input("What is the interest rate in numbers: "))
    interest_percent = (interest_rate / 100) / 12
    months = int(input("How many months to repay the bond: "))
    repayment = round((interest_percent * house_value) / (1 - (1 + interest_percent) ** (-months)) , 2)
    print(f"\nThe amount you will repay each month is {repayment}")
# if the users input is invalid display error message
else:
    print("\nYour input was not recognised please rerun program and try again")