import random
rand_number = random.randint(0,100)
number_found = False
guesses_no = 1
print ("Guess number game")
guess = int(input("Guess number: "))

while number_found == False:
  if guess < rand_number:
    guess = int(input("Too low, choose again: "))
    guesses_no += 1
    noumber_found = False
  elif guess > rand_number:
    guess = int(input("Too high, choose again: "))
    guesses_no += 1
    noumber_found = False
  else:
    print ("You've it! It took %s guesses" % guesses_no )
    number_found = True
  
