### HANGMAN ####
### This is a hangman game code, User will have 6 lives to guess the letter and complete the word.

#import hangman word_list,logo and stages 
import random
import hangman_art
import hangman_words


print(hangman_art.logo)

# Before importing the words list, you can create 3 words list to create the program.
# word_list = ["apple" , "pear" , "carrot" , "watermelon" ]

chosen_word = random.choice(hangman_words.word_list)
lives = 6

# print(f"Hush your chosen word is {chosen_word}")

length = len(chosen_word)

# creating an empty list to display the output
final = []
for i in range(0,length):
    final.append("_")

while 0 < lives:
    guess = input("Guess a letter : ").lower()
    if guess in chosen_word and guess in final:
        print(f"You've already guessed {guess}")
        print(final)
        print(hangman_art.stages[lives])
    elif guess in chosen_word:
        for i in range(0,length):
            if guess == chosen_word[i]:
                final[i] = guess
        print(final)
        print(hangman_art.stages[lives])
              
        
    else:
        lives -= 1
        if lives == 0:
            print(f"You guessed {guess}, that's not in word. You lose a life.")
            print("You lose.")
            print(final)
            print(hangman_art.stages[lives])
            
        else:    
            print(f"You guessed {guess}, that's not in word. You lose a life.")
            print(final)
            print(hangman_art.stages[lives])
        
        
        

        