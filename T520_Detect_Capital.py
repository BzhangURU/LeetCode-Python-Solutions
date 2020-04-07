##Given a word, you need to judge whether the usage of capitals in it is right or not.
##
##We define the usage of capitals in a word to be right when one of the following cases holds:
##
##All letters in this word are capitals, like "USA".
##All letters in this word are not capitals, like "leetcode".
##Only the first letter in this word is capital, like "Google".
##Otherwise, we define that this word doesn't use capitals in a right way.
import re
def detectCapitalUse(word: str) -> bool:
    pattern=r'[a-z]+$|[A-Z][a-z]+$|[A-Z]+$'
    if re.match(pattern,word):
        return True
    else:
        return False
