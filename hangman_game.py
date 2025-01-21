#**************STEP1******************** 

#TODO 1:to choose a random word form a list of words and assing it to a variable
hangmanpics = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']

print("WELCOME TO HANGMAN GAME")

import random
_words="ant babboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole rat raven rhino shark sheep spider toad turkey turtle wolf wombat zebra"
list_of_words=_words.split()
random_word_position=random.randint(0,len(list_of_words))
choosen_word=list_of_words[random_word_position]
print(choosen_word)

#TODO 8: create a variable called "lives" and keep the track of how many lives user have left
#set lives equal to 6.
lives=6
print("***********you have only 6 lives to play***********")

#TODO 4: create an empty string called palce holder
#for each letter in the choosen_word add a _ to the place holder
#if the choosen_word is "apple" then placeholder be "_ _ _ _ _"
place_holder=""
for i in choosen_word:
    place_holder+="_"

#TODO 2: ask the user for a letter asings it to a veriable called guess.make sure it is lower case
#TODO 6: use the while loop to let the user to let guess again
correct_letters=[]
game_over=False
while not game_over:
    guess=input("guess a letter:").lower()

    #TODO 9: if user entered a letter they have already guessed ,
    # print the letter and let them know
    if guess in correct_letters:
      print(f"you have already guessed letter {guess},guess another letter")

    #TODO 3 :check if the letter the user guessed is one of the letters in the choosen words.
    #print "right" if it is
    #print "wrong" if it is not

    # for i in range(0,len(choosen_word)):
    #     if guess==choosen_word[i]:
    #         print("right")
    #     else:
    #         print("wrong")

    #***************OR******************

    # for i in choosen_word:
    #     if guess==i:
    #         print("right")
    #     else:
    #         print("wrong")

    #TODO 5: create a display that put the guessed letter at right place
    # just updating upper para

    #TODO 7:update the loop to print display with previous letter  
    display=""
    for i in choosen_word:
        if guess==i:
            display+=i
            correct_letters.append(i)
        elif i in correct_letters:
            display+=i
        else:
            display+="_"
    print(display)

    if guess not in choosen_word:
      lives-=1
      print(f"you guessed {guess} which is not in word, you lose a life")
      print(f"***********you have {lives}/6 lives left************")
      if lives==0:
        game_over=True
        print("******************YOU LOSE******************")
    
  
    print(hangmanpics[lives])
    
    
    if "_" not in display:
        game_over=True
        print("*******************YOU WIN*******************")
    
    
    
        
    



