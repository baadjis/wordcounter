from functools import lru_cache

# define punctuations or quotes
opens = [' ', '\n', '(', '\u00AB', '\u201d', '\u201c', ':']
#define closing
closes = opens + ['?', '.', '!', ',', ')', '"', '\u00BB']


@lru_cache()
def strip_stuff(text: str) -> str:
    """
    Return the text without some stuff i don't want to see
    """
    return text.strip('_').strip("''")


@lru_cache()
def lower(text: str) -> str:
    "Return lower case of the text"
    return text.lower()


@lru_cache()
def end_with_opens(word: str) -> bool:
    " chek if a word ends with any the open character "
    for o in opens:
        if word.endswith(o):
            return True
    return False


@lru_cache()
def start_with_open(word: str) -> bool:
    " chek if a word starts with any of the open character "
    for o in opens:
        if word.startswith(o):
            return True

    return False


@lru_cache()
def end_with_close(word: str) -> bool:
    " chek if a word ends with any of the closes character "
    for c in closes:
        if word.endswith(c):
            return True
    return False


@lru_cache()
def start_with_close(word: str) -> bool:
    " chek if a word start with any the open character "
    for c in closes:
        if word.startswith(c):
            return True
    return False


def count_occurrences_in_text(word: str, text: str) -> int:
    """
    Return the number of occurrences of the passed word (case insensitive) in text
    """

    # TODO: your code goes here, but it's OK to add new functions or import modules if needed
    # strip some chars
    text_words = lower(strip_stuff(text))
    # lower
    word = lower(word)
    # split the into tokens using the word as a separator
    text_words = text_words.split(word)

    l = len(text_words)
    count = 0

    for i in range(l - 1):
        if i == 0:
            # check the first token condition
            if (text_words[i] == '' or end_with_opens(text_words[i])) and \
                    (text_words[i + 1] == '' or start_with_close(text_words[i + 1])):
                count += 1

        elif i == l - 2:
            # but here we must check the border condition

            if end_with_opens(text_words[i]) and (text_words[i + 1] == '' or start_with_close(text_words[i + 1])):
                count += 1

        # if i> 0 and i<l-2
        # no border condition
        else:

            # just check if the token  ends with opens chars and the following start with close char
            # and increment the counter
            if end_with_opens(text_words[i]) and start_with_close(text_words[i + 1]):
                count += 1
    return count