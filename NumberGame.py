import random
randomNumber = random.randint(1,10)
chances = 1
print('Hello')
print('Welcome to Number Guessing game ')
print('Guess a number between 1 and 10 (Including 1 and 10)')
print('If the number entered by you is equal')
print('to the number randomly genereted by')
print('computer then you are the winner')
print('You have 5 chances to do this')
print('All the best')
while chances < 7:
  if(chances == 6):
    print('Chances are over. You lost the game. The number is ',randomNumber)
    break
  guess = int(input('Enter your guess'))
  if(guess < randomNumber):
    if(chances <= 5):
      print('Nope. Hint: The number is less than the number you have guessed')
  elif(guess > randomNumber):
    if(chances <=5 ):
      print('Nope. Hint: The number is greater than the number you have guessed')
  elif(guess == randomNumber):
    if(chances <= 5):
      print('Yah, You got is right')
      break
  
  chances += 1
