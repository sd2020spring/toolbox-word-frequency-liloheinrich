"""Analyze the word frequencies in a book downloaded from Project Gutenberg."""

import string
import re

def get_word_list(filename):
    """Read the specified project Gutenberg book.

    Header comments, punctuation, and whitespace are stripped away. The function
    returns a list of the words used in the book as a list. All words are
    converted to lower case.
    """
    words = []
    rem = string.punctuation+string.whitespace
    with open(filename) as fp:
        read = False
        for line in fp:
            if line.find('START OF THIS PROJECT GUTENBERG EBOOK'):
                read = True
            elif line.find('END OF THIS PROJECT GUTENBERG EBOOK'):
                read = False

            if read:
                k = re.findall(r"[\w']+", line)
                for w in k:
                    w = w.strip().lower()
                    w = w.translate(str.maketrans('', '', rem))
                    words.append(w)
    return words

def get_top_n_words(word_list, n):
    """Take a list of words as input and return a list of the n most
    frequently-occurring words ordered from most- to least-frequent.

    Parameters
    ----------
    word_list: [str]
        A list of words. These are assumed to all be in lower case, with no
        punctuation.
    n: int
        The number of words to return.

    Returns
    -------
    int
        The n most frequently occurring words ordered from most to least.
    frequently to least frequently occurring
    """
    d = dict()
    for word in word_list:
        d[word] = d.get(word,0) + 1

    ordered = sorted(d.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)

    words = []
    for tup in ordered:
        if len(words) == n:
            break
        words.append(tup[0])
    return words

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")

    books = ["pg32325.txt", "verne A Journey to the Centre of the Earth.txt",
            "asimov Worlds Within Worlds: The Story of Nuclear Energy.txt",
            "wells Tales of Space and Time.txt"]

    for i in books:
        print(i)
        word_list = get_word_list(i)
        print(len(word_list))
        top_words = get_top_n_words(word_list, 100)
        print(top_words, '\n')
