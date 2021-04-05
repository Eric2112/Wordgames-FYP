#import random
#import os

#def formWord(request):
 #   with open(os.path.expanduser('gutenbergDictionary.txt'), 'r') as infile:
  #      words = [word for word in infile.read().split() if len(word) == 4]

   # letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #size = 4
    #chosen = (random.choice(words))

    #guesses = 0
    #while True:
     #   guesses += 1
      #  while True:
            # get a good guess
       #     guess = input('\n Guess the correct word[%i]: '% guesses).strip()
        #    if len(guess) == size and \
         #   all(char in letters for char in guess) \
          #  and len(set(guess)) == size:
           # break

       # if guess == chosen:
        #    break
        #bulls = cows = 0
        #for i in range(size):
         #   if guess[i] == chosen[i]:
          #      bulls += 1
           # elif guess[i] in chosen:
            #    cows += 1