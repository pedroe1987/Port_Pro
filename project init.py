#Intro
print('--------------------------------------')
print('Hello, Welcome to Financial Planner')
print('a new tool under your belt to help you')
print('plan for your financial future')
print('--------------------------------------')

#Getting the name
name = input('How do you like to be called from my part?')
no_name = 'X' 
if name:
    print('Thank you ' + name)
else:
    print('Thank you ' + no_name)
print('--------------------------------------')

#Getting info on type of help
print('How can i help you with?')
print('You can type the number of your option:')
print('1- Plan a vacation, 2- Save more money, 3- Increase my income')

goal = input('Enter goal: ')
options = ['1', '2', '3' ]

while goal not in options:
    print('One more time')
    goal = input('Enter goal: ')
while goal in options:
    if goal == options[0]:
        print('Alright lets start planning your vacations')
        break
    elif goal == options[1]:
        print('Let\'s see how can i help you save more money')
        break
    else:
        print('You said it, lets make more money')
        break
print('Thank you for entering your goal')
print('--------------------------------------')

#Gathering info for the calculations
salary = 2
monthly_expenses = 1
if goal != options[2]:
    print('Let\'s gather some information about your income')
    print('Tell me about your salary on a monthly basis')
    salary = int(input('How much do you earn in a month?: '))
    print('Thank you for providing your salary')
    print('--------------------------------------')


    print('In a monthly basis, how much do you spend?')
    print('Add everything that applies to you(rent, car, insurance, phone, wifi etc...)')
    monthly_expenses = int(input('Enter your monthly expenses: '))
    print('Thank you for the info ')
    print('--------------------------------------')

budget = 0
if goal == options[0]:
    print('Now let\'s think about, how much would you like to budget for the vacations?')
    budget = int(input('Enter your budget: '))
    print('Thanks again')
    print('--------------------------------------')


monthly_savings = salary - monthly_expenses
amount_of_months = budget / monthly_savings

#Answer for option 1
if goal == options[0]:
    if amount_of_months > 0:
        print('In orther to enjoy those vacations you will have to start saving {} in advance'.format(amount_of_months))
    else:
        print('You can\'t not go on vacations right now, you will have to increase your income or decrese your expenses.')
        print('--------------------------------------')
        print('Here are some remomendations:')
        print('Find a side hustle on your days off.')
        print('Request overtime at work.')
        print('Request a raise.')
        print('Move to a better paid job.')

#Answer for option 2
money_to_save = 0
if goal == options[1]:
    money_to_save = int(input('How much do you want to save: '))

months_to_save = money_to_save / monthly_savings
if goal == options[1]:
    if monthly_savings > 0 and monthly_savings <= 100:
        print('Its goint to take a while but')
        print('keeping the current living expenses')
        print('It will require {} months to save that amount.'.format(months_to_save))
    elif monthly_savings > 100 and monthly_savings <= 1000:
        print('you will need to save for only {} months.'.format(months_to_save))
    elif monthly_savings > 1000 and monthly_savings < 5000:
        print('Just think about it {} months in advance'.format(months_to_save))
    else:
        print('As easy as {} months'.format(months_to_save))

#Answer for option 3

if goal == options[2]:
    print('Here are some remomendations:')
    print('Find a side hustle on your days off.')
    print('Request overtime at work.')
    print('Request a raise.')
    print('Move to a better paid job.')
    print('Learn new better paid skills.')
    print('--------------------------------------')

print('Happy planning')
input('Enter any key for exit')