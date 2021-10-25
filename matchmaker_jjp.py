# Justina Piwoni
# Matchmaker
 
# Constants
from typing import Mapping
 
def requestAValidNumberBetween1And5():
    UserResponse2String = str(input('Enter a number between 1 and 5.\n'))
    print('You entered: ' + UserResponse2String)
 
    if not UserResponse2String.isnumeric():
        print('This is not a number!')
        return False, 0
    else:
        UserResponse2Int = int(UserResponse2String)
    if (UserResponse2Int < 1) or (UserResponse2Int > 5):
        print('\nThis is not a number between 1 and 5.')
        return False, 0
    else:
        print('\nThis is a number between 1 and 5. Great job!')
        return True, UserResponse2Int
 
def determineRangeCompatibility(userTotalCompatibility):
    if userTotalCompatibility >= 95:
        print('So can I call you tonight?')
    elif 75 <= userTotalCompatibility <= 94: 
        print('Uh... Friends?')
    else:
        print('Ugh, As if!')

INTRODUCTION = '''
*****************************************************
                Justina's Matchmaker
        Are you worthy of being called mine?
                WinningMyLoveSoft, Inc.
*****************************************************       
 
This program figures out whether you are worthy of 
having someone like me.
 
You will answer 5 questions. To each question, answer 5
if you strongly agree, 4 if you agree, 3 if you neither 
agree nor disagree, 2 if you disagree, and 1 if you 
strongly disagree.
 
It is either you get me or you do not. If you do not, 
then it is clearly for the best. Do not come running 
back asking for my love... it will not be reciprocated.
 
*****************************************************
'''
 
QUESTION = [
    'Kevin Parker (Tame Impala) is the best and most talented music artist out there.',
    'All Jeep cars are ugly except the Jeep Wrangler.',
    'Everyone should be vegan.',
    'Texas Roadhouse is the best restaurant.',
    'Traveling is a necessity.'
]
 
DESIRED_RESPONSE = [
    5, # strongly agree
    4, # agree
    3, # neither agree or disagree
    1, # strongly disagree
    5, # strongly agree
]
 
MAX_SCORE = 5 * len(QUESTION)
 
print(INTRODUCTION)
 
compatibility = []

for i in range(len(QUESTION)):
    userHasEnteredANumberBetween1And5 = False
    userResponse = 0
    print(QUESTION[i])
    while not userHasEnteredANumberBetween1And5: 
        userHasEnteredANumberBetween1And5, userResponse = requestAValidNumberBetween1And5()
        print(userHasEnteredANumberBetween1And5)
    if not userHasEnteredANumberBetween1And5:
        print("Please try again.")
 
    print(userResponse)
 
    questionCompatibility = 5 - abs(userResponse - DESIRED_RESPONSE[i])
    compatibility.append(questionCompatibility)
 
    # String formatting with paramaters and placeholders.
    print('Question %d compatibility: %d\n' % (i+1, questionCompatibility))
 
totalCompatibility = 0
for c in compatibility:
    totalCompatibility += c
 
totalCompatibility *= 100 / MAX_SCORE
print('Total Compatibility: %d\n\n' % (totalCompatibility))
 
determineRangeCompatibility(totalCompatibility)