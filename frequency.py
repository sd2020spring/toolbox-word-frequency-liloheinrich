"""Analyze the word frequencies in a book downloaded from Project Gutenberg."""

import string


def get_word_list(file_name):
    """Read the specified project Gutenberg book.

    Header comments, punctuation, and whitespace are stripped away. The function
    returns a list of the words used in the book as a list. All words are
    converted to lower case.
    """
    pass


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
    frequently to least frequentlyoccurring
    """
    pass


if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(string.punctuation)
