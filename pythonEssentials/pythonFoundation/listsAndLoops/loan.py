money_owed = float(input("How much money do you owe in USD? \n"))
apr = float(input("What is the annual percentage rate (APR) on the loan? \n"))
monthly_payment = float(input("How much money do you plan to pay each month in USD? \n"))
months = int(input("How many months do you want to see the results for? \n"))

monthly_rate = apr / 100 / 12

for i in range(months):
     interest = money_owed * monthly_rate
     money_owed += interest

     if money_owed - monthly_payment <= 0:
          print("The last payment is ", money_owed)
          print(f"You paid off the loan in {i + 1} months!")
          break
     money_owed -= monthly_payment
     print('Paid', monthly_payment, 'of which', interest, 'was interest. Remaining balance is', money_owed)