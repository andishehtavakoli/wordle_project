import random

from src.utils import (generate_word_frequency, print_error, print_novalid,
                       print_success, print_warning, read_file)


def wodle_runner():

    # read word
    words = generate_word_frequency()
    word = random.choice(words)

    num_try = 5

    while True:
        guess_word = input(f'Please enter the 5 letters word and enter q for exit: ')
        if guess_word == 'q':
            break

        num_try -= 1
        if num_try==0:
            print_error(f'Game is over! You are a NOOB:). Correct answer is: {word}')
            break


        if len(guess_word) != 5:
            print(f'the word is not 5 letters. Correct it!')
            continue

        # check valid letter, invalid position, invalid letter, invalid word
        for w, g_w in zip(word, guess_word):

            # valid letter
            if w == g_w:
                print_success(g_w)


            # invalid position
            elif g_w in word:
                print_warning(g_w)

            #invalid word
            elif g_w not in word:
                print_error(g_w)

            # word does not exist
            else:
                print_novalid(g_w)

        # Check
        if word == guess_word:
            print_success('Congratulations!')
            break


if __name__ =='__main__':
    wodle_runner()



