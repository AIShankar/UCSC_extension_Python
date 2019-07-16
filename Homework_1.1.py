'''Write a program that asks the user for their dream job title.  Then ask them for the hourly wage they want to earn.
This number should account for dollars and cents. Calculate the annual wage they will earn over a year.
Assume they work 48 weeks a year (4 weeks vacation) but are paid over 52 weeks.
Then ask them how much money they feel they will need at retirement time.
Determine the number of years they will have to work to save up their retirement dollar value assuming
their only source of income was their paycheck?  Finally, determine if the number of years they need to
save is an even or odd number.  For this part, use the modulus operator to determine if the number you calculated
is odd or even.  Once you have calculated it, use print to print out the value.  You should also print out
something like this.  "If the value is --- then the number is odd, however, if the value is ----- then the number is even."
Make sure you account for user input error.  Test your code by trying to cause errors in input.
It is not important to error check on their dream job title.  Just assume it will be a reasonable string. '''

dream_job = input("What is your dream job?") #raw_input in py2.0 is input in py3.5

while True:
    try:
        hourly_wage = float(input("Enter the hourly wage you wish to earn:"))
        break # if the value is a float
    except ValueError:
        print("Oops!  That was not a valid number.  Try again by entering an integer or float...")

annual_wage = float(hourly_wage) * 40 * 52 #Assuming they work 40 hours a week and 48 weeks but are paid for 52 weeks

while True:
    try:
        retirement_savings = float(input("How much money do you need for retirement?"))
        break # if the value is a float
    except ValueError:
        print("Oops!  That was not a valid number.  Try again by entering an integer or float...")

try:
    annual_savings = annual_wage / 2
    working_years = retirement_savings / annual_savings
    print ("Assuming you are able to save 50% of your annual wage, ", annual_wage)
    print ("You need to work for, ", working_years, " years")
    if (int(working_years) % 2 == 0):
        print("If hourly wage is ", hourly_wage, "You need to save even number of years")
    else:
        print("If hourly wage is " ,hourly_wage, "You need to save odd number of years")       
except ZeroDivisionError:
    print ("Hope you entered 0 wage by mistake. If not ...")
    print ("Sorry to hear your services are not being paid. You have to look for a job to save up for retirement :( ")
except ValueError:
    print("Oops!  That was no valid number.  Try again...")


