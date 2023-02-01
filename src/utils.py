from termcolor import colored, cprint
from typing import List, Tuple

def read_file(filepath: str) -> List[Tuple]:
    # read data
    with open(filepath) as f:
        data = f.read()

        # split, make list of tuple, and remove None
        data = [tuple(item.split(',')) for item in data.split('\n')[1:] if bool(item) == True]

        # change data type to int for frequency
        data = [(tup[0], int(tup[1])) for tup in data]

        #sort frequency as decending
        data = sorted(data, key=lambda x: x[1], reverse=True)

        # select 5 letters words
        data = list(filter(lambda w: len(w[0])==5, data))

    return data

def generate_word_frequency():

    """ input: a file path and read_file function,
        output = all 5 letters word with most frequency
    """
    file_path = 'src/unigram_freq.csv'
    data = read_file(file_path)

    words = [item[0] for item in data]

    return words


def print_success(text, end=' '):
    print(colored(text, 'green', attrs=['reverse']), end=' ')

def print_warning(text, end=' '):
    print(colored(text, 'yellow', attrs=['reverse']), end=' ')

def print_error(text, end=' '):
    print(colored(text, 'red', attrs=['reverse']), end=' ')

def print_novalid(text, end=' '):
    print(colored(text, 'grey', attrs=['reverse']), end=' ')
