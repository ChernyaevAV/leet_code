def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    prefix = vocab_words[0]
    res = map(lambda x: prefix + x, vocab_words[1:])
    return prefix + " :: " + " :: ".join(res)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    # word = word.rstrip("ness")
    # if word.endswith("i"):
    #     return word[:-1] + "y"
    # else:
    #     return word
    return word.replace("iness", "y").replace("ness", "")


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    return sentence.split()[index].strip(".,!?") + "en"

assert make_word_groups(['en', 'close', 'joy', 'lighten']) == 'en :: enclose :: enjoy :: enlighten'
assert remove_suffix_ness("sadness") == "sad"
assert adjective_to_verb('I need to make that bright.', -1 ) == 'brighten'
assert adjective_to_verb('It got dark as the sun set.', 2) == 'darken'